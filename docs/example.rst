================
Further Examples
================

Backported with Django
----------------------

For further example, hopefully this package can be backported with Python web frameworks such as Django or Flask which can be implemented and supported in the JSON field area, since the return of this LRUCache value is in the form of dictionary which is very common in JSON type. For simple usage in Django, you must setting the LRUCache in installed application within Django settings like this :

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'lru',
        ...
    ]


And then you can create some function for wrapped the objects that you want to cached with `JsonResponse` from Django API. The results of this function will return your objects in the form of a JSON dict at your web browser :

.. code-block:: python

    # views.py

    from django.http import JsonResponse
    from lru.lrucache import LRUCache

    # set the capacity of LRUCache
    test = LRUCache(3)

    # wrapped our object
    def test_lru(request):
        test.set(1, "foo")
        test.set(2, "bar")
        return JsonResponse(test.get_dict(), safe=False)


Dont forget to passing our function method into Django urls parameters :

.. code-block:: python

    # urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.test_lru),
    ]


After that you can run the django server and see it in a web browser based on your endpoint url. **Please remember**, at the moment, each time after you wrapped the object with `JsonResponse`, you need to set the `safe` parameter to `False` because when you set an object with LRUCache, we don't set it to dict type, while the output from `JsonResponse` itself is dict type.

Backported with Flask
---------------------

For simple usage in Flask probably occured by using the LRUCache decorators on top of the router flask decorator. Ensure you've already installed Flask with `pip install flask` and then create new file such as the following example :

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


After that, you can run the Flask app with the command like `python app.py` and then open it in the browser according to the existing localhost. **As for noted**, the use of the `@lru_cache_time` decorators itself will set the cache capacity and duration of the cache. Since here we only return plain text / html with *Hello World* output, i'm assume we don't need to set the cache capacity. 
Normally, using LRUCache at the web-environment level can be done with the following assumptions like :

- You want to build web-based streaming services
- You do object modeling in the database, such as creating objects for a song that is least or most recently heard.
- You set the song object with LRUCache, so that every time you open your site, that song will appear.

Another example of using this LRU cache is that you want to display a book that is most often searched by keywords, dynamically remove an object that is not or least used, store data of users who frequently visit our site and many others.