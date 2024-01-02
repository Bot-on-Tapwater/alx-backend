#!/usr/bin/env python3
"""Create class BasicCache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
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

    def get(self, key):
        """return value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
