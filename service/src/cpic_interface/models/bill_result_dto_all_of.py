# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface import util


class BillResultDtoAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total_amount=None, all_expense_amount=None, parts_expense_amount=None, reimbursement_amount=None, remark=None):  # noqa: E501
        """BillResultDtoAllOf - a model defined in OpenAPI

        :param total_amount: The total_amount of this BillResultDtoAllOf.  # noqa: E501
        :type total_amount: float
        :param all_expense_amount: The all_expense_amount of this BillResultDtoAllOf.  # noqa: E501
        :type all_expense_amount: float
        :param parts_expense_amount: The parts_expense_amount of this BillResultDtoAllOf.  # noqa: E501
        :type parts_expense_amount: float
        :param reimbursement_amount: The reimbursement_amount of this BillResultDtoAllOf.  # noqa: E501
        :type reimbursement_amount: float
        :param remark: The remark of this BillResultDtoAllOf.  # noqa: E501
        :type remark: str
        """
        self.openapi_types = {
            'total_amount': float,
            'all_expense_amount': float,
            'parts_expense_amount': float,
            'reimbursement_amount': float,
            'remark': str
        }

        self.attribute_map = {
            'total_amount': 'totalAmount',
            'all_expense_amount': 'allExpenseAmount',
            'parts_expense_amount': 'partsExpenseAmount',
            'reimbursement_amount': 'reimbursementAmount',
            'remark': 'remark'
        }

        self._total_amount = total_amount
        self._all_expense_amount = all_expense_amount
        self._parts_expense_amount = parts_expense_amount
        self._reimbursement_amount = reimbursement_amount
        self._remark = remark

    @classmethod
    def from_dict(cls, dikt) -> 'BillResultDtoAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BillResultDto_allOf of this BillResultDtoAllOf.  # noqa: E501
        :rtype: BillResultDtoAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_amount(self):
        """Gets the total_amount of this BillResultDtoAllOf.

        总金额  # noqa: E501

        :return: The total_amount of this BillResultDtoAllOf.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this BillResultDtoAllOf.

        总金额  # noqa: E501

        :param total_amount: The total_amount of this BillResultDtoAllOf.
        :type total_amount: float
        """

        self._total_amount = total_amount

    @property
    def all_expense_amount(self):
        """Gets the all_expense_amount of this BillResultDtoAllOf.

        全部自费金额  # noqa: E501

        :return: The all_expense_amount of this BillResultDtoAllOf.
        :rtype: float
        """
        return self._all_expense_amount

    @all_expense_amount.setter
    def all_expense_amount(self, all_expense_amount):
        """Sets the all_expense_amount of this BillResultDtoAllOf.

        全部自费金额  # noqa: E501

        :param all_expense_amount: The all_expense_amount of this BillResultDtoAllOf.
        :type all_expense_amount: float
        """

        self._all_expense_amount = all_expense_amount

    @property
    def parts_expense_amount(self):
        """Gets the parts_expense_amount of this BillResultDtoAllOf.

        部分自费金额  # noqa: E501

        :return: The parts_expense_amount of this BillResultDtoAllOf.
        :rtype: float
        """
        return self._parts_expense_amount

    @parts_expense_amount.setter
    def parts_expense_amount(self, parts_expense_amount):
        """Sets the parts_expense_amount of this BillResultDtoAllOf.

        部分自费金额  # noqa: E501

        :param parts_expense_amount: The parts_expense_amount of this BillResultDtoAllOf.
        :type parts_expense_amount: float
        """

        self._parts_expense_amount = parts_expense_amount

    @property
    def reimbursement_amount(self):
        """Gets the reimbursement_amount of this BillResultDtoAllOf.

        医保报销金额  # noqa: E501

        :return: The reimbursement_amount of this BillResultDtoAllOf.
        :rtype: float
        """
        return self._reimbursement_amount

    @reimbursement_amount.setter
    def reimbursement_amount(self, reimbursement_amount):
        """Sets the reimbursement_amount of this BillResultDtoAllOf.

        医保报销金额  # noqa: E501

        :param reimbursement_amount: The reimbursement_amount of this BillResultDtoAllOf.
        :type reimbursement_amount: float
        """

        self._reimbursement_amount = reimbursement_amount

    @property
    def remark(self):
        """Gets the remark of this BillResultDtoAllOf.

        备注  # noqa: E501

        :return: The remark of this BillResultDtoAllOf.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BillResultDtoAllOf.

        备注  # noqa: E501

        :param remark: The remark of this BillResultDtoAllOf.
        :type remark: str
        """

        self._remark = remark
