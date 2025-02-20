from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self.win)] * self.num_rows] * self.num_cols
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
        

    def _draw_cell(self, i, j):
        cell_x = i * self.cell_size_x + self.x1
        cell_y = j * self.cell_size_y + self.y1
        self._cells[i][j].draw(cell_x, cell_y, cell_x + self.cell_size_x, cell_y + self.cell_size_y)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)