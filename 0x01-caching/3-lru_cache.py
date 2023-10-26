#!/usr/bin/env python3
""" 3-lru_cache.py - module for LRUCache class """


from typing import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ inherits from BaseCaching for caching system """
    def __init__(self):
        """ Initialize caching objects """
        self.order = OrderedDict()
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cace """
        if key and item:
            self.order[key] = item
            self.order.move_to_end(key)
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            dkey = list(self.order.keys())[0]
            del self.cache_data[dkey]
            print(f"DISCARD: {dkey}")
            self.order.popitem(last=False)

    def get(self, key):
        """ Get an item from cache by key """
        if key in self.cache_data:
            self.order.move_to_end(key)
        return self.cache_data.get(key)
