# -*- coding: utf-8 -*-

"""
rtsimple.base
~~~~~~~~~~~~~
This module implements the base class of rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details
"""

import json
import requests

class ApiKeyMissing(Exception):
    pass

class RT(object):
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}
    BASE_PATH = ''
    URLS = {}

    def __init__(self):
        from . import API_VERSION
        self.base_uri= 'http://api.rottentomatoes.com/api/public'
        self.base_uri+= '/v{version}'.format(version=API_VERSION)

    def _get_path(self, key):
        return self.BASE_PATH + self.URLS[key]

    def _get_id_path(self, key):
        return self._get_path(key).format(id=self.id)

    def _get_complete_url(self, path):
        return'{base_uri}/{path}.json'.format(base_uri=self.base_uri, path=path)

    def _get_params(self, params):
        from . import API_KEY
        if not API_KEY:
            raise ApiKeyMissing

        api_dict = {'apikey': API_KEY}
        if params:
            params.update(api_dict)
        else:
            params = api_dict
        return params

    def _request(self, method, path, params=None, payload=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)

        response = requests.request(method, url, 
                                    params=params, 
                                    data=json.dumps(payload) if payload else payload, 
                                    headers=self.headers)

        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def _GET(self, path, params=None):
        return self._request('GET', path, params=params)

    def _set_attrs_to_values(self, response={}):
        """ Set attributes to dictionary values

        >>> import rtsimple as rt
        >>> movie = rt.Movies(770672122)
        >>> response = movie.info()
        >>> movie.title  # instead of response['title']
        'Toy Story 3'
        """
        for key in response.keys():
            setattr(self, key, response[key])
