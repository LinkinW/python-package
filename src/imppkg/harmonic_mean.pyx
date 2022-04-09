#!/usr/bin/env python
# -*- coding: utf-8 -*-

def harmonic_mean(list):
    """
    输入一串浮点数，计算调和平均数
    """
    ret = 0
    n = 0
    for data in list:
        ret = ret + 1 / data
        n+=1
    return n/ret