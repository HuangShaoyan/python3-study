# -*- coding: utf-8 -*-

import ipaddress

from nose.tools import eq_
from nose.tools import ok_


def test_ipv4():
    '''IPv4的基础知识'''
    ip4 = ipaddress.ip_address('192.168.1.1')
    eq_('192.168.1.1', str(ip4))
    eq_(4, ip4.version)
    ok_(not ip4.is_multicast)
    ok_(not ip4.is_unspecified)
    ok_(ip4.is_private)
    ok_(not ip4.is_reserved)
    ok_(not ip4.is_loopback)
    ok_(not ip4.is_link_local)


def test_unspecified():
    '''0.0.0.0 是unspecified ip'''
    ip4 = ipaddress.ip_address('0.0.0.0')
    ok_(ip4.is_unspecified)


def test_loopback():
    '''127.0.0.0 - 127.255.255.255 是loopback ip'''
    ok_(ipaddress.ip_address('127.0.0.0').is_loopback)
    ok_(ipaddress.ip_address('127.0.0.1').is_loopback)
    ok_(ipaddress.ip_address('127.255.255.255').is_loopback)
