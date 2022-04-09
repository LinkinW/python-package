#!/usr/bin/env python
# -*- coding: utf-8 -*-

def too_long(l: str) -> int:
    """
    :param l: input str

    :return: input str is longer than standard
    """
    return len(l) > 2


print(too_long([1, 2, 3]))