from lru.decorators import lru_cache_time

# decorators for caching an object
# based on function
@lru_cache_time(capacity=3, seconds=15)
def lru_with_decorators(x):
    print("Calling {0}".format(x))
    return x

# set the "x" object that wants to
# be cached
lru_with_decorators.set(1, "foo")
lru_with_decorators.set(2, "test")
lru_with_decorators.set(3, "foos")
lru_with_decorators.set(4, "fc")
lru_with_decorators.set(5, "set")

# get capacity of cache
print(lru_with_decorators.get_capacity())

# get all cache list and returned as dict type
print(lru_with_decorators.get_dict())

# remove all cache list
print(lru_with_decorators.clear_all())