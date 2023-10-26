#!/usr/bin/env python3
""" 100-lfu_cache.py - module for LFUCache class """


from typing import OrderedDict
from operator import itemgetter


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ inherits from BaseCaching for caching system """
    def __init__(self):
        """ Initialize caching objects """
        self.order = OrderedDict()
        super().__init__()

    def freq(self, key):
        """ count how many times a key is used """
        freq = 0
        if key in self.order:
            freq = self.order.get(key)
            freq += 1
        self.order[key] = freq
        return None

    def put(self, key, item):
        """ Add an item in the cace """
        items = OrderedDict(sorted(self.order.items(), key=itemgetter(1)))
        if key and item:
            self.freq(key)
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            dkey = list(items.keys())[0]
            del self.cache_data[dkey]
            del self.order[dkey]
            print(f"DISCARD: {dkey}")

    def get(self, key):
        """ Get an item from cache by key """
        if key in self.cache_data:
            self.freq(key)
        return self.cache_data.get(key)
