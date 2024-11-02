#!/usr/bin/env python3
"""Pagination module"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """this function accept two int and return a tuple"""
    offset = (page - 1) * page_size
    startindex = offset
    endindex = offset + page_size
    return (startindex, endindex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """the return a range of data"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        with open(Server.DATA_FILE) as f:
            file = csv.reader(f)
            Lfile = list(file)
            (startI, endI) = index_range(page, page_size)
            try:
                return [Lfile[i] for i in range((startI + 1), (endI + 1))]
            except IndexError:
                return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get the hyper media"""
        dic = {}
        with open(Server.DATA_FILE) as f:
            file = csv.reader(f)
            Lfile = list(file)
            total_pages = (len(Lfile) + page_size - 1) // page_size
        dic["page_size"] = page_size
        dic["page"] = page
        data = self.get_page(page, page_size)
        dic["data"] = data
        dic["next_page"] = page + 1 if page < total_pages else None
        dic["prev_page"] = page - 1 if page > 1 else None
        dic["total_pages"] = total_pages
        return dic
