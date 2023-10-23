#!/usr/bin/env python3
"""
    2-hypermedia_pagination.py - module for implementing hypermedia pagination
"""

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        function for returning range of indexes for a particular pagination
        parameters

        args:
            page - page number
            page_size - size of page
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


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
        """gets a page base on the args: page and page_size"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        index = index_range(page, page_size)
        data = self.dataset()

        return data[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Hypermedia pagination"""
        data = self.get_page(page, page_size)
        size = len(data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None
        if page + 1 <= total_pages:
            next_page = page + 1
        prev_page = None
        if page > 1:
            prev_page = page - 1
        hypermedia = {
                'page_size': size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return hypermedia
