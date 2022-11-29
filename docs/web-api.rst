======================
YouTubeMusicAPI 2.7.1
======================

The search API for `YouTube Music <https://music.youtube.com/>`_.

Get Started:
============

Prerequisites:
______________
- Python 3.6+

Installation:
_____________

- First, please make sure that the latest pip version is installed in your working environment.

.. code-block::
    
    python -m pip install -U pip

- Then you can install ``YouTubeMusicAPI`` using a simple ``pip install`` command.

.. code-block::

    python -m pip install -U YouTubeMusicAPI

Example:
===============

.. code-block:: python

    import YouTubeMusicAPI
    
    result = YouTubeMusicAPI.Search("shape of you")
    
    print(result)

output:
_______

.. code-block:: json

    {
        "name": "Ed Sheeran - Shape of You (Official Music Video)",
        "id": "JGwWNGJdvx8",
        "url": "https://music.youtube.com/watch?v=JGwWNGJdvx8",
        "images": [
            "https://i.ytimg.com/vi/JGwWNGJdvx8/hqdefault.jpg",
            "https://i.ytimg.com/vi/JGwWNGJdvx8/default.jpg",
            "https://i.ytimg.com/vi/JGwWNGJdvx8/mqdefault.jpg",
            "https://i.ytimg.com/vi/JGwWNGJdvx8/sddefault.jpg",
            "https://i.ytimg.com/vi/JGwWNGJdvx8/maxresdefault.jpg"
        ],
        "author_name": "Ed Sheeran",
        "author_url": "https://www.youtube.com/c/EdSheeran"
    }
