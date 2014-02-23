# -*- coding: utf-8 -*-

from unittest import TestCase


class TestDivision(TestCase):

    def test_div(self):
        '''1 / 2 不再得到0，而是0.5'''
        self.assertEqual(0.5, 1 / 2)
