import connexion
import six

from cpic_interface.models.create_case_dto import CreateCaseDto  # noqa: E501
from cpic_interface.models.create_case_res_dto import CreateCaseResDto  # noqa: E501
from cpic_interface import util


def create_case(create_case_dto=None):  # noqa: E501
    """用于接收渠道推送的案件信息

     # noqa: E501

    :param create_case_dto: 
    :type create_case_dto: dict | bytes

    :rtype: CreateCaseResDto
    """
    if connexion.request.is_json:
        create_case_dto = CreateCaseDto.from_dict(connexion.request.get_json())  # noqa: E501

    create_case_res_dto = CreateCaseResDto.from_dict({"code": 200, "data": {"caseNo": "9"}})  # noqa: E501

    return create_case_res_dto
