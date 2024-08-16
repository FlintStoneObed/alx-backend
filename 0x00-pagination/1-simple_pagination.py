#!/usr/bin/env python3
"""
This module provides a Server class to paginate a dataset of popular baby names
and includes a function to calculate pagination indexes.
"""

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

class Server:
    """Server class to paginate a database of popular baby names.
    
    The class reads data from a CSV file and provides functionality
    to retrieve pages of the data.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        
        Loads the dataset from the CSV file and caches it.
        
        Returns:
            List[List]: The dataset, where each item is a list of row data.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.
        
        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.
        
        Returns:
            List[List]: A list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
