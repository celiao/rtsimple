# -*- coding: utf-8 -*-

"""
test_lists.py
~~~~~~~~~~~~~

This test suite checks the methods of the Lists class of rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import rtsimple as rt

from tests import API_KEY
rt.API_KEY = API_KEY

LISTS_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies.json'
MOVIES_BOX_OFFICE_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?limit=2&country=us'
MOVIES_IN_THEATERS_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=3&country=us&page=1'
MOVIES_OPENING_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json?limit=4&country=us'
MOVIES_UPCOMING_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?page_limit=5&country=us&page=1'

DVD_TOP_RENTALS_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?limit=2&country=us'
DVD_CURRENT_RELEASES_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/current_releases.json?page_limit=3&country=us&page=1'
DVD_NEW_RELEASES_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/new_releases.json?page_limit=4&country=us&page=1'
DVD_UPCOMING_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/upcoming.json?page_limit=5&country=us&page=1'

class TestLists(unittest.TestCase):
    def test_lists(self):
        list = rt.Lists()
        list.lists()
        self.assertEqual(list.links['movies'], LISTS_LINK)

    def test_movie_lists(self):
        list = rt.Lists()
        list.movie_lists()
        self.assertTrue('box_office' in list.links)
        self.assertTrue('in_theaters' in list.links)
        self.assertTrue('opening' in list.links)
        self.assertTrue('upcoming' in list.links)

    def test_movies_box_office(self):
        list = rt.Lists()
        list.movies_box_office(limit=2)
        self.assertEqual(list.links['self'], MOVIES_BOX_OFFICE_LINK)
        
    def test_movies_in_theaters(self):
        list = rt.Lists()
        list.movies_in_theaters(page_limit=3)
        self.assertEqual(list.links['self'], MOVIES_IN_THEATERS_LINK)

    def test_movies_opening(self):
        list = rt.Lists()
        list.movies_opening(limit=4)
        self.assertEqual(list.links['self'], MOVIES_OPENING_LINK)

    def test_movies_upcoming(self):
        list = rt.Lists()
        list.movies_upcoming(page_limit=5)
        self.assertEqual(list.links['self'], MOVIES_UPCOMING_LINK)

    def test_dvd_lists(self):
        list = rt.Lists()
        list.dvd_lists()
        self.assertTrue('top_rentals' in list.links)
        self.assertTrue('current_releases' in list.links)
        self.assertTrue('new_releases' in list.links)
        self.assertTrue('upcoming' in list.links)

    def test_dvds_top_rentals(self):
        list = rt.Lists()
        list.dvds_top_rentals(limit=2)
        self.assertEqual(list.links['self'], DVD_TOP_RENTALS_LINK)
        
    def test_dvds_current_releases(self):
        list = rt.Lists()
        list.dvds_current_releases(page_limit=3)
        self.assertEqual(list.links['self'], DVD_CURRENT_RELEASES_LINK)
        
    def test_dvds_new_releases(self):
        list = rt.Lists()
        list.dvds_new_releases(page_limit=4)
        self.assertEqual(list.links['self'], DVD_NEW_RELEASES_LINK)
        
    def test_dvds_upcoming(self):
        list = rt.Lists()
        list.dvds_upcoming(page_limit=5)
        self.assertEqual(list.links['self'], DVD_UPCOMING_LINK)
        
