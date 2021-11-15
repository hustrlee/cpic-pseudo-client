# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface.models.image_type_dto import ImageTypeDto
from cpic_interface.models.other_result_dto_all_of import OtherResultDtoAllOf
from cpic_interface import util

from cpic_interface.models.image_type_dto import ImageTypeDto  # noqa: E501
from cpic_interface.models.other_result_dto_all_of import OtherResultDtoAllOf  # noqa: E501

class OtherResultDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image_type=None, image_classification=None, ocr_result=None, remark=None):  # noqa: E501
        """OtherResultDto - a model defined in OpenAPI

        :param image_type: The image_type of this OtherResultDto.  # noqa: E501
        :type image_type: str
        :param image_classification: The image_classification of this OtherResultDto.  # noqa: E501
        :type image_classification: str
        :param ocr_result: The ocr_result of this OtherResultDto.  # noqa: E501
        :type ocr_result: str
        :param remark: The remark of this OtherResultDto.  # noqa: E501
        :type remark: str
        """
        self.openapi_types = {
            'image_type': str,
            'image_classification': str,
            'ocr_result': str,
            'remark': str
        }

        self.attribute_map = {
            'image_type': 'imageType',
            'image_classification': 'imageClassification',
            'ocr_result': 'ocrResult',
            'remark': 'remark'
        }

        self._image_type = image_type
        self._image_classification = image_classification
        self._ocr_result = ocr_result
        self._remark = remark

    @classmethod
    def from_dict(cls, dikt) -> 'OtherResultDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OtherResultDto of this OtherResultDto.  # noqa: E501
        :rtype: OtherResultDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_type(self):
        """Gets the image_type of this OtherResultDto.

        图片类型。  # noqa: E501

        :return: The image_type of this OtherResultDto.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this OtherResultDto.

        图片类型。  # noqa: E501

        :param image_type: The image_type of this OtherResultDto.
        :type image_type: str
        """
        allowed_values = ["发票", "清单", "结算单", "其它"]  # noqa: E501
        if image_type not in allowed_values:
            raise ValueError(
                "Invalid value for `image_type` ({0}), must be one of {1}"
                .format(image_type, allowed_values)
            )

        self._image_type = image_type

    @property
    def image_classification(self):
        """Gets the image_classification of this OtherResultDto.

        图片分类  # noqa: E501

        :return: The image_classification of this OtherResultDto.
        :rtype: str
        """
        return self._image_classification

    @image_classification.setter
    def image_classification(self, image_classification):
        """Sets the image_classification of this OtherResultDto.

        图片分类  # noqa: E501

        :param image_classification: The image_classification of this OtherResultDto.
        :type image_classification: str
        """
        allowed_values = ["门诊发票", "住院发票", "外购药发票", "门诊清单", "住院清单", "结算单", "其它"]  # noqa: E501
        if image_classification not in allowed_values:
            raise ValueError(
                "Invalid value for `image_classification` ({0}), must be one of {1}"
                .format(image_classification, allowed_values)
            )

        self._image_classification = image_classification

    @property
    def ocr_result(self):
        """Gets the ocr_result of this OtherResultDto.

        识别结果，没有具体定义，任意字符串。  # noqa: E501

        :return: The ocr_result of this OtherResultDto.
        :rtype: str
        """
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, ocr_result):
        """Sets the ocr_result of this OtherResultDto.

        识别结果，没有具体定义，任意字符串。  # noqa: E501

        :param ocr_result: The ocr_result of this OtherResultDto.
        :type ocr_result: str
        """

        self._ocr_result = ocr_result

    @property
    def remark(self):
        """Gets the remark of this OtherResultDto.

        备注  # noqa: E501

        :return: The remark of this OtherResultDto.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this OtherResultDto.

        备注  # noqa: E501

        :param remark: The remark of this OtherResultDto.
        :type remark: str
        """

        self._remark = remark