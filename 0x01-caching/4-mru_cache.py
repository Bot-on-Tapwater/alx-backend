#!/usr/bin/python3
""" MRU Cache """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
   def __init__(self):
       super().__init__()
       self.cache_data = OrderedDict()

   def put(self, key, item):
       if key is None or item is None:
           return
       self.cache_data[key] = item
       if len(self.cache_data) > BaseCaching.MAX_ITEMS:
           discarded_key = next(iter(self.cache_data))
           print(f"DISCARD: {discarded_key}")
           del self.cache_data[discarded_key]


   def get(self, key):
       if key is None or key not in self.cache_data:
           return None
       return self.cache_data[key]
