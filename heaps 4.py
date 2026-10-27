class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][1] <= self.heap[parent][1]:
                break
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def _sift_down(self, i):
        n = len(self.heap)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left][1] > self.heap[largest][1]:
            largest = left
        if right < n and self.heap[right][1] > self.heap[largest][1]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(largest)

    def insert(self, name, urgency):
        self.heap.append((name, urgency))
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return top

    def is_empty(self):
        return len(self.heap) == 0


triage = PriorityQueue()

triage.insert("Sprained ankle", 2)
triage.insert("Chest pain", 9)
triage.insert("Minor cut", 1)
triage.insert("Broken arm", 6)

while not triage.is_empty():
    name, urgency = triage.extract_max()
    print(f"Treating: {name} (urgency {urgency})")