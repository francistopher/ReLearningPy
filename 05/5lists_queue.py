def print_queue(queue):
    top_side =    "---"
    contents =    " < "
    bottom_side = "---"
    index = 0
    for element in queue:
        element_len = len(element)
        half_len = element_len // 2
        for _ in range(element_len):
            if _ == half_len:
                top_side += str(index)
                bottom_side += str(index)
            else:
                top_side += "-"
                bottom_side += "-"
        top_side += "---"
        bottom_side += "---"
        contents += element + " < "
        index += 1

    print(top_side, contents, bottom_side, sep="\n")

print("# You can use a list as a queue, I'm gonna pronounce it as kwiwi")
print("# Import deque from the collections library to convert a list to a queue") 

print("""
from collections import deque

queue = deque(["Christopher", "Josue", "Francisco"])

print(queue) # output below
""")
from collections import deque

queue = deque(["Christopher", "Josue", "Francisco"])

print(queue)

print("\n# Below is a visual representation of the queue. The '<' indicates the direction they were added\n")
print_queue(queue)

print("\n# You can append items to the queue by calling append(element) on the queue")
print("""
queue.append("De Villa")

print(queue) # Output below
""")
queue.append("De Villa")

print(queue, "\n")

print_queue(queue)

print("\n# You can append elements to the front by calling appendleft(element) on the queue")

print("""
queue.appendleft("Christopher")

print(queue) # Output below
""")

queue.appendleft("Christopher")

print(queue, "\n")

print_queue(queue)

print("\n# You can get a count of a particular element in the queue by calling queue.count(particular_element)")

print("""
christopher_count = queue.count("Christopher")

print(christopher_count) # output below
""")

christopher_count = queue.count("Christopher")

print(christopher_count)

print("\n# You can remove the last element by calling pop() on the queue")

print("""
queue.pop()

print(queue) # output below
""")

queue.pop()
print(queue, "\n")

print_queue(queue)

print("\n# You can remove the first element by calling popleft() on the queue")

print("""
queue.popleft()

print(queue) # output below
""")

queue.popleft()
print(queue, "\n")

print_queue(queue)


