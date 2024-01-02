#!/usr/bin/env python3
"""Create class FIFOCache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implement BasicCache class"""

    def __init__(self):
        """Constructor method"""
        super().__init__()

    def put(self, key, item):
        """append key item pair to dict"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            value = self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """return value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
