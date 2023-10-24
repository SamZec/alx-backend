#!/usr/bin/env python3
""" 3-lru_cache.py - module for LRUCache class """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ inherits from BaseCaching for caching system """
    def __init__(self):
        """ Initialize caching objects """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cace """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data.keys():
                    del self.cache_data[key]
                    self.cache_data[key] = item
                else:
                    dkey = list(self.cache_data.keys())[0]
                    del self.cache_data[dkey]
                    print(f"DISCARD: {dkey}")
                    self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item from cache by key """
        return self.cache_data.get(key)
