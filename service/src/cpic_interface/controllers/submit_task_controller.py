import connexion
import six

from cpic_interface.models.create_case_dto import CreateCaseDto  # noqa: E501
from cpic_interface.models.create_case_res_dto import CreateCaseResDto  # noqa: E501
from cpic_interface import util
from cpic_interface.db_models import Customer
from cpic_interface import GDTB_CUSTID


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
        return 'status 400 demo', 405

    # 解码 token

    # 校验客户 appkey 是否正确

    # 校验 sign 是否正确

    # 生成 caseNo

    # 将任务推送到 rabbitMQ

    # 检查是否需要返回 Case_Info

    return gdtb.to_dict()
