# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface import util


class ListItemDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type_name=None, item_name=None, specification=None, count=None, unit_price=None, count_price=None, drug_classification=None, drug_classification_source=None, own_pay_scale=None, own_pay_amount=None):  # noqa: E501
        """ListItemDto - a model defined in OpenAPI

        :param type_name: The type_name of this ListItemDto.  # noqa: E501
        :type type_name: str
        :param item_name: The item_name of this ListItemDto.  # noqa: E501
        :type item_name: str
        :param specification: The specification of this ListItemDto.  # noqa: E501
        :type specification: str
        :param count: The count of this ListItemDto.  # noqa: E501
        :type count: float
        :param unit_price: The unit_price of this ListItemDto.  # noqa: E501
        :type unit_price: float
        :param count_price: The count_price of this ListItemDto.  # noqa: E501
        :type count_price: float
        :param drug_classification: The drug_classification of this ListItemDto.  # noqa: E501
        :type drug_classification: str
        :param drug_classification_source: The drug_classification_source of this ListItemDto.  # noqa: E501
        :type drug_classification_source: str
        :param own_pay_scale: The own_pay_scale of this ListItemDto.  # noqa: E501
        :type own_pay_scale: float
        :param own_pay_amount: The own_pay_amount of this ListItemDto.  # noqa: E501
        :type own_pay_amount: float
        """
        self.openapi_types = {
            'type_name': str,
            'item_name': str,
            'specification': str,
            'count': float,
            'unit_price': float,
            'count_price': float,
            'drug_classification': str,
            'drug_classification_source': str,
            'own_pay_scale': float,
            'own_pay_amount': float
        }

        self.attribute_map = {
            'type_name': 'typeName',
            'item_name': 'itemName',
            'specification': 'specification',
            'count': 'count',
            'unit_price': 'unitPrice',
            'count_price': 'countPrice',
            'drug_classification': 'drugClassification',
            'drug_classification_source': 'drugClassificationSource',
            'own_pay_scale': 'ownPayScale',
            'own_pay_amount': 'ownPayAmount'
        }

        self._type_name = type_name
        self._item_name = item_name
        self._specification = specification
        self._count = count
        self._unit_price = unit_price
        self._count_price = count_price
        self._drug_classification = drug_classification
        self._drug_classification_source = drug_classification_source
        self._own_pay_scale = own_pay_scale
        self._own_pay_amount = own_pay_amount

    @classmethod
    def from_dict(cls, dikt) -> 'ListItemDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListItemDto of this ListItemDto.  # noqa: E501
        :rtype: ListItemDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type_name(self):
        """Gets the type_name of this ListItemDto.

        大项名称。例如：“西药费”、“中药费“  # noqa: E501

        :return: The type_name of this ListItemDto.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this ListItemDto.

        大项名称。例如：“西药费”、“中药费“  # noqa: E501

        :param type_name: The type_name of this ListItemDto.
        :type type_name: str
        """

        self._type_name = type_name

    @property
    def item_name(self):
        """Gets the item_name of this ListItemDto.

        项目名称。例如：氯化钠注射液  # noqa: E501

        :return: The item_name of this ListItemDto.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this ListItemDto.

        项目名称。例如：氯化钠注射液  # noqa: E501

        :param item_name: The item_name of this ListItemDto.
        :type item_name: str
        """

        self._item_name = item_name

    @property
    def specification(self):
        """Gets the specification of this ListItemDto.

        规格  # noqa: E501

        :return: The specification of this ListItemDto.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this ListItemDto.

        规格  # noqa: E501

        :param specification: The specification of this ListItemDto.
        :type specification: str
        """

        self._specification = specification

    @property
    def count(self):
        """Gets the count of this ListItemDto.

        数量  # noqa: E501

        :return: The count of this ListItemDto.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListItemDto.

        数量  # noqa: E501

        :param count: The count of this ListItemDto.
        :type count: float
        """

        self._count = count

    @property
    def unit_price(self):
        """Gets the unit_price of this ListItemDto.

        单价  # noqa: E501

        :return: The unit_price of this ListItemDto.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ListItemDto.

        单价  # noqa: E501

        :param unit_price: The unit_price of this ListItemDto.
        :type unit_price: float
        """

        self._unit_price = unit_price

    @property
    def count_price(self):
        """Gets the count_price of this ListItemDto.

        费用金额  # noqa: E501

        :return: The count_price of this ListItemDto.
        :rtype: float
        """
        return self._count_price

    @count_price.setter
    def count_price(self, count_price):
        """Sets the count_price of this ListItemDto.

        费用金额  # noqa: E501

        :param count_price: The count_price of this ListItemDto.
        :type count_price: float
        """

        self._count_price = count_price

    @property
    def drug_classification(self):
        """Gets the drug_classification of this ListItemDto.

        社保标识  # noqa: E501

        :return: The drug_classification of this ListItemDto.
        :rtype: str
        """
        return self._drug_classification

    @drug_classification.setter
    def drug_classification(self, drug_classification):
        """Sets the drug_classification of this ListItemDto.

        社保标识  # noqa: E501

        :param drug_classification: The drug_classification of this ListItemDto.
        :type drug_classification: str
        """
        allowed_values = ["甲", "乙", "自费"]  # noqa: E501
        if drug_classification not in allowed_values:
            raise ValueError(
                "Invalid value for `drug_classification` ({0}), must be one of {1}"
                .format(drug_classification, allowed_values)
            )

        self._drug_classification = drug_classification

    @property
    def drug_classification_source(self):
        """Gets the drug_classification_source of this ListItemDto.

        社保标识来源  # noqa: E501

        :return: The drug_classification_source of this ListItemDto.
        :rtype: str
        """
        return self._drug_classification_source

    @drug_classification_source.setter
    def drug_classification_source(self, drug_classification_source):
        """Sets the drug_classification_source of this ListItemDto.

        社保标识来源  # noqa: E501

        :param drug_classification_source: The drug_classification_source of this ListItemDto.
        :type drug_classification_source: str
        """
        allowed_values = ["清单", "医保库"]  # noqa: E501
        if drug_classification_source not in allowed_values:
            raise ValueError(
                "Invalid value for `drug_classification_source` ({0}), must be one of {1}"
                .format(drug_classification_source, allowed_values)
            )

        self._drug_classification_source = drug_classification_source

    @property
    def own_pay_scale(self):
        """Gets the own_pay_scale of this ListItemDto.

        自付比例  # noqa: E501

        :return: The own_pay_scale of this ListItemDto.
        :rtype: float
        """
        return self._own_pay_scale

    @own_pay_scale.setter
    def own_pay_scale(self, own_pay_scale):
        """Sets the own_pay_scale of this ListItemDto.

        自付比例  # noqa: E501

        :param own_pay_scale: The own_pay_scale of this ListItemDto.
        :type own_pay_scale: float
        """

        self._own_pay_scale = own_pay_scale

    @property
    def own_pay_amount(self):
        """Gets the own_pay_amount of this ListItemDto.

        自付金额  # noqa: E501

        :return: The own_pay_amount of this ListItemDto.
        :rtype: float
        """
        return self._own_pay_amount

    @own_pay_amount.setter
    def own_pay_amount(self, own_pay_amount):
        """Sets the own_pay_amount of this ListItemDto.

        自付金额  # noqa: E501

        :param own_pay_amount: The own_pay_amount of this ListItemDto.
        :type own_pay_amount: float
        """

        self._own_pay_amount = own_pay_amount
