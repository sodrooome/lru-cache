from lru.lrucache import LRUCache

# example test for LRU Cache
# initialize the object with parameters such as:
test_lru = LRUCache(capacity=3, seconds=15, thread_safe=False)

# set a value that wants to be cached
test_lru.set(1, "Collection Number 1")

# check whether the cache list is empty or not
print(test_lru.is_empty())

# get all cache and returned as dictionary
print(test_lru.get_dict())

# check time-to-left of expired duration of cache
print(test_lru.get_ttl(1))

# check current capacity of cache
print(test_lru.get_capacity())

# remove the cache in list based on their key
print(test_lru.clear_cache_key(1))

# check again whether there's still cache in list or not
print(test_lru.is_empty())