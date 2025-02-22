from graphics import Window
from cell import Cell
from maze import Maze

def main():
    print("start")
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 10, 50, 50, win)

    win.wait_for_close()
    print("end")

if __name__ == "__main__":
    main()