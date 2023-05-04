# https://github.com/storpipfugl/pykdtree/blob/master/pykdtree/_kdtree_core.c
from kdtree import KdTree
import numpy as np

a = np.array([[0,0,0], [0.5, 0.5, 0.5], [0.8, 0.4, 0.6], [1, 1, 1]])
tree = KdTree(a)