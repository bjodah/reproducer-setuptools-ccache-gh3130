#!/usr/bin/env python3

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np

my_numpy_ext = Extension("my_numpy_pkg._my_numpy_ext", ["my_numpy_pkg/_my_numpy_ext.pyx"])
my_numpy_ext.language = "c++"
my_numpy_ext.include_dirs = [np.get_include()]

setup(
    name="my_numpy_pkg",
    ext_modules=cythonize([my_numpy_ext])
)
