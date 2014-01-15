# -*- coding: utf-8 -*-

"""
test_movies.py
~~~~~~~~~~~~~~

This test suite checks the methods of the Movies class of rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import rtsimple as rt

from . import API_KEY
rt.API_KEY = API_KEY

SEARCH_LINK = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=Bourne&page_limit=30&page=1'

class TestMovies(unittest.TestCase):
    def test_search(self):
        movies = rt.Movies()
        movies.search(q='Bourne')
        self.assertEqual(movies.links['self'], SEARCH_LINK)

    def test_info(self):
        id = 770672122
        title = 'Toy Story 3'
        movie = rt.Movies(id)
        movie.info()
        movie.title
        self.assertEqual(movie.title, title)

    def test_cast(self):
        id = 770672122
        movie = rt.Movies(id)
        movie.cast()
        self.assertTrue(hasattr(movie, 'cast'))
    
    def test_clips(self):
        id = 770672122
        movie = rt.Movies(id)
        movie.clips()
        self.assertTrue(hasattr(movie, 'clips'))
    
    def test_reviews(self):
        id = 770672122
        movie = rt.Movies(id)
        movie.reviews(review_type="top_critic", page_limit=1, page=1)
        self.assertTrue(hasattr(movie, 'reviews'))
    
    def test_similar(self):
        id = 770672122
        movie = rt.Movies(id)
        movie.similar(limit=1)
        self.assertTrue(hasattr(movie, 'movies'))
    

