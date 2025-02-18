from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver 2000")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    
    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

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
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = 0
        self.__y2 = 0
        self.__win = window

    def draw(self, top_left, bottom_right):
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)
        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, "black")

