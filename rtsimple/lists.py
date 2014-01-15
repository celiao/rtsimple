# -*- coding: utf-8 -*-

"""
rtsimple.lists
~~~~~~~~~~~~~~

This module implements the list functionality for rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

from .base import RT

class Lists(RT):
    BASE_PATH = 'lists'
    URLS = {
        'lists': '',
        'movie_lists': '/movies',
        'movies_box_office': '/movies/box_office',
        'movies_in_theaters': '/movies/in_theaters',
        'movies_opening': '/movies/opening',
        'movies_upcoming': '/movies/upcoming',
        'dvd_lists': '/dvds',
        'dvds_top_rentals': '/dvds/top_rentals',
        'dvds_current_releases': '/dvds/current_releases',
        'dvds_new_releases': '/dvds/new_releases',
        'dvds_upcoming': '/dvds/upcoming',
    }

    def __init__(self):
        super(Lists, self).__init__()

    def lists(self, **kwargs):
        """Gets the top-level lists available from the API.

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('lists')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movie_lists(self, **kwargs):
        """Gets the movie lists available from the API.

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movie_lists')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movies_box_office(self, **kwargs):
        """Gets the top box office earning movies from the API.
           Sorted by most recent weekend gross ticket sales.

        Args:
          limit (optional): limits the number of movies returned, default=10
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movies_box_office')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movies_in_theaters(self, **kwargs):
        """Gets the movies currently in theaters from the API.

        Args:
          page_limit (optional): number of movies to show per page, default=16
          page (optional): selected page of movies, default=1
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movies_in_theaters')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movies_opening(self, **kwargs):
        """Gets the current opening movies from the API.

        Args:
          limit (optional): limits the number of movies returned, default=10
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movies_opening')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movies_upcoming(self, **kwargs):
        """Gets the upcoming movies from the API.

        Args:
          page_limit (optional): number of movies to show per page, default=16
          page (optional): selected page of movies, default=1
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movies_upcoming')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def dvd_lists(self, **kwargs):
        """Gets the dvd lists available from the API.

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('dvd_lists')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def dvds_top_rentals(self, **kwargs):
        """Gets the current opening movies from the API.

        Args:
          limit (optional): limits the number of movies returned, default=10
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('dvds_top_rentals')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def dvds_current_releases(self, **kwargs):
        """Gets the upcoming movies from the API.

        Args:
          page_limit (optional): number of movies to show per page, default=16
          page (optional): selected page of movies, default=1
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('dvds_current_releases')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def dvds_new_releases(self, **kwargs):
        """Gets the upcoming movies from the API.

        Args:
          page_limit (optional): number of movies to show per page, default=16
          page (optional): selected page of movies, default=1
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('dvds_new_releases')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def dvds_upcoming(self, **kwargs):
        """Gets the upcoming movies from the API.

        Args:
          page_limit (optional): number of movies to show per page, default=16
          page (optional): selected page of movies, default=1
          country (optional): localized data for selected country, default="us"

        Returns:
          A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('dvds_upcoming')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response


