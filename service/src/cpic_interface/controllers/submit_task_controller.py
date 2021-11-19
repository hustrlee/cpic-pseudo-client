import connexion
import six
import json
from hashlib import md5
from uuid import uuid1

from cpic_interface.models.create_case_dto import CreateCaseDto  # noqa: E501
from cpic_interface.models.create_case_res_dto import CreateCaseResDto  # noqa: E501
from cpic_interface import util
from cpic_interface import GDTB_CUSTID
from cpic_interface.common.aes_ecb import AESCipher
from cpic_interface.db_config import db
from cpic_interface.db_models import Customer, Case

import pika
from cpic_interface.mq_config import CasePublisher


def create_case(create_case_dto=None):  # noqa: E501
    """用于接收渠道推送的案件信息

     # noqa: E501

    :param create_case_dto: 
    :type create_case_dto: dict | bytes

    :rtype: CreateCaseResDto
    """
    if connexion.request.is_json:
        create_case_dto = CreateCaseDto.from_dict(connexion.request.get_json())  # noqa: E501

    # 获取广东太保的加密参数
    gdtb = Customer.query.filter(Customer.custid == GDTB_CUSTID).one_or_none()

    # 校验客户 ID 是否为广东太保
    if not create_case_dto.custid == gdtb.custid:
        return {"code": 401, "msg": "custid 或 appkey 错误。"}

    try:
        # 解码 token
        token = AESCipher(gdtb.salt).decrypt(create_case_dto.token)
        case_info = json.loads(token)

        # 校验客户 appkey 是否正确
        if not case_info["appkey"] == gdtb.appkey:
            return {"code": 401, "msg": "custid 或 appkey 错误。"}

        # 校验 sign 是否正确
        sign = md5(case_info["appkey"].encode("utf-8"))
        sign.update(case_info["registno"].encode("utf-8"))
        sign.update(case_info["timestamp"].encode("utf-8"))
        sign.update(create_case_dto.uuid.encode("utf-8"))
        sign.update(gdtb.secretkey.encode("utf-8"))
        if not sign.hexdigest() == case_info["sign"]:
            return {"code": 403, "msg": "无效的 sign。"}
    except:
        return {"code": 403, "msg": "无效的 token"}

    # 生成 caseNo
    case_no = str(uuid1())

    #  将任务保存到数据库
    case_record = Case(
        case_no=case_no,
        uuid=create_case_dto.uuid,
        appkey=case_info["appkey"],
        insure_code=case_info["insurecode"],
        insure_name=case_info["insurename"],
        regist_no=case_info["registno"],
        sign=case_info["sign"],
        timestamp=case_info["timestamp"],
        weight=case_info["weight"],
        zmark=case_info["zmark"],
        images=case_info["images"]
    )
    db.session.add(case_record)
    db.session.commit()

    #  将任务推送到 rabbitMQ
    # case_publisher = CasePublisher()

    # case_publisher.connect()
    # case_publisher.publish(msg=json.dumps({"caseNo": case_no, "caseInfo": case_info}).encode())  # noqa
    # case_publisher.close()
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost'))
    # channel = connection.channel()

    # channel.exchange_declare(exchange='case_exchange',
    #                          exchange_type='fanout', durable=True)
    # channel.queue_declare(queue='case_queue', durable=True)
    # channel.queue_bind("case_queue", "case_exchange", routing_key="")

    # channel.basic_publish(
    #     exchange="case_exchange",
    #     routing_key='',
    #     body=json.dumps({"caseNo": case_no, "caseInfo": case_info}).encode(),
    #     properties=pika.BasicProperties(delivery_mode=2)
    # )
    # connection.close()

    # 检查是否需要返回 Case_info
    if create_case_dto.with_case_info_in_return:
        return {"code": 200, "data": {"caseNo": case_no, "caseInfo": case_info}}
    else:
        return {"code": 200, "data": {"caseNo": case_no}}
