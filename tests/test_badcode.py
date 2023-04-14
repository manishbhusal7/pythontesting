"""
Sample Test
"""
# pylint: disable=redefined-outer-name, unused-argument

import pytest
from badcode import sum_all, multiply_all, count_characters, count_words, count_lines, greet



def test_sum_all():
    assert sum_all([1, 2, 3]) == 6