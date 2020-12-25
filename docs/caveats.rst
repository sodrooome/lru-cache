=======
Caveats
=======

Basically, based on the example there’s a several confusion and caveats :

- After the cache duration that we have set exceeds the maximum limit of expired time, will the value of the function be deleted or not? cause the output is not JSON type (probably i’ll given a try to using the jsonify method or make_response).

- Secondly, whether the value it still be stored and appears in a web browser or not, if we stop the flask server.

- Using LRUCache decorators in Django cause a problem in the clickjacking middleware section, we can temporarily set X-FRAME-OPTIONS to DENY in settings.py file inside Django root project if we want to use LRUCache decorators.

Likewise, the use of LRUcache in Django or Flask itself is very limited at this time, because there is a contradiction that is we can’t set the objects dynamically, and another obstacle is that if the object that we set is not in the dict type, we need to do the object hashing