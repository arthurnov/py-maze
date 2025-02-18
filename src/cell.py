from graphics import Line, Point

class Cell:
    def __init__(self, window,
                 has_left_wall = True, 
                 has_right_wall = True,
                 has_top_wall = True,
                 has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo = False):
        mid_point_1 = Point(abs(self._x1 - self._x2) // 2 + min(self._x1, self._x2), abs(self._y1 - self._y2) // 2 + min(self._y1, self._y2))
        mid_point_2 = Point(abs(to_cell._x1 - to_cell._x2) // 2 + min(to_cell._x1, to_cell._x2), abs(to_cell._y1 - to_cell._y2) // 2 + min(to_cell._y1, to_cell._y2))
        line = Line(mid_point_1, mid_point_2)
        color = "red" if undo == False else "grey"
        self._win.draw_line(line, color)