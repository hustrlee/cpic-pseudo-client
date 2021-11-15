# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface.models.invoice_basic_info_dto import InvoiceBasicInfoDto
from cpic_interface import util

from cpic_interface.models.invoice_basic_info_dto import InvoiceBasicInfoDto  # noqa: E501

class CaseInfoDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, case_no=None, regist_no=None, insure_name=None, insurecode=None, cost_type=None, invoice_total_amount=None, admission_date=None, discharge_date=None, hospitalization_days=None, invoice_list=None):  # noqa: E501
        """CaseInfoDto - a model defined in OpenAPI

        :param case_no: The case_no of this CaseInfoDto.  # noqa: E501
        :type case_no: str
        :param regist_no: The regist_no of this CaseInfoDto.  # noqa: E501
        :type regist_no: str
        :param insure_name: The insure_name of this CaseInfoDto.  # noqa: E501
        :type insure_name: str
        :param insurecode: The insurecode of this CaseInfoDto.  # noqa: E501
        :type insurecode: str
        :param cost_type: The cost_type of this CaseInfoDto.  # noqa: E501
        :type cost_type: str
        :param invoice_total_amount: The invoice_total_amount of this CaseInfoDto.  # noqa: E501
        :type invoice_total_amount: float
        :param admission_date: The admission_date of this CaseInfoDto.  # noqa: E501
        :type admission_date: str
        :param discharge_date: The discharge_date of this CaseInfoDto.  # noqa: E501
        :type discharge_date: str
        :param hospitalization_days: The hospitalization_days of this CaseInfoDto.  # noqa: E501
        :type hospitalization_days: float
        :param invoice_list: The invoice_list of this CaseInfoDto.  # noqa: E501
        :type invoice_list: List[InvoiceBasicInfoDto]
        """
        self.openapi_types = {
            'case_no': str,
            'regist_no': str,
            'insure_name': str,
            'insurecode': str,
            'cost_type': str,
            'invoice_total_amount': float,
            'admission_date': str,
            'discharge_date': str,
            'hospitalization_days': float,
            'invoice_list': List[InvoiceBasicInfoDto]
        }

        self.attribute_map = {
            'case_no': 'caseNo',
            'regist_no': 'registNo',
            'insure_name': 'insureName',
            'insurecode': 'insurecode',
            'cost_type': 'costType',
            'invoice_total_amount': 'invoiceTotalAmount',
            'admission_date': 'admissionDate',
            'discharge_date': 'dischargeDate',
            'hospitalization_days': 'hospitalizationDays',
            'invoice_list': 'invoiceList'
        }

        self._case_no = case_no
        self._regist_no = regist_no
        self._insure_name = insure_name
        self._insurecode = insurecode
        self._cost_type = cost_type
        self._invoice_total_amount = invoice_total_amount
        self._admission_date = admission_date
        self._discharge_date = discharge_date
        self._hospitalization_days = hospitalization_days
        self._invoice_list = invoice_list

    @classmethod
    def from_dict(cls, dikt) -> 'CaseInfoDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CaseInfoDto of this CaseInfoDto.  # noqa: E501
        :rtype: CaseInfoDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def case_no(self):
        """Gets the case_no of this CaseInfoDto.

        任务号  # noqa: E501

        :return: The case_no of this CaseInfoDto.
        :rtype: str
        """
        return self._case_no

    @case_no.setter
    def case_no(self, case_no):
        """Sets the case_no of this CaseInfoDto.

        任务号  # noqa: E501

        :param case_no: The case_no of this CaseInfoDto.
        :type case_no: str
        """

        self._case_no = case_no

    @property
    def regist_no(self):
        """Gets the regist_no of this CaseInfoDto.

        报案号  # noqa: E501

        :return: The regist_no of this CaseInfoDto.
        :rtype: str
        """
        return self._regist_no

    @regist_no.setter
    def regist_no(self, regist_no):
        """Sets the regist_no of this CaseInfoDto.

        报案号  # noqa: E501

        :param regist_no: The regist_no of this CaseInfoDto.
        :type regist_no: str
        """

        self._regist_no = regist_no

    @property
    def insure_name(self):
        """Gets the insure_name of this CaseInfoDto.

        被保险人姓名  # noqa: E501

        :return: The insure_name of this CaseInfoDto.
        :rtype: str
        """
        return self._insure_name

    @insure_name.setter
    def insure_name(self, insure_name):
        """Sets the insure_name of this CaseInfoDto.

        被保险人姓名  # noqa: E501

        :param insure_name: The insure_name of this CaseInfoDto.
        :type insure_name: str
        """

        self._insure_name = insure_name

    @property
    def insurecode(self):
        """Gets the insurecode of this CaseInfoDto.

        被保险人身份证号  # noqa: E501

        :return: The insurecode of this CaseInfoDto.
        :rtype: str
        """
        return self._insurecode

    @insurecode.setter
    def insurecode(self, insurecode):
        """Sets the insurecode of this CaseInfoDto.

        被保险人身份证号  # noqa: E501

        :param insurecode: The insurecode of this CaseInfoDto.
        :type insurecode: str
        """

        self._insurecode = insurecode

    @property
    def cost_type(self):
        """Gets the cost_type of this CaseInfoDto.

        费用类型  # noqa: E501

        :return: The cost_type of this CaseInfoDto.
        :rtype: str
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this CaseInfoDto.

        费用类型  # noqa: E501

        :param cost_type: The cost_type of this CaseInfoDto.
        :type cost_type: str
        """
        allowed_values = ["门诊", "住院", "外购药"]  # noqa: E501
        if cost_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cost_type` ({0}), must be one of {1}"
                .format(cost_type, allowed_values)
            )

        self._cost_type = cost_type

    @property
    def invoice_total_amount(self):
        """Gets the invoice_total_amount of this CaseInfoDto.

        案件下所有发票的总金额  # noqa: E501

        :return: The invoice_total_amount of this CaseInfoDto.
        :rtype: float
        """
        return self._invoice_total_amount

    @invoice_total_amount.setter
    def invoice_total_amount(self, invoice_total_amount):
        """Sets the invoice_total_amount of this CaseInfoDto.

        案件下所有发票的总金额  # noqa: E501

        :param invoice_total_amount: The invoice_total_amount of this CaseInfoDto.
        :type invoice_total_amount: float
        """

        self._invoice_total_amount = invoice_total_amount

    @property
    def admission_date(self):
        """Gets the admission_date of this CaseInfoDto.

        入院日期  # noqa: E501

        :return: The admission_date of this CaseInfoDto.
        :rtype: str
        """
        return self._admission_date

    @admission_date.setter
    def admission_date(self, admission_date):
        """Sets the admission_date of this CaseInfoDto.

        入院日期  # noqa: E501

        :param admission_date: The admission_date of this CaseInfoDto.
        :type admission_date: str
        """

        self._admission_date = admission_date

    @property
    def discharge_date(self):
        """Gets the discharge_date of this CaseInfoDto.

        出院日期  # noqa: E501

        :return: The discharge_date of this CaseInfoDto.
        :rtype: str
        """
        return self._discharge_date

    @discharge_date.setter
    def discharge_date(self, discharge_date):
        """Sets the discharge_date of this CaseInfoDto.

        出院日期  # noqa: E501

        :param discharge_date: The discharge_date of this CaseInfoDto.
        :type discharge_date: str
        """

        self._discharge_date = discharge_date

    @property
    def hospitalization_days(self):
        """Gets the hospitalization_days of this CaseInfoDto.

        住院天数  # noqa: E501

        :return: The hospitalization_days of this CaseInfoDto.
        :rtype: float
        """
        return self._hospitalization_days

    @hospitalization_days.setter
    def hospitalization_days(self, hospitalization_days):
        """Sets the hospitalization_days of this CaseInfoDto.

        住院天数  # noqa: E501

        :param hospitalization_days: The hospitalization_days of this CaseInfoDto.
        :type hospitalization_days: float
        """

        self._hospitalization_days = hospitalization_days

    @property
    def invoice_list(self):
        """Gets the invoice_list of this CaseInfoDto.

        发票详情列表  # noqa: E501

        :return: The invoice_list of this CaseInfoDto.
        :rtype: List[InvoiceBasicInfoDto]
        """
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, invoice_list):
        """Sets the invoice_list of this CaseInfoDto.

        发票详情列表  # noqa: E501

        :param invoice_list: The invoice_list of this CaseInfoDto.
        :type invoice_list: List[InvoiceBasicInfoDto]
        """

        self._invoice_list = invoice_list