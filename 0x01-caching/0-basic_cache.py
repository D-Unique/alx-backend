#!/usr/bin/env python3
"""The BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        """call the parent class"""

    def put(self, key, item):
        """this function adds item to the dict - cache_data
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """this function retrives item from the dict - cache_data
            using its key
        """
        rkey = self.cache_data.get(key)
        if (rkey is None):
            return None
        else:
            return rkey
