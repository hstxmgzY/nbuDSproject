import heapq


class DHeapNode:
    def __init__(self, key):
        self.key = key
        self.children = []


class DHeap:
    def __init__(self, d):
        self.d = d
        self.heap = []

    def bubbleUp(self, index):
        if index == 0:
            return

        parentIndex = (index - 1) // self.d
        if self.heap[parentIndex].key > self.heap[index].key:
            self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            self.bubbleUp(parentIndex)

    def bubbleDown(self, index):
        smallest = index

        for i in range(1, self.d + 1):
            childIndex = self.d * index + i
            if childIndex < len(self.heap) and self.heap[childIndex].key < self.heap[smallest].key:
                smallest = childIndex

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.bubbleDown(smallest)

    def insert(self, key):
        node = DHeapNode(key)
        self.heap.append(node)
        self.bubbleUp(len(self.heap) - 1)

    def deleteMin(self):
        if len(self.heap) == 0:
            return

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_key = self.heap.pop().key
        print(min_key, end=' ')
        self.bubbleDown(0)

    def printHeap(self):
        print("D-heap:", end=' ')
        for node in self.heap:
            print(node.key, end=' ')
        print()


if __name__ == '__main__':
    x = DHeap(3)  # Create a D-heap with d = 3

    data = [8, 3, 6, 9, 2, 5, 1, 7, 4]
    for item in data:
        x.insert(item)

    while len(x.heap) > 0:
        x.deleteMin()
