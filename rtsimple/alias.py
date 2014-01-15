# -*- coding: utf-8 -*-

"""
rtsimple.alias
~~~~~~~~~~~~~~

This module implements the alias functionality for rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

from .base import RT

class Alias(RT):
    BASE_PATH = 'movie_alias'
    URLS = {
        'movie': '',
    }

    def __init__(self):
        super(Alias, self).__init__()

    def movie(self, **kwargs):
        """Get movie info base on id from different vendor from the API.

        Args:
          type (optional): alias type to look up, only supports "imdb"
          id (optional): id to look up 

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movie')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
