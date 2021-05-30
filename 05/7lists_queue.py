from collections import deque

queue = deque(["Christopher2", "Christopher1", "Christopher", "Josue", "Francisco", "Francisco1", "Francisco2"])

print("# Continuing on, what if I want to produce a shallow copy of a queue, call the copy function on the queue")

print("""
reversed_queue = queue.copy()

print(reversed_queue, '\\n')
print(queue) # Output below
""")

reversed_queue = queue.copy()
print(reversed_queue, '\n')
print(queue)

print("\n# What if I want to really reverse the reversed_queue? Call the reverse function on the queue")

print("""
reversed_queue.reverse()

print(reversed_queue, '\\n') # This got reversed
print(queue) # Output below
""")

reversed_queue.reverse()
print(reversed_queue, '\n')
print(queue)

print("\n# Elements of the queue can be 'rotated', aka, moving an element to the other end")
print("# Call queue.rotate(number_of_elements), number_of_elements can either be positive or negative")

print("""
queue.rotate(2) # a positive value moves an element from the back to the front, 1 by 1

print(queue)
""")

queue.rotate(2)
print(queue)

print("""
queue.rotate(-2) # a negative values moves an element from the front to the back, 1 by 1

print(queue) # output below
""")

queue.rotate(-2)
print(queue)

print("\n# You can get the max length of the queue by calling queue.maxlen")

print("""
queue_length = queue.maxlen

print(queue_length) # output below
""")

queue_length = queue.maxlen

print(queue_length, "\n\n# What? I expected a number! That's right, you expected a max count of the elements in the queue")
print("# maxlen returns the max count of elements the queue is set to support")
print("# in the deque function we can pass in the iterable and set the max length")

print("""
queue = deque(["Christopher", "Francisco"], maxlen=10)

print(queue.maxlen) # output below
""")

queue = deque(["Christopher", "Francisco"], maxlen=10)
print(queue.maxlen) # output below

print("\nNow it's time to empty the queue by calling the clear function on queue")

print("""
queue.clear()

print(queue) # output below
""")
queue.clear()
print(queue)


