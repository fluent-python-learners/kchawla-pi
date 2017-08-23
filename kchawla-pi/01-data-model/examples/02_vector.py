class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def sort_spades_high(crad):
    pass

vector0 = Vector(2, 3)
vector1 = Vector(3, 4)
print(vector0 + vector1)
print(vector0 * 5)
print(vector0)
