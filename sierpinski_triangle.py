import turtle as t

import enum
class Orientation(enum.Enum):
    UP = 0
    DOWN = 1

class SierpinskiTriangle():

    _colors = [ 'blue', 'violet', 'orange','red','yellow', 'green']

    def __init__(self, orientation = Orientation.UP):
        self._orientation = orientation
        self._angle = 120

    def sierpinski(self, level, length):
        if(level==0):
            return

        for i in range(3):
            self.sierpinski(level-1, length/2)
            defColor = self._get_color(level)
            self._draw_triangle(defColor, level, length)


    def _draw_triangle(self, color, level, length):
        if self._orientation is Orientation.UP:
            self._draw_triangle_up(color, level, length)
        else:
            self._draw_triangle_down(color, level, length)

    def _draw_triangle_up(self, color, level, length):
        t.color(color)
        t.fd(length)
        t.left(self._angle)

    def _draw_triangle_down(self, color, level, length):
        t.color(color)
        t.fd(length)
        t.right(self._angle)

    def _get_color(self, n):
        return self._colors[n]

def run():
    sierpinski_triangle = SierpinskiTriangle(orientation = Orientation.DOWN)

    sierpinski_triangle.sierpinski(5, 400)

    t.exitonclick()

run()
