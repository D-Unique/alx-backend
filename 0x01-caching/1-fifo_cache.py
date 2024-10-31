#!/usr/bin/env python3
""" FIFO cache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ inherit from BaseCaching
        -function - put: implement FIFO
        -function - get: retrive item
    """
    def __init__(self):
        """Intialise the class"""
        super().__init__()
        """call parent class"""

    def put(self, key, item):
        """ Add key- item pair
            remove first item when storage is > maxlimit
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item
            if (len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS):
                # Get the first key
                first_key = next(iter(self.cache_data))
                # Remove the key-value pair
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """retrives item by key"""
        if (self.cache_data.get(key) is None):
            return None
        else:
            return self.cache_data.get(key)
