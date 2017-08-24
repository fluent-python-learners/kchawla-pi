import dis


# dis is the python byte-code disassembler, breaks down py code into byte code. Returns None

# dis.dis('a_tuple = (0, 1, [2, 3])')
# dis.dis('a_tuple[2] *= 2')


a_tuple = (0, 1, [2, 3])
print(a_tuple)

try:
    a_tuple[2] *= 2
except TypeError:
    print(a_tuple)  # the reference to mutable in the tuple(immutable) cahnges and raises a type error as well.
else:
    print('No error raised')
    


# :TODO: bisect.bisect, bisect.insort, array.array, memoryview,
