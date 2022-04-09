#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Cython.Build

setuptools.setup(ext_modules=Cython.Build.cythonize(
    "src/imppkg/harmonic_mean.pyx"))
