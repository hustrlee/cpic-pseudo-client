import connexion
import six
import json

from hashlib import md5

from cpic_interface.models.create_case_dto import CreateCaseDto  # noqa: E501
from cpic_interface.models.create_case_res_dto import CreateCaseResDto  # noqa: E501
from cpic_interface import util
from cpic_interface.db_models import Customer
from cpic_interface import GDTB_CUSTID
from cpic_interface.common.aes_ecb import AESCipher


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

    # 解码 token
    try:
        token = AESCipher(gdtb.salt).decrypt(create_case_dto.token)
        case_info = json.loads(token)
    except:
        return {"code": 403, "msg": "无效的 token"}

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

    # 生成 caseNo

    # 将任务推送到 rabbitMQ

    # 检查是否需要返回 Case_info

    return case_info
