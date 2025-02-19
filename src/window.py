from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    root_widget = Tk()
    root_widget.title = "Maze Solver 2000"
    