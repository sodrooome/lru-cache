================
Further Examples
================

Using with Django
-----------------

You can integrate ``LRUCache`` with Django to cache in-memory data and
return it as JSON responses. First, add ``lru`` to your ``INSTALLED_APPS``
(so that the module is importable):

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'lru',
        ...
    ]

Then wrap your cached data with ``JsonResponse``:

.. code-block:: python

    # views.py

    from django.http import JsonResponse
    from lru.lrucache import LRUCache

    cache = LRUCache(3)

    def test_lru(request):
        cache.set(1, "foo")
        cache.set(2, "bar")
        return JsonResponse(cache.get_dict(), safe=False)

Register the view in your URL configuration:

.. code-block:: python

    # urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.test_lru),
    ]

.. important::

    - ``JsonResponse`` expects a dictionary. Pass ``safe=False`` when your
      top-level data is not a ``dict``.
    - The cache lives in **process memory**, it's not shared between Django
      workers or persisted across server restarts. Each worker process has
      its own independent cache.

Using with Flask
----------------

You can use the ``@lru_cache_time`` decorator with Flask route handlers.
Ensure Flask is installed, then:

.. code-block:: python

    # app.py

    from flask import Flask
    from lru.decorators import lru_cache_time

    app = Flask(__name__)

    @lru_cache_time(seconds=60)
    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

``@lru_cache_time`` wraps the route handler so that the response is cached
for 60 seconds. Subsequent requests within that window return the cached
``"Hello World!"`` without re-executing the handler.

Possible use cases
------------------

There are several use cases that can be done implemented along the way with this package, such as:

- **Web-based streaming services**: cache frequently accessed metadata
- **Object modelling in databases**: track least / most recently accessed
  records (for example; recently played songs, frequently searched books)
- **User activity tracking**: store data for users who frequently visit
  the site
- **Function-level memoization**: avoid repeated expensive computations
  during a request or process lifetime
