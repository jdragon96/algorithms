import numpy as np
cimport numpy as np
from libc.stdint cimport uint32_t, int8_t, uint8_t
cimport cython

cdef extern from "kdtree_core.h":
  void get_bounding_box(float *points, uint32_t *pidx, int8_t dim, float *bbox);
  void create_kdtree(float *points, uint8_t dim, uint32_t length);

cdef class KdTree:

  cdef float *data_float_pointer

  def __cinit__(KdTree self):
    pass

  def __init__(KdTree self, np.ndarray data_pts not None):
    cdef np.ndarray[float, ndim=1] data_array_float
    data_array_float = np.ascontiguousarray(data_pts.ravel(), dtype=np.float32)
    print(data_array_float)

    self.data_float_pointer = <float*>data_array_float.data;