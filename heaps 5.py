import heapq


def find_kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


nums = [20, 90, 30, 70, 60, 80, 40]
k = 3

print(f"The {k}rd largest element is:", find_kth_largest(nums, k))