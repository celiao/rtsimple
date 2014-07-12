# -*- coding: utf-8 -*-

# See http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'rtsimple',
    version = '0.9.0',
    author = 'Celia Oakley',
    author_email = 'celia.oakley@alumni.stanford.edu',
    description = 'A Python wrapper for the Rotten Tomatoes API v1.0',
    keywords = ['movie', 'movies', 'rotten tomatoes', 'rotten', 
                'tomatoes', 'rt', 'wrapper', 'database', 'api'],
    url = 'https://github.com/celiao/rtsimple',
    download_url = 'https://github.com/celiao/rtsimple/tarball/0.9.0',
    packages = ['rtsimple'],
    long_description=read('README.rst'),
    install_requires = ['requests>=2.3.0'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Utilities",
    ],
)
