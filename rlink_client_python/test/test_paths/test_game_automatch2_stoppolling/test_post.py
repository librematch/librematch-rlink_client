# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import rlink_client
from rlink_client.paths.game_automatch2_stoppolling import post  # noqa: E501
from rlink_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestGameAutomatch2Stoppolling(ApiTestMixin, unittest.TestCase):
    """
    GameAutomatch2Stoppolling unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
