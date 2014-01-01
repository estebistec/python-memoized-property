#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_memoized_property
----------------------

Tests of the `memoized_property` module.

"""


import unittest

from memoized_property import memoized_property


class C(object):
    """Example class for testing ``@memoized_property``"""

    load_name_count = 0

    @memoized_property
    def name(self):
        "name's docstring"
        self.load_name_count += 1
        return "the name"


class TestMemoizedProperty(unittest.TestCase):
    """
    Tests of the ``memoized_property`` decorator.

    """

    def setUp(self):
        self.instance = C()

    def test_property_not_accessed_not_loaded(self):
        """
        When a memoized property has not been accessed, the decorated loading function should not
        have been called.
        """
        self.assertEqual(0, self.instance.load_name_count)

    def test_property_not_accessed_no_private_attribute(self):
        """
        When a memoized property has not been accessed, it should not have a private attribute for
        storing the result of a load.
        """
        self.assertFalse(hasattr(self.instance, '_name'))

    def test_property_accessed_loaded(self):
        """
        When a memoized property has been accessed, the decorated loading function should have been
        called once.
        """
        self.instance.name
        self.assertEqual(1, self.instance.load_name_count)

    def test_property_accessed_private_attribute(self):
        """
        When a memoized property has been accessed, it should have a private attribute for storing
        the result of a load.
        """
        self.instance.name
        self.assertTrue(hasattr(self.instance, '_name'))

    def test_property_multiple_accesses_one_load(self):
        """
        When a memoized property has been accessed multiple times, the decorated loading function
        should have been called only once.
        """
        self.instance.name
        self.instance.name
        self.assertEqual(1, self.instance.load_name_count)

    def test_property_docstring(self):
        """
        A memoized property should expose the docstring of the underlying load function (the fget).
        """
        self.assertEqual("name's docstring", C.name.__doc__)


if __name__ == '__main__':
    unittest.main()
