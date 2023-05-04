import numpy as np

import heapq
import itertools
import operator
import math
from collections import deque
from functools import wraps
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from util import data

class Node():
  def __init__(self, data=None, left=None, right=None, axis=None):
    self.data = data
    self.left = left
    self.right = right
    self.axis = axis
    
  def __repr__(self) -> str:
    return f"{self.data}"

#################################################################################### FUNCTIONS    

def _create(
  current_points,
  axis,
  dim
):
  # 0. 탈출조건
  # 0-1 차원이 맞지 않는 경우
  
  # 0-2 더이상 트리를 생성할 데이터가 없는경우
  if len(current_points) == 0:
    return
  
  # 1. current_dim을 기준으로 정렬한다.
  current_points.sort(key=lambda p: p[axis])
  length = len(current_points) // 2
  new_axis = (axis+1) % dim
  
  # 2. KDTree를 생성한다.
  left = _create(current_points[:length], new_axis, dim)
  right = _create(current_points[length+1:], new_axis, dim)
  return Node(current_points[length], left, right, axis)
  
def is_longer_than_threshold(
  center,
  target,
  dim,
  distance
):
  dist = 0
  for index in range(dim):
    dist += (center[index] - target[index]) ** 2
  return True if dist > distance else False

def _find_nearest(
  tree: Node,
  start, 
  neaerest: list,
  distance,
  square_distnace,
  dim
):
  if tree is None: return
  if tree.data is None: return
  # 1. 거리 비교
  if not is_longer_than_threshold(start, tree.data, dim, square_distnace):
    # 1-1 반경 내
    neaerest.append(tree.data)
  
  sub_distnace = start[tree.axis] - start[tree.axis]
  # 2. 다음 트리 탐색
  if sub_distnace > distance:
    # 2-1 메인축 기준, 기준보다 값이 큰 경우
    # => left side만 탐색한다.
    _find_nearest(tree.left, start, neaerest, distance, square_distnace, dim)
  elif sub_distnace <= distance and -distance < sub_distnace:
    # 2-2 원 내부에 존재할 때
    # => 양쪽 다 탐색
    _find_nearest(tree.left, start, neaerest, distance, square_distnace, dim)
    _find_nearest(tree.right, start, neaerest, distance, square_distnace, dim)
  else:
    # 2-3 메인축 기준, 기준보다 값이 작은 경우
    # => right side만 탐색
    _find_nearest(tree.right, start, neaerest, distance, square_distnace, dim)

#################################################################################### COMMANDS
  
def create(
  points
):
  # 메타정보 설정
  length = len(points)
  dim = len(points[0])
  
  # kdtree 생성 시작
  return _create(points, 0 % dim, dim)

def visualization(
  tree,
  points = []
):
  points = np.array(points)
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')
  ax.set_xlabel("$x_0$")
  ax.set_ylabel("$y_0$")
  ax.set_zlabel("$f(x_0, y_0)$")
  # color = ["red", "blue", "green"]
  color = ["black", "dimgray", "dimgrey","gray", "grey", "darkgray", "darkgrey",
           "silver", "lightgray", "lightgrey", "gainsboro", "whitesmoke"]
  color_index = 0
  target_nodes = []
  target_nodes.append(tree.left)
  target_nodes.append(tree.right)
  
  ax.scatter(*tree.data, ".", color=color[color_index])
  while(len(target_nodes) >= 1):
    color_index = (color_index+1)%len(color)
    
    for node in target_nodes:
      ax.scatter(*node.data, ".", color=color[color_index])
    
    temp_nodes = []
    for node in target_nodes:
      if node.left != None:
        temp_nodes.append(node.left)
      if node.right != None:
        temp_nodes.append(node.right)
        
    target_nodes = temp_nodes

  ax.scatter(points[:, 0], points[:, 1], points[:, 2], ".", color='red')
  plt.show()

def find_nearest(
  tree,
  start, 
  distance
):
  nearest_points = []
  dim = len(start)
  d = distance
  distance *= distance
  _find_nearest(tree, start, nearest_points, d, distance, dim)
  return nearest_points
  

if __name__ == "__main__":
  points = data.gen_3d_points(300)
  kdtree = create(points)
  points = find_nearest(kdtree, [0.5, 0.5, 0.5], 0.3)
  visualization(kdtree, points)