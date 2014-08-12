#!/usr/bin/env python
 
from distutils.core import setup
from distutils.extension import Extension
 
setup(name="PackageName",
    ext_modules=[
        Extension("primehelpers", ["primehelpersmodule.cpp"],
        libraries = ["boost_python"], extra_link_args=["-lgmp"])
    ])

