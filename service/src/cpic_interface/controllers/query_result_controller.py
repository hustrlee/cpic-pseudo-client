import connexion
import six

from cpic_interface.models.query_case_dto import QueryCaseDto  # noqa: E501
from cpic_interface.models.query_case_res_dto import QueryCaseResDto  # noqa: E501
from cpic_interface import util


def query_case(query_case_dto=None):  # noqa: E501
    """查询任务状态，及识别结果

     # noqa: E501

    :param query_case_dto: 
    :type query_case_dto: dict | bytes

    :rtype: QueryCaseResDto
    """
    if connexion.request.is_json:
        query_case_dto = QueryCaseDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
