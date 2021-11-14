# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from cpic_interface.models.create_case_dto import CreateCaseDto  # noqa: E501
from cpic_interface.models.create_case_res_dto import CreateCaseResDto  # noqa: E501
from cpic_interface.test import BaseTestCase


class TestSubmitTaskController(BaseTestCase):
    """SubmitTaskController integration test stubs"""

    def test_create_case(self):
        """Test case for create_case

        用于接收渠道推送的案件信息
        """
        create_case_dto = {
  "withCaseInfoInReturn" : true,
  "custid" : "custid",
  "uuid" : "uuid",
  "token" : "token"
}
        headers = { 
        }
        response = self.client.open(
            '/createCase',
            method='POST',
            headers=headers,
            data=json.dumps(create_case_dto),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
