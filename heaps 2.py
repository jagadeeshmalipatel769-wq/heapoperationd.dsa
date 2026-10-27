def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] <= heap[parent]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent


def insert_value(heap, value):
    heap.append(value)
    sift_up(heap, len(heap) - 1)


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


def extract_max(heap):
    max_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    sift_down(heap, len(heap), 0)
    return max_value


heap = [90, 70, 80, 40, 60]

insert_value(heap, 100)
print("After inserting 100:", heap)

removed = extract_max(heap)
print("Extracted max:", removed)
print("After extraction:", heap)