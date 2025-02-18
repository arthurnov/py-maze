from graphics import Window, Point, Line, Cell

def main():
    print("start")
    win = Window(800, 600)

    point1 = Point(10, 10)
    point2 = Point(20, 20)

    line = Line(point1, point2)

    # win.draw_line(line, "black")
    
    cell = Cell(win)
    cell.draw(point1, point2)

    win.wait_for_close()
    print("end")

if __name__ == "__main__":
    main()