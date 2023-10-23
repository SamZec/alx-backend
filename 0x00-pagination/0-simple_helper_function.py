#!/usr/bin/env python3
"""0-simple_helper_function.py - module for index_range function"""

from typing import Tuple


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
