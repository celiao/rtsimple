# -*- coding: utf-8 -*-

"""
rtsimple.movies
~~~~~~~~~~~~~~~

This module implements the movie functionality for rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

from .base import RT

class Movies(RT):
    BASE_PATH = 'movies'
    URLS = {
        'search': '',
        'info': '/{id}',
        'cast': '/{id}/cast',
        'clips': '/{id}/clips',
        'reviews': '/{id}/reviews',
        'similar': '/{id}/similar',
    }

    def __init__(self, id=0):
        super(Movies, self).__init__()
        self.id = id

    def search(self, **kwargs):
        """Get movies that match the search query string from the API.

        Args:
          q (optional): plain text search query; remember to URI encode
          page_limit (optional): number of search results to show per page, 
                                 default=30
          page (optional): selected page of search results, default=1

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('search')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
        
    def info(self, **kwargs):
        """Get detailed info on a movie specified by id from the API.

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_id_path('info')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
        
    def cast(self, **kwargs):
        """Get the cast for a movie specified by id from the API.

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_id_path('cast')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
        
    def clips(self, **kwargs):
        """Get related clips and trailers for a movie specified by id 
           from the API.

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_id_path('clips')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, **kwargs):
        """Get reviews for a movie specified by id from the API.

        Args:
          review_type (optional): "all", "top_critic", or "dvd",  
                                  default="top_critic"
          page_limit (optional): number of reviews to show per page, default=30
          page (optional): selected page of reviews, default=1
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_id_path('reviews')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def similar(self, **kwargs):
        """Get reviews for a movie specified by id from the API.

        Args:
          limit (optional): number of similar moview to show, default=5

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_id_path('similar')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

