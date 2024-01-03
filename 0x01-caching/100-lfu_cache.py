#!/usr/bin/python3
""" 100-lfu_cache """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
   def __init__(self):
       super().__init__()
       self.freq_list = LinkedList()

   def put(self, key, item):
       if key is None or item is None:
           return
       if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
           self.discard_item()
       self.cache_data[key] = item

   def get(self, key):
       if key is None or key not in self.cache_data:
           return None
       else:
           return self.cache_data[key]

   def discard_item(self):
       min_freq_node = self.freq_list.head
       min_freq_item = min_freq_node.data_list.head
       self.freq_list.head.data_list.remove(min_freq_item)
       del self.cache_data[min_freq_item.data_key]
       if not self.freq_list.head.data_list:
           self.freq_list.remove(self.freq_list.head)
       print("DISCARD: " + str(min_freq_item.data_key))
