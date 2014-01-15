""" Either place your API_KEY in the following constant:
"""
API_KEY = ''

""" or include it in a keys.py file.
"""
try:
    from .keys import *
except ImportError:
    pass
