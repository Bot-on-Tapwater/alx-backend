#!/usr/bin/python3
""" MRU Cache """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Implement MRUCache class"""

    recently_used = None

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                del self.cache_data[key]
                self.recently_used = key
                self.cache_data[key] = item

            else:
                if len(self.cache_data) == self.MAX_ITEMS:
                    print(f"DISCARD: {self.recently_used}")
                    self.cache_data.pop(self.recently_used)
                    self.cache_data[key] = item
                    self.recently_used = key
                else:
                    self.cache_data[key] = item
                    self.recently_used = key

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            self.recently_used = key
            return self.cache_data[key]
