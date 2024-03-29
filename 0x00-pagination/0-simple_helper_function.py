#!/usr/bin/env python3
"""Implement index_range function"""


def index_range(page, page_size):
    """Return tuple containing start and end index"""
    return ((page - 1) * page_size, (page * page_size))
