from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

"""
cythonize: Cython코드를 C로 손쉽게 변환해준다.
"""
ext = Extension(
  name="kdtree_core",
  sources=[
    "kdtree_core.c",
    "kdtree.pyx"
  ])

setup(
  ext_modules=cythonize(ext),
  
  # https://stackoverflow.com/questions/14657375/cython-fatal-error-numpy-arrayobject-h-no-such-file-or-directory
  include_dirs=[numpy.get_include()]
)