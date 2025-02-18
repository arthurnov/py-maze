from graphics import Window
from cell import Cell

def main():
    print("start")
    win = Window(800, 600)

    c = Cell(win)
    c.draw(50, 50, 100, 100)

    d = Cell(win)
    d.draw(100, 50, 150, 100)
    d.draw_move(c)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)



    win.wait_for_close()
    print("end")

if __name__ == "__main__":
    main()