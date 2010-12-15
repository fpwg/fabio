#!/usr/bin/env python
#coding: utf8

"""
Setup script for python distutils package and fabio

Added Erik Knudsen's mar 345 code
"""
from setuptools import setup, find_packages
from distutils.core import  Extension


# for numpy
from numpy.distutils.misc_util import get_numpy_include_dirs



mar345_backend = Extension('mar345_io',
                           include_dirs=get_numpy_include_dirs(),
                           sources=['src/mar345_iomodule.c',
                                      'src/ccp4_pack.c'])

cf_backend = Extension('cf_io', include_dirs=get_numpy_include_dirs(),
      sources=['src/cf_iomodule.c', 'src/columnfile.c'])

byteOffset_backend = Extension("byte_offset",
                       include_dirs=get_numpy_include_dirs(),
                           sources=['src/byte_offset.c'])

# See the distutils docs...
setup(name='fabio',
      version="0.0.5",
      author="Henning Sorensen, Erik Knudsen and Jon Wright",
      author_email="fable-talk@lists.sourceforge.net",
      description='Image IO for fable',
      url="http://fable.wiki.sourceforge.net/fabio",
      download_url="http://sourceforge.net/project/showfiles.php?group_id=82044&package_id=248946",
      ext_package="fabio",
#      cmdclass = {'build_ext': build_ext},
      ext_modules=[mar345_backend, cf_backend, byteOffset_backend ],
      packages=["fabio"],
      package_dir={"fabio": "fabio" }
      )


