# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface import util


class OtherResultDtoAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ocr_result=None, remark=None):  # noqa: E501
        """OtherResultDtoAllOf - a model defined in OpenAPI

        :param ocr_result: The ocr_result of this OtherResultDtoAllOf.  # noqa: E501
        :type ocr_result: str
        :param remark: The remark of this OtherResultDtoAllOf.  # noqa: E501
        :type remark: str
        """
        self.openapi_types = {
            'ocr_result': str,
            'remark': str
        }

        self.attribute_map = {
            'ocr_result': 'ocrResult',
            'remark': 'remark'
        }

        self._ocr_result = ocr_result
        self._remark = remark

    @classmethod
    def from_dict(cls, dikt) -> 'OtherResultDtoAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OtherResultDto_allOf of this OtherResultDtoAllOf.  # noqa: E501
        :rtype: OtherResultDtoAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ocr_result(self):
        """Gets the ocr_result of this OtherResultDtoAllOf.

        识别结果，没有具体定义，任意字符串。  # noqa: E501

        :return: The ocr_result of this OtherResultDtoAllOf.
        :rtype: str
        """
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, ocr_result):
        """Sets the ocr_result of this OtherResultDtoAllOf.

        识别结果，没有具体定义，任意字符串。  # noqa: E501

        :param ocr_result: The ocr_result of this OtherResultDtoAllOf.
        :type ocr_result: str
        """

        self._ocr_result = ocr_result

    @property
    def remark(self):
        """Gets the remark of this OtherResultDtoAllOf.

        备注  # noqa: E501

        :return: The remark of this OtherResultDtoAllOf.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this OtherResultDtoAllOf.

        备注  # noqa: E501

        :param remark: The remark of this OtherResultDtoAllOf.
        :type remark: str
        """

        self._remark = remark
