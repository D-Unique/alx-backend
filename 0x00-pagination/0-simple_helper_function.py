#!/usr/bin/env python3
"""Pagination module"""


def index_range(page: int, page_size: int) -> tuple:
    """this function accept two int and return a tuple"""
    offset = (page - 1) * page_size
    startindex = offset
    endindex = offset + page_size
    return (startindex, endindex)
