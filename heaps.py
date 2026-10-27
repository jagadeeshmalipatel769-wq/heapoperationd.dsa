heap = [90, 70, 80, 40, 60, 30, 20]

print("Root (max value):", heap[0])

for i in range(len(heap)):
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    line = f"Node {heap[i]} -> "
    if left_index < len(heap):
        line += f"left: {heap[left_index]} "
    if right_index < len(heap):
        line += f"right: {heap[right_index]}"
    print(line)