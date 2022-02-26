#!/usr/bin/env python3

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

my_ext = Extension("my_plain_pkg._my_ext", ["my_plain_pkg/_my_ext.pyx"])
my_ext.language = "c++"

setup(
    name="my_plain_pkg",
    ext_modules=cythonize([my_ext])
)
