from graphics import Window, Point, Line

def main():
    print("start")
    win = Window(800, 600)

    point1 = Point(10, 10)
    point2 = Point(790, 590)

    line = Line(point1, point2)

    win.draw_line(line, "black")

    win.wait_for_close()
    print("end")

if __name__ == "__main__":
    main()