class Heap:
  """
        n
    2n+1  2n+2
    순서로 힙 구성
  """
  heap: list
  def __init__(self, values: list = []) -> None:
    self.heap = []
    for value in values:
      self.heap_up(value, self.heap)

  def _get_parent_index(self, index):
    # n => 2n+1, 2n+2
    return int((index - 1) / 2)
  def _get_current_index(self):
    return len(self.heap) - 1
  def _get_left_child_index(self, parent):
    return 2 * parent + 1
  def _get_right_child_index(self, parent):
    return 2 * parent + 2

  def push(self, value):
    # Leaf node에 값을 push한 후, 정렬한다.
    self.heap_up(value, self.heap)

  def pop(self):
    if len(self.heap) < 1: return None
    if len(self.heap) == 1: return self.heap.pop()

    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    value = self.heap.pop()
    self.heap_down(self.heap)

    return value

  def heap_up(self, value, heap: list):
    if heap is None: raise("힙 인스턴스가 할당되지 않았습니다.")
    heap.append(value)
    if len(heap) < 2: return
    current_node_index = self._get_current_index()
    parent_node_index = self._get_parent_index(current_node_index)

    # 부모 node의 value가 더 작을 때, 중단한다.
    while (current_node_index >= 0) and (heap[current_node_index] < heap[parent_node_index]):
      # swap
      heap[current_node_index], heap[parent_node_index] = heap[parent_node_index], heap[current_node_index]
      current_node_index = parent_node_index
      parent_node_index = self._get_parent_index(current_node_index)

  def heap_down(self, heap):
    current_index = 0
    left_leaf_index = self._get_left_child_index(current_index)
    right_leaf_index = self._get_right_child_index(current_index)
    while left_leaf_index < len(heap):

      # 왼쪽 노드보다 root 노드가 더 큰 경우
      if heap[left_leaf_index] < heap[current_index]:
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
        if heap[right_leaf_index] < heap[current_index]:
          # 스왑한다.
          heap[right_leaf_index], heap[current_index] = heap[current_index], heap[right_leaf_index]
          left_leaf_index = self._get_left_child_index(right_leaf_index)
          right_leaf_index = self._get_right_child_index(right_leaf_index)
        else:
           # 하위 노드와 교체할 수 없다면 종료한다.
           break

heap2 = Heap([5,3,1,2,6,8])
# for value in [5,3,1,2,6,8]:
#   heap2.push(value)
print(heap2.heap)
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
