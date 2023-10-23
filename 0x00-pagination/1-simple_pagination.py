#!/usr/bin/env python3
"""1-simple_pagination.py - module for implementing index_range function"""

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
