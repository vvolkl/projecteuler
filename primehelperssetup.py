#!/usr/bin/env python
 
from distutils.core import setup
from distutils.extension import Extension
 
setup(name="primehelpers_cpp",
    ext_modules=[
        Extension("primehelpers_cpp", ["primehelpersmodule.cpp"],
        libraries = ["boost_python"], extra_link_args=["-lgmp"])
    ])

