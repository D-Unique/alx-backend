#!/usr/bin/env python3
"""The LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ This class inherit from BaseCaching"""
    def __init__(self):
        """initialize the class"""
        super().__init__()
        """call the parent class"""
    def put(self, key, item):
        """implement LIFO"""
        if (key is None or item is None):
            pass
        else:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                last_key, last_value = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrives the value of the key"""
        if (key is None or key not in self.cache_data.keys):
            return None

        return self.cache_data.get(key)
