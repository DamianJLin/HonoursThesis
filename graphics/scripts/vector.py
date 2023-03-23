class Vector2:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, other):

        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __neg__(self, other):

        return Vector2(-self.x, -self.y)

    def __sub__(self, other):

        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return Vector2(x, y)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def coords(self):
        return self.x, self.y

    def __repr__(self):
        return f'Vector2({self.x}, {self.y})'
