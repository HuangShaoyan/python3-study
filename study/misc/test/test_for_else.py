# -*- coding: utf-8 -*-

from nose.tools import eq_


def test_for_else_ok():
    '''for break时，不执行else'''
    for i in range(3):
        if i == 2:
            break
    else:
        i = 10

    eq_(i, 2)


def test_for_else_break():
    '''for 没有break时，执行else'''
    for i in range(3):
        if i == 3:
            break
    else:
        i = 10

    eq_(i, 10)
