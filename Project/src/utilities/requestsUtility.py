import requests
import os
import json
import logging as logger
from Project.src.configs.hosts_config import API_HOSTS
from Project.src.utilities.credentialsUtility import CredentialsUtility
from requests_oauthlib import OAuth1


class RequestsUtility(object):
    """Utility to make API calls.
    - Supports POST, GET, PUT, PATCH & DELETE methods.
    - Supports Json & XML"""

    def __init__(self):
        """Initializes env (environment variable) & base url(host_configs)"""

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def assert_status_code(self):
        """Compares expected_status_code & response status code
        :arg
        expected_status_code : integer
        status_code : integer
        :return
        bool
            Ture or False
        """
        assert self.status_code == self.expected_status_code, \
                                   f"Bad Status code." \
                                   f"Expected {self.expected_status_code}," \
                                   f"Actual status code: {self.status_code}," \
                                   f"URL: {self.url}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """Make a POST api call
        :arg
        endpoint : str
        payload : dict
        headers : dict
        expected_status_code : int
        :return list
            API response body
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers)  # Makes API call
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()  # Fetches API response body
        self.assert_status_code()
        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """Make a GET api call
        :arg
        endpoint : str
        payload : dict
        headers : dict
        expected_status_code : int
        :return list
            API response body
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        self.rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers)  # Makes API call
        self.status_code = self.rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        if self.rs_api.headers['Content-Type'] == 'application/xml':
            self.body = self.rs_api.content
            self.response = self.body.decode()  # Fetches XML response body
        else:
            self.response = self.rs_api.json()  # Fetches json response body
        logger.debug(f"GET API response: {self.response}")

        return self.response

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """Make a PUT api call
        :arg
        endpoint : str
        payload : dict
        headers : dict
        expected_status_code : int
        :return list
            API response body
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers)  # Makes API call
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()  # Fetches response body
        self.assert_status_code()
        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json

    def patch(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """Make a PATCH api call
        :arg
        endpoint : str
        payload : dict
        headers : dict
        expected_status_code : int
        :return list
            API response body
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.patch(url=self.url, data=json.dumps(payload), headers=headers)  # Makes API call
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()  # Fetches response body
        self.assert_status_code()
        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json

    def delete(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """Make a DELETE api call
        :arg
        endpoint : str
        payload : dict
        headers : dict
        expected_status_code : int
        :return list
            API response body
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.delete(url=self.url, data=json.dumps(payload), headers=headers)  # Makes API call
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()  # Fetches response body
        self.assert_status_code()
        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json