# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface.models.bill_result_dto import BillResultDto
from cpic_interface.models.invoice_result_dto import InvoiceResultDto
from cpic_interface.models.list_result_dto import ListResultDto
from cpic_interface.models.other_result_dto import OtherResultDto
from cpic_interface import util

from cpic_interface.models.bill_result_dto import BillResultDto  # noqa: E501
from cpic_interface.models.invoice_result_dto import InvoiceResultDto  # noqa: E501
from cpic_interface.models.list_result_dto import ListResultDto  # noqa: E501
from cpic_interface.models.other_result_dto import OtherResultDto  # noqa: E501

class ImageResultDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image_id=None, image_name=None, more_than_one_list=None, remark=None, details1=None, details2=None, details3=None, details4=None):  # noqa: E501
        """ImageResultDto - a model defined in OpenAPI

        :param image_id: The image_id of this ImageResultDto.  # noqa: E501
        :type image_id: str
        :param image_name: The image_name of this ImageResultDto.  # noqa: E501
        :type image_name: str
        :param more_than_one_list: The more_than_one_list of this ImageResultDto.  # noqa: E501
        :type more_than_one_list: float
        :param remark: The remark of this ImageResultDto.  # noqa: E501
        :type remark: str
        :param details1: The details1 of this ImageResultDto.  # noqa: E501
        :type details1: List[InvoiceResultDto]
        :param details2: The details2 of this ImageResultDto.  # noqa: E501
        :type details2: List[ListResultDto]
        :param details3: The details3 of this ImageResultDto.  # noqa: E501
        :type details3: List[BillResultDto]
        :param details4: The details4 of this ImageResultDto.  # noqa: E501
        :type details4: List[OtherResultDto]
        """
        self.openapi_types = {
            'image_id': str,
            'image_name': str,
            'more_than_one_list': float,
            'remark': str,
            'details1': List[InvoiceResultDto],
            'details2': List[ListResultDto],
            'details3': List[BillResultDto],
            'details4': List[OtherResultDto]
        }

        self.attribute_map = {
            'image_id': 'imageId',
            'image_name': 'imageName',
            'more_than_one_list': 'moreThanOneList',
            'remark': 'remark',
            'details1': 'details1',
            'details2': 'details2',
            'details3': 'details3',
            'details4': 'details4'
        }

        self._image_id = image_id
        self._image_name = image_name
        self._more_than_one_list = more_than_one_list
        self._remark = remark
        self._details1 = details1
        self._details2 = details2
        self._details3 = details3
        self._details4 = details4

    @classmethod
    def from_dict(cls, dikt) -> 'ImageResultDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageResultDto of this ImageResultDto.  # noqa: E501
        :rtype: ImageResultDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_id(self):
        """Gets the image_id of this ImageResultDto.

        图片 ID  # noqa: E501

        :return: The image_id of this ImageResultDto.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageResultDto.

        图片 ID  # noqa: E501

        :param image_id: The image_id of this ImageResultDto.
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this ImageResultDto.

        图片名称  # noqa: E501

        :return: The image_name of this ImageResultDto.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ImageResultDto.

        图片名称  # noqa: E501

        :param image_name: The image_name of this ImageResultDto.
        :type image_name: str
        """

        self._image_name = image_name

    @property
    def more_than_one_list(self):
        """Gets the more_than_one_list of this ImageResultDto.

        是否一图多票。1：是；2：否  # noqa: E501

        :return: The more_than_one_list of this ImageResultDto.
        :rtype: float
        """
        return self._more_than_one_list

    @more_than_one_list.setter
    def more_than_one_list(self, more_than_one_list):
        """Sets the more_than_one_list of this ImageResultDto.

        是否一图多票。1：是；2：否  # noqa: E501

        :param more_than_one_list: The more_than_one_list of this ImageResultDto.
        :type more_than_one_list: float
        """

        self._more_than_one_list = more_than_one_list

    @property
    def remark(self):
        """Gets the remark of this ImageResultDto.

        备注  # noqa: E501

        :return: The remark of this ImageResultDto.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ImageResultDto.

        备注  # noqa: E501

        :param remark: The remark of this ImageResultDto.
        :type remark: str
        """

        self._remark = remark

    @property
    def details1(self):
        """Gets the details1 of this ImageResultDto.

        发票详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :return: The details1 of this ImageResultDto.
        :rtype: List[InvoiceResultDto]
        """
        return self._details1

    @details1.setter
    def details1(self, details1):
        """Sets the details1 of this ImageResultDto.

        发票详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :param details1: The details1 of this ImageResultDto.
        :type details1: List[InvoiceResultDto]
        """

        self._details1 = details1

    @property
    def details2(self):
        """Gets the details2 of this ImageResultDto.

        清单详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :return: The details2 of this ImageResultDto.
        :rtype: List[ListResultDto]
        """
        return self._details2

    @details2.setter
    def details2(self, details2):
        """Sets the details2 of this ImageResultDto.

        清单详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :param details2: The details2 of this ImageResultDto.
        :type details2: List[ListResultDto]
        """

        self._details2 = details2

    @property
    def details3(self):
        """Gets the details3 of this ImageResultDto.

        结算单详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :return: The details3 of this ImageResultDto.
        :rtype: List[BillResultDto]
        """
        return self._details3

    @details3.setter
    def details3(self, details3):
        """Sets the details3 of this ImageResultDto.

        结算单详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :param details3: The details3 of this ImageResultDto.
        :type details3: List[BillResultDto]
        """

        self._details3 = details3

    @property
    def details4(self):
        """Gets the details4 of this ImageResultDto.

        其它单据详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :return: The details4 of this ImageResultDto.
        :rtype: List[OtherResultDto]
        """
        return self._details4

    @details4.setter
    def details4(self, details4):
        """Sets the details4 of this ImageResultDto.

        其它单据详情。如果一图多票，则返回多个数组元素。  # noqa: E501

        :param details4: The details4 of this ImageResultDto.
        :type details4: List[OtherResultDto]
        """

        self._details4 = details4