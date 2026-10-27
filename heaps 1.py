def sift_down(heap, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        sift_down(heap, n, largest)


def build_heap(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(heap, n, i)


arr = [20, 90, 30, 70, 60, 80, 40]

build_heap(arr)

print("Heapified array:", arr)