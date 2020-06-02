# (c) 2020, Nick Celebic <ncelebic@morpheusdata.com>
# Apache 2 License

from __future__ import (absolute_import, division, print_function)
import os
import warnings
import requests

__metaclass__ = type
DOCUMENTATION = """
  lookup: cypher
  author: Nick Celebic <ncelebic@morpheusdata.com>
  version_added: "0.1.0"
  short_description: retrieve secrets from Morpheus Cypher Secret Storage
  requirements:
    - requests (python library)
  description:
    - retrieve secrets from Morpheus Cypher Secret Storage
  options:
    secret:
      description: query you are making.
      required: False
    token:
      description:
          - The Execution Lease Token used for validating temporary execution access via the morpheus command bus
      type: string
      vars:
          - name: morpheus_token
    url:
      description:
          - The Morpheus Appliance URL where the api calls need to be made
      type: string
      vars:
          - name: morpheus_url
"""
RETURN = """
_raw:
  description:
    - secrets(s) requested
"""


class Cypher:
    def __init__(self, url=None, token=None):
        if url is None:
            self.url = os.environ.get("morpheus_url", None)
        else:
            self.url = url
        if url is None:
            raise Exception("morpheus_url not specified in ENV")

        if token is None:
            self.token = os.environ.get("morpheus_token", None)
        else:
            self.token = token
        if token is None:
            raise Exception("morpheus_token not specified in ENV")

    @staticmethod
    def _get_item(response, path):
        for item in path:
            if item.isdigit():
                item = int(item)
            response = response[item]
        return response

    def get(self, secret_input):
        s_f = secret_input.split(':', 1)
        secret = s_f[0]
        if len(s_f) >= 2:
            if ':' in s_f[1]:
                secret_path = s_f[1].split(':')
            else:
                secret_path = [s_f[1]]
        else:
            secret_path = ''
        appliance_url = self.url
        url = appliance_url + '/api/cypher/v1/' + secret
        headers = {'content-type': 'application/json', 'X-Cypher-Token': self.token}
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=Warning)
            r = requests.get(url=url, headers=headers, verify=False)
        data = r.json()
        if data is None:
            raise Exception("The secret %s doesn't seem to exist for cypher lookup" % secret)
        if not data['success']:
            raise Exception("The secret %s doesn't seem to exist for cypher lookup" % secret)
        if secret_path == '':
            return data['data']
        try:
            return self._get_item(data['data'], secret_path)
        except:
            raise Exception("The secret %s does not contain the path '%s'. for cypher lookup" %
                            (secret, ":".join(secret_path)))
