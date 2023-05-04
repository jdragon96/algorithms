from enum import Enum
class ChildPosition(Enum):
  LEFT=0
  RIGHT=1
  ROOT=3

class MaxHeap:
  """
        n
    2n+1  2n+2
    순서로 힙 구성
  """
  heap: list
  def __init__(self, values: list = []) -> None:
    self.heap = []
    for value in values:
      self._heap_up(value, self.heap)


  # Functions #############################################################################
  def _get_parent_index(self, index):
    # n => 2n+1, 2n+2
    return int((index - 1) / 2)
  
  def _get_current_index(self, heap):
    return len(heap) - 1
  
  def _get_left_child_index(self, parent):
    return 2 * parent + 1
  
  def _get_right_child_index(self, parent):
    return 2 * parent + 2
  
  def _is_right_node(self, index):
    """ 해당 노드의 right 노드가 존재하는가? """
    if index < 2: return False
    if index % 2 == 0:
      # 해당 index가 right node인 경우
      return True
    else:
      return False
    
  def _what_is_node_position(self, index):
    if index == 0: return ChildPosition.ROOT
    elif index % 2 == 0: return ChildPosition.RIGHT
    elif index % 2 == 1: return ChildPosition.LEFT

  def _sort_between_left_and_right(self, heap, current_node_index):
    pos = self._what_is_node_position(current_node_index)
    if pos == ChildPosition.LEFT:
      if len(heap) >= current_node_index:
        if heap[current_node_index] > heap[current_node_index+1]:
          heap[current_node_index], heap[current_node_index+1] = heap[current_node_index+1], heap[current_node_index]
          current_node_index = current_node_index+1
    elif pos == ChildPosition.RIGHT:
      if heap[current_node_index] < heap[current_node_index-1]:
        heap[current_node_index], heap[current_node_index-1] = heap[current_node_index-1], heap[current_node_index]
        current_node_index = current_node_index-1

  def _heap_up(self, value, heap: list):
    """ Leaf node에서 최적 위치를 찾아가도록 한다. """
    if heap is None: raise("힙 인스턴스가 할당되지 않았습니다.")
    heap.append(value)
    if len(heap) < 2: return
    current_node_index = self._get_current_index(heap)
    parent_node_index = self._get_parent_index(current_node_index)

    # 부모 node의 value가 더 작을 때, 중단한다.
    while (current_node_index >= 0) and (heap[current_node_index] > heap[parent_node_index]):
      # swap
      heap[current_node_index], heap[parent_node_index] = heap[parent_node_index], heap[current_node_index]
      # update node index
      current_node_index = parent_node_index
      parent_node_index = self._get_parent_index(current_node_index)
      # sorting
      self._sort_between_left_and_right(heap, current_node_index)

  def _heap_down(self, heap):
    """ Root node에서 최적 위치를 찾아가도록 한다. """
    current_index = 0
    left_leaf_index = self._get_left_child_index(current_index)
    right_leaf_index = self._get_right_child_index(current_index)
    while left_leaf_index < len(heap):

      # 왼쪽 노드보다 root 노드가 더 큰 경우
      if heap[left_leaf_index] > heap[current_index]:
        # 스왑한다.
        heap[left_leaf_index], heap[current_index] = heap[current_index], heap[left_leaf_index]
        right_leaf_index = self._get_right_child_index(left_leaf_index)
        left_leaf_index = self._get_left_child_index(left_leaf_index)
      else:
        # 오른쪽 노드가 존재하는지 체크한다.
        if right_leaf_index >= len(heap): break  # 더 이상 비교할 노드가 없음

        # 1. 오른쪽 노드가 존재하고,
        # 2. 왼쪽 노드가 root보다 작으며,
        # 3. 오른쪽 노드보다 root노드가 더 큰 경우
        if heap[right_leaf_index] > heap[current_index]:
          # 스왑한다.
          heap[right_leaf_index], heap[current_index] = heap[current_index], heap[right_leaf_index]
          left_leaf_index = self._get_left_child_index(right_leaf_index)
          right_leaf_index = self._get_right_child_index(right_leaf_index)
        else:
           # 하위 노드와 교체할 수 없다면 종료한다.
           break


  # Commands ####################################################################################
  def push(self, value):
    # Leaf node에 값을 push한 후, 정렬한다.
    self._heap_up(value, self.heap)

  def pop(self):
    if len(self.heap) < 1: return None
    if len(self.heap) == 1: return self.heap.pop()

    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    value = self.heap.pop()
    self._heap_down(self.heap)

    return value


        
if __name__ == "__main__":
  heap2 = MaxHeap([5,3,1,2,6,8])
  print(heap2.heap)
  print(heap2.pop())
  print(heap2.pop())
  print(heap2.pop())
  print(heap2.pop())
  print(heap2.pop())
  print(heap2.pop())
  print(heap2.pop())
  print(heap2.pop())