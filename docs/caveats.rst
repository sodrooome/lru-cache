=======
Caveats
=======

Basically, based on the example there’s a several confusion and caveats :

- After the cache duration that we have set exceeds the maximum limit of expired time, will the value of the function be deleted or not? cause the output is not JSON type (probably i’ll given a try to using the jsonify method or make_response).

- Secondly, whether the value it still be stored and appears in a web browser or not, if we stop the flask server.

- Using LRUCache decorators in Django cause a problem in the clickjacking middleware section, we can temporarily set X-FRAME-OPTIONS to DENY in settings.py file inside Django root project if we want to use LRUCache decorators.

Likewise, the use of LRUcache in Django or Flask itself is very limited at this time, because there is a contradiction that is we can’t set the objects dynamically, and another obstacle is that if the object that we set is not in the dict type, we need to do the object hashing

Particularly, this package is **not recommended** to serve as primary caching at the web environment level, as for noted, it is highly recommended to use the locmemcache provided by django or to use the redis instance. There are some writings that say that caching should not be done in Python (i also don't really know if this is true or not) because using cache with this package itself doesn't really reduce efficiency in memory.


Why it matters to use this?
===========================

This **LRUcache** package is suitable for storing a small amount of data and then returning the data in the relevant amount. Besides that, you can also use this package at the development level (not in production) to be able to find out and measure how much the performance of the web is made of (you can do this by using django-debug-toolbar), as when we use it at the development level we don't need to run a worker or some sort of web server process

In addition to that, it might **suitable** for real-world case use in the right contexts and appropriate manners such as :

- Internal tools
- Development environments
- Function level optimization (for instance, memoize repeated computations like whenever fetch or streaming API request)
