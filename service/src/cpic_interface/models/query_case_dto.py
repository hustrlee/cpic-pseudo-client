# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cpic_interface.models.base_model_ import Model
from cpic_interface import util


class QueryCaseDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, custid=None, uuid=None, token=None):  # noqa: E501
        """QueryCaseDto - a model defined in OpenAPI

        :param custid: The custid of this QueryCaseDto.  # noqa: E501
        :type custid: str
        :param uuid: The uuid of this QueryCaseDto.  # noqa: E501
        :type uuid: str
        :param token: The token of this QueryCaseDto.  # noqa: E501
        :type token: str
        """
        self.openapi_types = {
            'custid': str,
            'uuid': str,
            'token': str
        }

        self.attribute_map = {
            'custid': 'custid',
            'uuid': 'uuid',
            'token': 'token'
        }

        self._custid = custid
        self._uuid = uuid
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'QueryCaseDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryCaseDto of this QueryCaseDto.  # noqa: E501
        :rtype: QueryCaseDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def custid(self):
        """Gets the custid of this QueryCaseDto.

        客户渠道 ID  # noqa: E501

        :return: The custid of this QueryCaseDto.
        :rtype: str
        """
        return self._custid

    @custid.setter
    def custid(self, custid):
        """Sets the custid of this QueryCaseDto.

        客户渠道 ID  # noqa: E501

        :param custid: The custid of this QueryCaseDto.
        :type custid: str
        """

        self._custid = custid

    @property
    def uuid(self):
        """Gets the uuid of this QueryCaseDto.

        标识案件的唯一标识，用于客户确认结果。由客户端保证唯一性。  # noqa: E501

        :return: The uuid of this QueryCaseDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this QueryCaseDto.

        标识案件的唯一标识，用于客户确认结果。由客户端保证唯一性。  # noqa: E501

        :param uuid: The uuid of this QueryCaseDto.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def token(self):
        """Gets the token of this QueryCaseDto.

        加密后的查询验证条件。  ## 加密方案 ---  验证数据采用`aes-256-ecb`加密，加密结果使用`base64`编码。  ### 1. 验证数据的原始数据结构  | 字段名 | 描述    | |-------|--------| | appkey | 用户授权码  | | caseNo | 任务序号，在提交任务时，由服务端返回，全局唯一  | | registNo | 报案号  | | sign | 参数签名，用以校验传入参数  | | timestamp | 接口调用时间戳  |  ### 2. 由平台方分配给用户的参数  | 参数名 | 描述 | 给广东太保分配的值 | |:-------|:-----|:-----------------:| | custid | 用户渠道 ID | 21 | | appkey | 用户授权码 | asdfghjkl | | secretkey | 用户安全码 | dwsuhfci | | salt | 加密密钥明文 | gdtb |  ### 3. 签名  签名，用以校验参数是否被篡改。  **计算方法**：  ``` md5(appkey+caseNo+timestamp+uuid+secretkey).digest(\"hex\") ```  ### 4. 密钥  `aes-256-ecb`加密需要 32bits 的密钥，因此使用`md5(salt).digest(\"hex\")`作为加密密钥。  ### 5. 加密  Node.js 示例：  ```javascript const crypto = require(\"crypto\");  const md5 = crypto.createHash(\"md5\"); const cipher = crypto.createCipheriv(   \"aes-256-ecb\",   md5.update(salt).digest(\"hex\"),   \"\"   ); tokenCipher = cipher.update(   JSON.stringify(tokenJson),   \"base64\"   ); tokenCipher += cipher.final(\"base64\"); ```   # noqa: E501

        :return: The token of this QueryCaseDto.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this QueryCaseDto.

        加密后的查询验证条件。  ## 加密方案 ---  验证数据采用`aes-256-ecb`加密，加密结果使用`base64`编码。  ### 1. 验证数据的原始数据结构  | 字段名 | 描述    | |-------|--------| | appkey | 用户授权码  | | caseNo | 任务序号，在提交任务时，由服务端返回，全局唯一  | | registNo | 报案号  | | sign | 参数签名，用以校验传入参数  | | timestamp | 接口调用时间戳  |  ### 2. 由平台方分配给用户的参数  | 参数名 | 描述 | 给广东太保分配的值 | |:-------|:-----|:-----------------:| | custid | 用户渠道 ID | 21 | | appkey | 用户授权码 | asdfghjkl | | secretkey | 用户安全码 | dwsuhfci | | salt | 加密密钥明文 | gdtb |  ### 3. 签名  签名，用以校验参数是否被篡改。  **计算方法**：  ``` md5(appkey+caseNo+timestamp+uuid+secretkey).digest(\"hex\") ```  ### 4. 密钥  `aes-256-ecb`加密需要 32bits 的密钥，因此使用`md5(salt).digest(\"hex\")`作为加密密钥。  ### 5. 加密  Node.js 示例：  ```javascript const crypto = require(\"crypto\");  const md5 = crypto.createHash(\"md5\"); const cipher = crypto.createCipheriv(   \"aes-256-ecb\",   md5.update(salt).digest(\"hex\"),   \"\"   ); tokenCipher = cipher.update(   JSON.stringify(tokenJson),   \"base64\"   ); tokenCipher += cipher.final(\"base64\"); ```   # noqa: E501

        :param token: The token of this QueryCaseDto.
        :type token: str
        """

        self._token = token
