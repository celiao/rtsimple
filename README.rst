rtsimple
========

A wrapper for the Rotten Tomatoes API
--------------------------------------

*rtsimple* is a wrapper, written in Python, for the Rotten Tomatoes (RT) API.  By calling the methods available in *rtsimple* you can simplify your code and easily access a vast amount of movie data, including detailed movie information, lists of new released movies and dvds, critic and audience scores, and published reviews.  To find out more about the Rotten Tomatoes API, check out the Welcome page http://developer.rottentomatoes.com and Overview page http://developer.rottentomatoes.com/docs.

Features
--------

- Supports and tested under Python 2.7.2 and 3.3.2
- One-to-one mapping between *rtsimple* and RT methods.
- Implements all RT methods.
- Easy to access data using Python class attributes.
- Easy to experiment with *rtsimple* methods inside the Python interpreter.
- Code tested with unittests, which illustrate the method call syntax.

Installation
------------

*rtsimple* is available on the Python Package Index (PyPI) at https://pypi.python.org/pypi/rtsimple.

You can install *rtsimple* using one of the following techniques.

- Use pip:

::

    pip install rtsimple

- Download the .zip or .tar.gz file from PyPI and install it yourself
- Download the `source from Github`_ and install it yourself

If you install it yourself, also install requests_.

.. _source from Github: http://github.com/celiao/rtsimple
.. _requests: http://www.python-requests.org/en/latest/

API Key
-------
You will need an API key to Rotten Tomatoes to access the API.  To obtain a key, follow these steps:

1) Register for and verify an account_.
2) `Log into`_ your account.
3) Once you are logged in, click on the link to *Apply for an API key* and follow the instructions.

.. _account: http://developer.rottentomatoes.com/member/register
.. _Log into: https://secure.mashery.com/login/developer.rottentomatoes.com/

Examples
--------
With the *rtsimple* package installed and an RT API key, you can start to play with the data.

First, import the package and assign your API_KEY.

.. code-block:: python

    >>> import rtsimple as rt
    >>> rt.API_KEY = 'YOUR API KEY HERE'

To communicate with the Rotten Tomatoes (RT) API, create an instance of one of the object types, call one of the methods on the instance, and access instance attributes.  Use keys to access attribute values that are dictionaries.  In this example, we search for movies with *Hunger Games* in the title, and determine the Rotten Tomatoes id of the second installment in the series, Catching Fire.

.. code-block:: python

    >>> movie = rt.Movies()
    >>> response = movie.search(q="Hunger Games")
    >>> len(movie.movies)
    4
    >>> for m in movie.movies:
    ...     print(m['title'])
    ...
    The Hunger Games
    The Hunger Games: Catching Fire
    The Hunger Games: Mockingjay - Part 1
    The Hunger Games: Mockingjay - Part 2
    >>> movie.movies[1]['id']
    '771250004'

Once we have the RT id, we can create a movie instance to represent that movie specifically and examine its attributes.

.. code-block:: python

    >>> movie = rt.Movies('771250004')
    >>> response = movie.info()
    >>> movie.title
    'The Hunger Games: Catching Fire'
    >>> movie.mpaa_rating
    'PG-13'
    >>> movie.genres
    ['Action & Adventure', 'Science Fiction & Fantasy']
    >>> movie.runtime
    146
    >>> movie.ratings['critics_score']
    89
    >>> movie.ratings['audience_score']
    92

For fun, get ratings for the other *Hunger Games* movies and determine which of the movies is considered by critics to be the best in the series.

Call other instance methods to gather additional information.  In this example, we find movies that are considered similar to *The Hunger Games: Catching Fire*.  On the list are the original movie, which isn't too surprising, and one of the Harry Potter movies, which is a surprise.

.. code-block:: python

    >>> response = movie.similar()
    >>> len(movie.movies)
    2
    >>> for m in movie.movies:
    ...     print(m['title'])
    ...
    The Hunger Games
    Harry Potter and the Deathly Hallows - Part 1

In addition to extracting detailed information about specific movies, you can get movie and DVD lists from the Rotten Tomatoes API.  Suppose you are curious whether the *Movies In Theaters* list has any movies in common with the *DVDs Upcoming* list.  Note that the RT API lists are updated on a regular basis, so your results may vary from those below.

.. code-block:: python

    >>> lst = rt.Lists()
    >>> response = lst.movies_in_theaters()
    >>> lst.total
    127
    >>> for m in lst.movies[:5]:
    ...     print(m['title'])
    ...
    The Legend of Hercules
    The Hobbit: The Desolation Of Smaug
    Frozen
    Lone Survivor
    Anchorman 2: The Legend Continues
    >>> response = lst.dvds_upcoming()
    >>> lst.total
    72
    >>> for m in lst.movies[:5]:
    ...     print(m['title'])
    ...
    Riddick
    Carrie
    Lee Daniels' The Butler
    Enough Said
    You're Next

For the first 5 entries, there doesn't appear to be any overlap.  For fun, create complete lists of the *Movies In Theaters* list and *DVDs Upcoming* list and determine if the lists overlap at all.

Note that you can call methods and get details without explicitly instanciating an object.

.. code-block:: python

    >>> response = rt.Movies(771250004).info()
    >>> response['alternate_ids']
    {'imdb': '1951264'}

.. If you like this wrapper, and would like access to even more movie and TV data, check out *tmdbsimple* <https://pypi.python.org/pypi/tmdbsimple>, a wrapper for The Movie Database API v3, developed by the same author.
