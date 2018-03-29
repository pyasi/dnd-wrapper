import json
import requests


class DnDBase(object):

    def __init__(self):
        self.base_uri = 'http://dnd5eapi.co/api/'
        self.headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Connection': 'close'}

    def _query(self, method, path, params=None, payload=None):
        url = self.base_uri + path

        response = requests.request(
            method, url, params=params,
            data=json.dumps(payload) if payload else payload,
            headers=self.headers)

        response.raise_for_status()
        return response.json()

    def _get(self, path):
        return self._query('GET', path)

    def _set_response_info_to_class_values(self, response={}):
        """

        """
        if isinstance(response, dict):
            for key in response.keys():
                if not hasattr(self, key) or not callable(getattr(self, key)):
                    setattr(self, key, response[key])
