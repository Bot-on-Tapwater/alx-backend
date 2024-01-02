#!/usr/bin/env python3
"""Create class LIFOCache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implement LIFOCache class"""

    recent_updated_key = None

    def __init__(self):
        """Constructor method"""
        super().__init__()

    def put(self, key, item):
        """append key item pair to dict"""
        if key is None or item is None:
            pass
        else:
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                if self.recent_updated_key is not None:
                    self.cache_data.pop(self.recent_updated_key)
                    print(f"DISCARD: {self.recent_updated_key}")
                    self.cache_data[key] = item
                    self.recent_updated_key = key
                else:
                    pop_key, pop_value = self.cache_data.popitem()
                    print(f"DISCARD: {pop_key}")
                    self.cache_data[key] = item
                    self.recent_updated_key = key

            else:
                self.cache_data[key] = item
                self.recent_updated_key = key

    def get(self, key):
        """return value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
