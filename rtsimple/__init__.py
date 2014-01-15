# -*- coding: utf-8 -*-

"""
rtsimple
~~~~~~~~

*rtsimple* is a wrapper, written in Python, for The Rotten Tomatoes (RT) API.  By calling the functions available in *rtsimple* you can simplify your code and easily access a vast amount of movie data, including detailed movie information, new release and dvd lists, critic and audience scores, and published reviews.  To find out more about The Rotten Tomatoes API, check out the welcome page http://developer.rottentomatoes.com/ and overview page http://developer.rottentomatoes.com/docs.

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details
"""

__title__ = 'rtsimple'
__version__ = '0.1.0'
__author__ = 'Celia Oakley'
__copyright__ = 'Copyright (c) 2013-1014 Celia Oakley'
__license__ = 'GPLv3'

import os

from .lists import Lists
from .movies import Movies
from .alias import Alias

def _get_env_key(key):
    try:
        return os.environ[key]
    except KeyError:
        return None

API_KEY = _get_env_key('RT_API_KEY')
API_VERSION = '1.0'

