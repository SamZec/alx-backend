#!/usr/bin/env python3
""" 2-lifo_cache.py - module for LIFOCache class """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ inherits from BaseCaching for caching system """
    def __init__(self):
        """ Initialize caching objects """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cace """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                dkey = list(self.cache_data.keys())[-2]
                del self.cache_data[dkey]
                print(f"DISCARD: {dkey}")

    def get(self, key):
        """ Get an item from cache by key """
        return self.cache_data.get(key)
