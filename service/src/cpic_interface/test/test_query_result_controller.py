# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from cpic_interface.models.query_case_dto import QueryCaseDto  # noqa: E501
from cpic_interface.models.query_case_res_dto import QueryCaseResDto  # noqa: E501
from cpic_interface.test import BaseTestCase


class TestQueryResultController(BaseTestCase):
    """QueryResultController integration test stubs"""

    def test_query_case(self):
        """Test case for query_case

        查询任务状态，及识别结果
        """
        query_case_dto = {
  "custid" : "custid",
  "uuid" : "uuid",
  "token" : "token"
}
        headers = { 
        }
        response = self.client.open(
            '/v1/queryCase',
            method='POST',
            headers=headers,
            data=json.dumps(query_case_dto),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
