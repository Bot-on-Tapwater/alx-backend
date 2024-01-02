#!/usr/bin/python3
""" LRU Cache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines an LRUCache class """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            # Check if key is already in cache
            if key in self.cache_data:
                # Move the key to the most recently used position
                del self.cache_data[key]

            # Add new key-value pair
            self.cache_data[key] = item

            # Check if cache exceeds maximum capacity
            if len(self.cache_data) > self.MAX_ITEMS:
                # Remove the least recently used item (first item in dict)
                lru_key = list(self.cache_data.keys())[0]
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Move the key to the most recently used position
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
