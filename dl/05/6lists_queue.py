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

from collections import deque

queue = deque(["Christopher", "Josue", "Francisco"])

print("# Continuing on, you can remove an element from the queue by calling queue.remove(element)")

print("""
queue.remove("Josue") # A ValueError would arise if the element didn't exist

print(queue) # output below
""")

queue.remove("Josue")

print(queue, "\n")

print_queue(queue)

print("\n# You can insert the element back at any position by calling queue.insert(position, element)")

print("""
queue.insert(1, "Josue")

print(queue) # output below
""")

queue.insert(1, "Josue")

print(queue, '\n')

print_queue(queue)

print("\n# What if I want to append multiple items? Call the extend function on the queue")
print('# queue.extend([element1, element2]') 

print("""
queue.extend(["Francisco1", "Francisco2"])

print(queue) # Output below
""")

queue.extend(["Francisco1", "Francisco2"])

print(queue, '\n')

print_queue(queue)

print("\n# What if I want to append multiple items on the front? Call the extendleft functon on the queue")
print("# queue.extendleft([element1, element2]")

print("""
queue.extendleft(["Christopher1", "Christopher2"])

print(queue) # Output below
""")

queue.extendleft(["Christopher1", "Christopher2"])

print(queue, '\n')

print_queue(queue)

print("\n# What if I want to find the position of a particular element? Call the index function on the queue")
print("# queue.index(element) or queue.index(element, left_bound_inclusive, right_bound_exclusive)")

print("""
# If the element isn't within bounds it would produce a ValueError
element_index = queue.index("Christopher1", 0, 2)
element_index = queue.index("Christopher1")

print(element_index) # output below
""")

element_index = queue.index("Christopher1", 0, 2)

print(element_index)


