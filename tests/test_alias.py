# -*- coding: utf-8 -*-

"""
test_alias.py
~~~~~~~~~~~~~

This test suite checks the methods of the Alias class of rtsimple.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import rtsimple as rt

from . import API_KEY
rt.API_KEY = API_KEY

class TestAlias(unittest.TestCase):
    def test_movie(self):
        id = "0031381"
        title = 'Gone With the Wind'
        alias = rt.Alias()
        alias.movie(type="imdb", id=id)
        self.assertEqual(alias.title, title)
