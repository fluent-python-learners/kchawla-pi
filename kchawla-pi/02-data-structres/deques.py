from collections import deque

d1 = deque([1, 2, 3, 4, 5])
print('d1', d1)
d1.extend([-1, -2, -3])
print('d1', d1)
d1.extendleft([-1, -2, -3])
print('d1', d1)
print()
l1 = list([1, 2, 3, 4, 5])
print('l1', l1)
l1.extend([-1, -2, -3])
print('l1', l1)

# l1.extendleft([-1, -2, -3])
print('l1', l1)
print()
l1.extend(set([10, 20]))
print('l1', l1)

