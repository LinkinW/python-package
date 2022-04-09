#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
计算调和平均数

输入：调用参数sys.arg，输入的值，会转换为浮点数

输出：
调和平均数

调和平均数计算方法

异常处理：
输入无法转换为浮点数或者输入为0，返回0.0
"""
import sys
from imppkg.harmonic_mean import harmonic_mean
from termcolor import cprint


def main():
    result = 0.0
    try:
        nums = [float(num) for num in sys.argv[1:]]
    except ValueError:
        nums = []
    try:
        result = harmonic_mean(nums)
    except ZeroDivisionError:
        a = 1
        pass

    cprint(result, 'red', 'on_cyan', attrs=['bold'])
