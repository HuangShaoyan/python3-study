# -*- coding: utf-8 -*-

from nose.tools import eq_


def foo(bar=[]):
    bar.append('baz')
    return bar


def test_ok():
    '''默认参数共享同一个实例'''
    eq_(['baz'], foo())
    eq_(['baz', 'baz'], foo())
    eq_(['baz', 'baz', 'baz'], foo())
