#!/usr/bin/env python3
""" 0-basic_cache.py - module for BasicCache class """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching for caching system"""
    def __init__(self):
        """ initialize cache system """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key """
        return self.cache_data.get(key)
