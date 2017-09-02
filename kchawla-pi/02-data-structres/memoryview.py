"""
Part 2, chapter 2 , page 51, MemoryViews
"""
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
memv = memoryview(numbers)
print(memv)
print(len(memv))

print(memv[0])
memv_oct = memv.cast('B')
print('memv_oct', memv_oct.tolist())
print(memv_oct[5])
memv_oct[5] = 4
print(memv_oct[5])
print(numbers)  # Note change to numbers: a 4 in the most significant byte of a 2-byte unsigned integer is 102

# TODO: look up this last line
"""
Build memoryview from array of 5 short signed integers (typecode 'h'). memv sees the same 5 items in the array.
Create memv_oct by casting the elements of memv to typecode 'B' (unsigned char). Export elements of memv_oct as a list, for inspection. Assign value 4 to byte offset 5.
Note change to numbers: a 4 in the most significant byte of a 2-byte unsigned integer is 1024
"""
