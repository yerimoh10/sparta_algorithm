class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1] # -1 => 마지막 노드를 의미
        prev_max = self.items.pop()     # 루트 노드를 pop()을 이용해 배열에서 삭제 후 변수에 저장해 둔다.
        cur_index = 1   # 비교해야 할 노드의 index 를 저장해둔다.

        while cur_index <= len(self.items) - 1:     # 비교할 인덱스가 배열의 길이의 끝까지 갈 때까지 반복한다
            left_child_index = cur_index * 2    # 왼쪽 노드의 인덱스 구하기
            right_child_index = cur_index * 2 + 1   # 오른쪽 노드의 인덱스 구하기
            max_index = cur_index       # 현재 인덱스를 맥스 인덱스라 여기고 비교

            # 왼쪽 노드의 인덱스가 배열의 마지막 인덱스보다 작고, 왼쪽 노드의 값이 현재 노드의 값보다 클 때
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index    # 왼쪽 노드의 인덱스를 max 인덱스에 넣는다.
            # 오른쪽 노드와도 왼쪽 노드의 인덱스와 비교한 것처럼 동일하게 비교한다.
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index
            if max_index == cur_index:  # 왼쪽, 오른쪽 노드와 다 비교했음에도 max 인덱스가 현재 인덱스와 동일하다면
                break                   # 반복문을 빠져나간다
            # 반복문을 빠져나가지 않았다면 현재 인덱스의 위치와 max 인덱스의 위치를 변경한다.
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index   # 현재 인덱스에 max 인덱스를 넣어 반복한다.
        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]