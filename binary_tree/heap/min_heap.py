class MinHeap:
    def __init__(self):
        self.heap = []

    def peek(self):
        if not self.heap:
            return False
        return self.heap[0]

    def push(self, data):
        if type(data) == list:
          for value in data:
            self.heap.append(value)
        else:
          self.heap.append(data)
        self.heapify_up()

    def heapify_up(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2
        while self.heap[child] < self.heap[parent] and child != 0:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = parent
            parent = (child - 1) // 2

    def pop(self):
        if not self.heap:
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap.pop()
        self.heapify_down()
        return data

    def heapify_down(self):
        i = 0
        while (2*i+1) < len(self.heap):
            smaller_idx = 2*i+1
            if (2*i+2) < len(self.heap) and self.heap[2*i+2] < self.heap[2*i+1]:
                smaller_idx = 2*i+2
            if self.heap[smaller_idx] > self.heap[i]:
                return
            self.heap[smaller_idx], self.heap[i] = self.heap[i], self.heap[smaller_idx]
            i = smaller_idx

class Heap:
  """
        n
    2n+1  2n+2
    순서로 힙 구성
  """
  heap: list
  def __init__(self) -> None:
    self.heap = []

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
    # Leaf node에 값을 push한 후,
    self.heap.append(value)
    # 정렬한다.
    self.heap_up()

  def pop(self):
    if len(self.heap) < 1: return None
    if len(self.heap) == 1: return self.heap.pop()

    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    value = self.heap.pop()
    self.heap_down()

    return value
  
  def heap_up(self):
    if self.heap is None: raise("힙 인스턴스가 할당되지 않았습니다.")
    if len(self.heap) < 2: return
    current_node_index = self._get_current_index()
    parent_node_index = self._get_parent_index(current_node_index)

    # 부모 node의 value가 더 작을 때, 중단한다.
    while (current_node_index >= 0) and (self.heap[current_node_index] < self.heap[parent_node_index]):
      # swap
      self.heap[current_node_index], self.heap[parent_node_index] = self.heap[parent_node_index], self.heap[current_node_index]
      current_node_index = parent_node_index
      parent_node_index = self._get_parent_index(current_node_index)

  def heap_down(self):
    current_index = 0
    left_leaf_index = self._get_left_child_index(current_index)
    right_leaf_index = self._get_right_child_index(current_index)
    while left_leaf_index < len(self.heap):

      # 왼쪽 노드보다 root 노드가 더 큰 경우
      if self.heap[left_leaf_index] < self.heap[current_index]:
        # 스왑한다.
        self.heap[left_leaf_index], self.heap[current_index] = self.heap[current_index], self.heap[left_leaf_index]
        right_leaf_index = self._get_right_child_index(left_leaf_index)
        left_leaf_index = self._get_left_child_index(left_leaf_index)
      else:
        # 오른쪽 노드가 존재하는지 체크한다.
        if right_leaf_index >= len(self.heap): break  # 더 이상 비교할 노드가 없음

        # 1. 오른쪽 노드가 존재하고,
        # 2. 왼쪽 노드가 root보다 작으며,
        # 3. 오른쪽 노드보다 root노드가 더 큰 경우
        if self.heap[right_leaf_index] < self.heap[current_index]:
          # 스왑한다.
          self.heap[right_leaf_index], self.heap[current_index] = self.heap[current_index], self.heap[right_leaf_index]
          left_leaf_index = self._get_left_child_index(right_leaf_index)
          right_leaf_index = self._get_right_child_index(right_leaf_index)
        else:
           # 하위 노드와 교체할 수 없다면 종료한다.
           break

heap = MinHeap()
# heap.push()

heap2 = Heap()

print(5 // 2)
print(5 % 2)


for value in [5,3,1,2,6,8]:
  heap.push(value)
print(heap.heap)

for value in [5,3,1,2,6,8]:
  heap2.push(value)
print(heap2.heap)
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())