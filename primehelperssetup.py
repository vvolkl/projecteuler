#!/usr/bin/env python
 
import distutils.core
import distutils.extension

ext_modules = [distutils.extension.Extension("primehelpers_cpp", 
    ["primehelpersmodule.cpp", "primehelpersmodule_boost_python.cpp"],
    libraries = ["boost_python"], extra_link_args=["-lgmp"])]

distutils.core.setup(name="primehelpers_cpp", ext_modules=ext_modules)


