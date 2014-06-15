# -*- coding: utf-8 -*-

from nose.tools import eq_


class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


def test_mro():
    ''' 子类的class variable继承自父类 '''
    eq_(1, A.x)
    eq_(1, B.x)
    eq_(1, C.x)

    B.x = 2
    eq_(1, A.x)
    eq_(2, B.x)
    eq_(1, C.x)

    A.x = 3
    eq_(3, A.x)
    eq_(2, B.x)
    eq_(3, C.x)  # C.x is actually A.x
