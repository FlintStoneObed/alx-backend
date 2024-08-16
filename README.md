0x00-PAGINATION

OVERVIEW

This project focuses on implementing pagination techniques to handle and manage large datasets effectively. Pagination allows for dividing a dataset into manageable chunks or pages, making it easier to navigate and retrieve specific subsets of data. The project emphasizes various pagination methods, including deletion-resilient pagination, ensuring that users can access data consistently even if the dataset changes between queries.

PROJECT STRUCTURE

FILES

0-simple_pagination.py: Implements basic pagination using page number and page size to return specific sections of a dataset.

1-simple_pagination_with_hypermedia.py: Extends the basic pagination by adding hypermedia controls, such as next_page and prev_page, to provide better navigation between pages.

2-index_range.py: Contains the index_range function, which calculates the start and end indices for pagination based on page number and page size.

3-hypermedia_del_pagination.py: Implements deletion-resilient pagination, ensuring that users do not miss any items from the dataset even if rows are removed between queries.

KEY CONCEPTS

Pagination: Dividing a large dataset into smaller, manageable pages.
Hypermedia Pagination: Adding navigational controls (e.g., next page, previous page) to the paginated data for easier access.

Deletion-Resilient Pagination: Ensuring that pagination remains consistent even when data is removed from the dataset.

REQUIREMENTS

Python 3.x

Pycodestyle (version 2.5.*): Code adheres to the PEP 8 style guide.

CSV File: The project uses a CSV file (Popular_Baby_Names.csv) as the dataset for pagination.

USAGE

Basic Pagination:

Retrieve a specific page of data by providing the page number and page size.
Example: get_page(page=2, page_size=20)
Hypermedia Pagination:

Retrieve paginated data with additional navigation controls, including next_page and prev_page.
Example: get_hyper(page=2, page_size=20)
Deletion-Resilient Pagination:

Handle cases where data may be deleted between queries without causing the user to miss items from the dataset.
Example: get_hyper_index(index=10, page_size=10)
Running the Code
To run any of the Python files, simply execute the script from the command line. For example:

_$ python3 0-simple_pagination.py_

Ensure that the required CSV file is in the same directory as the scripts.

TESTING
All functions and methods include type annotations and thorough documentation. You can test the length of files using wc and verify the correctness of the code using Python’s unittest module.
