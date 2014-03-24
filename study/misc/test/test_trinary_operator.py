# -*- coding: utf-8 -*-

from nose.tools import eq_


def test_using_if_else():
    '''基于if...else的3元操作模拟'''
    a = 2
    b = 3 if a > 1 else 4
    eq_(b, 3)


def test_using_and_or():
    '''基于if...else的3元操作模拟'''
    a = 2
    b = a > 1 and 3 or 4
    eq_(b, 3)


def test_when_facing_boolean():
    '''计算结果是boolean时，只能用if...else形式'''
    a = 2
    b = a > 1 and False or True
    eq_(b, True)
    c = False if a > 1 else True
    eq_(c, False)
