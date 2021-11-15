# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface.models.query_case_res_dto_data import QueryCaseResDtoData
from cpic_interface import util

from cpic_interface.models.query_case_res_dto_data import QueryCaseResDtoData  # noqa: E501

class QueryCaseResDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, msg=None, uuid=None, data=None):  # noqa: E501
        """QueryCaseResDto - a model defined in OpenAPI

        :param code: The code of this QueryCaseResDto.  # noqa: E501
        :type code: int
        :param msg: The msg of this QueryCaseResDto.  # noqa: E501
        :type msg: str
        :param uuid: The uuid of this QueryCaseResDto.  # noqa: E501
        :type uuid: str
        :param data: The data of this QueryCaseResDto.  # noqa: E501
        :type data: QueryCaseResDtoData
        """
        self.openapi_types = {
            'code': int,
            'msg': str,
            'uuid': str,
            'data': QueryCaseResDtoData
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'uuid': 'uuid',
            'data': 'data'
        }

        self._code = code
        self._msg = msg
        self._uuid = uuid
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'QueryCaseResDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryCaseResDto of this QueryCaseResDto.  # noqa: E501
        :rtype: QueryCaseResDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this QueryCaseResDto.

        结果代码。200：查询成功  # noqa: E501

        :return: The code of this QueryCaseResDto.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this QueryCaseResDto.

        结果代码。200：查询成功  # noqa: E501

        :param code: The code of this QueryCaseResDto.
        :type code: int
        """

        self._code = code

    @property
    def msg(self):
        """Gets the msg of this QueryCaseResDto.

        发生错误时，返回错误信息。成功时，不返回该字段。  # noqa: E501

        :return: The msg of this QueryCaseResDto.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this QueryCaseResDto.

        发生错误时，返回错误信息。成功时，不返回该字段。  # noqa: E501

        :param msg: The msg of this QueryCaseResDto.
        :type msg: str
        """

        self._msg = msg

    @property
    def uuid(self):
        """Gets the uuid of this QueryCaseResDto.

        创建任务时，由创建方生成的任务唯一标识。  # noqa: E501

        :return: The uuid of this QueryCaseResDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this QueryCaseResDto.

        创建任务时，由创建方生成的任务唯一标识。  # noqa: E501

        :param uuid: The uuid of this QueryCaseResDto.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def data(self):
        """Gets the data of this QueryCaseResDto.


        :return: The data of this QueryCaseResDto.
        :rtype: QueryCaseResDtoData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this QueryCaseResDto.


        :param data: The data of this QueryCaseResDto.
        :type data: QueryCaseResDtoData
        """

        self._data = data
