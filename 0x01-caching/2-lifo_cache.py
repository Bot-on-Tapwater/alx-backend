#!/usr/bin/env python3
"""Create class LIFOCache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implement BasicCache class"""

    def __init__(self):
        """Constructor method"""
        super().__init__()

    def put(self, key, item):
        """append key item pair to dict"""
        if key is None or item is None:
            pass
        elif(len(self.cache_data) == BaseCaching.MAX_ITEMS):
            pop_key, pop_value = self.cache_data.popitem()
            print(f"DISCARD: {pop_key}")
            self.cache_data[key] = item
            return
        else:
            self.cache_data[key] = item
            

    def get(self, key):
        """return value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
