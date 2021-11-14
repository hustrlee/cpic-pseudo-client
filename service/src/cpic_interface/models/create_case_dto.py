# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface import util


class CreateCaseDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, custid=None, uuid=None, with_case_info_in_return=None, token=None):  # noqa: E501
        """CreateCaseDto - a model defined in OpenAPI

        :param custid: The custid of this CreateCaseDto.  # noqa: E501
        :type custid: str
        :param uuid: The uuid of this CreateCaseDto.  # noqa: E501
        :type uuid: str
        :param with_case_info_in_return: The with_case_info_in_return of this CreateCaseDto.  # noqa: E501
        :type with_case_info_in_return: bool
        :param token: The token of this CreateCaseDto.  # noqa: E501
        :type token: str
        """
        self.openapi_types = {
            'custid': str,
            'uuid': str,
            'with_case_info_in_return': bool,
            'token': str
        }

        self.attribute_map = {
            'custid': 'custid',
            'uuid': 'uuid',
            'with_case_info_in_return': 'withCaseInfoInReturn',
            'token': 'token'
        }

        self._custid = custid
        self._uuid = uuid
        self._with_case_info_in_return = with_case_info_in_return
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'CreateCaseDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateCaseDto of this CreateCaseDto.  # noqa: E501
        :rtype: CreateCaseDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def custid(self):
        """Gets the custid of this CreateCaseDto.

        客户渠道 ID  # noqa: E501

        :return: The custid of this CreateCaseDto.
        :rtype: str
        """
        return self._custid

    @custid.setter
    def custid(self, custid):
        """Sets the custid of this CreateCaseDto.

        客户渠道 ID  # noqa: E501

        :param custid: The custid of this CreateCaseDto.
        :type custid: str
        """
        if custid is None:
            raise ValueError("Invalid value for `custid`, must not be `None`")  # noqa: E501

        self._custid = custid

    @property
    def uuid(self):
        """Gets the uuid of this CreateCaseDto.

        标识案件的唯一标识，用于客户确认结果。由客户端保证唯一性。  # noqa: E501

        :return: The uuid of this CreateCaseDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CreateCaseDto.

        标识案件的唯一标识，用于客户确认结果。由客户端保证唯一性。  # noqa: E501

        :param uuid: The uuid of this CreateCaseDto.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def with_case_info_in_return(self):
        """Gets the with_case_info_in_return of this CreateCaseDto.

        指示是否返回案件详情，用于检验是否正确提交。默认值：false  # noqa: E501

        :return: The with_case_info_in_return of this CreateCaseDto.
        :rtype: bool
        """
        return self._with_case_info_in_return

    @with_case_info_in_return.setter
    def with_case_info_in_return(self, with_case_info_in_return):
        """Sets the with_case_info_in_return of this CreateCaseDto.

        指示是否返回案件详情，用于检验是否正确提交。默认值：false  # noqa: E501

        :param with_case_info_in_return: The with_case_info_in_return of this CreateCaseDto.
        :type with_case_info_in_return: bool
        """

        self._with_case_info_in_return = with_case_info_in_return

    @property
    def token(self):
        """Gets the token of this CreateCaseDto.

        经过加密后的案件数据信息。  ## 加密方案 ---  为了保证数据的安全性，案件数据采用`aes-256-ecb`加密，加密结果使用`base64`编码。  ### 1. 原始的案件详情数据结构  原始的案件详情数据结构请参考：*OriginalCaseDetailDto*  ### 2. 由平台方分配给用户的参数  | 参数名 | 描述 | 给广东太保分配的值 | |:-------|:-----|:-----------------:| | custid | 用户渠道 ID | 21 | | appkey | 用户授权码 | asdfghjkl | | secretkey | 用户安全码 | dwsuhfci | | salt | 加密密钥明文 | gdtb |  ### 3. 签名  签名，用以校验参数是否被篡改。  **计算方法**：  ``` md5(appkey+registno+timestamp+uuid+secretkey).digest(\"hex\") ```  ### 4. 密钥  `aes-256-ecb`加密需要 32bits 的密钥，因此使用`md5(salt).digest(\"hex\")`作为加密密钥。  ### 5. 加密  Node.js 示例：  ```javascript const crypto = require(\"crypto\");  const md5 = crypto.createHash(\"md5\"); const cipher = crypto.createCipheriv(   \"aes-256-ecb\",   md5.update(salt).digest(\"hex\"),   \"\"   ); tokenCipher = cipher.update(   JSON.stringify(tokenJson),   \"base64\"   ); tokenCipher += cipher.final(\"base64\"); ```   # noqa: E501

        :return: The token of this CreateCaseDto.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateCaseDto.

        经过加密后的案件数据信息。  ## 加密方案 ---  为了保证数据的安全性，案件数据采用`aes-256-ecb`加密，加密结果使用`base64`编码。  ### 1. 原始的案件详情数据结构  原始的案件详情数据结构请参考：*OriginalCaseDetailDto*  ### 2. 由平台方分配给用户的参数  | 参数名 | 描述 | 给广东太保分配的值 | |:-------|:-----|:-----------------:| | custid | 用户渠道 ID | 21 | | appkey | 用户授权码 | asdfghjkl | | secretkey | 用户安全码 | dwsuhfci | | salt | 加密密钥明文 | gdtb |  ### 3. 签名  签名，用以校验参数是否被篡改。  **计算方法**：  ``` md5(appkey+registno+timestamp+uuid+secretkey).digest(\"hex\") ```  ### 4. 密钥  `aes-256-ecb`加密需要 32bits 的密钥，因此使用`md5(salt).digest(\"hex\")`作为加密密钥。  ### 5. 加密  Node.js 示例：  ```javascript const crypto = require(\"crypto\");  const md5 = crypto.createHash(\"md5\"); const cipher = crypto.createCipheriv(   \"aes-256-ecb\",   md5.update(salt).digest(\"hex\"),   \"\"   ); tokenCipher = cipher.update(   JSON.stringify(tokenJson),   \"base64\"   ); tokenCipher += cipher.final(\"base64\"); ```   # noqa: E501

        :param token: The token of this CreateCaseDto.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token
