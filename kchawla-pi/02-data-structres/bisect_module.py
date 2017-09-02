"""
Part2, Chapter2: Managing Ordered Sequences with bisect Page 44
"""

import bisect
import random
import sys


HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '    |'
        print(ROW_FMT.format(needle, position, offset))
        
def example_fp():
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    
    
def generate_num(n):
    return sorted([random.randint(-100, 100) for loop in range(0,n)])


def example_bisect():
    haystack = generate_num(20)
    needles = generate_num(5)
    print(haystack)
    for needle_ in NEEDLES:
        print(needle_, bisect.bisect(HAYSTACK, needle_), 'bisect')
        print(needle_, bisect.bisect_right(HAYSTACK, needle_), 'bisect_right')
        print(needle_, bisect.bisect_left(HAYSTACK, needle_), 'bisect_left')
        print()
    print()
    
    
def example_insort():
    for needle_ in NEEDLES:
        bisect.insort(HAYSTACK, needle_)
        print(needle_, HAYSTACK, 'insort')
        
        bisect.insort_right(HAYSTACK, needle_)
        print(needle_, HAYSTACK, 'insort_right')

        bisect.insort_left(HAYSTACK, needle_)
        print(needle_, HAYSTACK, 'insort_left')
        print()
        
        
if __name__ == '__main__':
    example_bisect()
    example_insort()

#TODO: Do these operations using regular fn and compare performance.
#TODO: Similar to merge sort? Find out.
