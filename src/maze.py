from cell import Cell
import random
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
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j, False)

    def _draw_cell(self, i, j, anim=True):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        if anim:
            self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        # print("DEBUG: SOLVIG")
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        # print(f"DEBUG: SOLVING _R i: {i} j: {j}")
        self._animate()
        # print(f"DEBUG: CELL({i}, {j}) Animated")
        self._cells[i][j].visited = True
        # print(f"DEBUG: CELL({i}, {j}) Set 'visited'")
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            # print("DEBUG: Found END")
            return True
        # print(f"DEBUG: CELL({i}, {j}) Looking at walls")
        # print(f"DEBUG: CELL({i}, {j})'s walls:\nT: {self._cells[i][j].has_top_wall} | L: {self._cells[i][j].has_left_wall} | B: {self._cells[i][j].has_bottom_wall} | R: {self._cells[i][j].has_right_wall}")
        #right
        if self._cells[i][j].has_right_wall == False and i+1 < self._num_cols and self._cells[i+1][j].visited == False:
            # print("DEBUG: Moving LEFT")
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        #left
        if self._cells[i][j].has_left_wall == False and i-1 >= 0 and self._cells[i-1][j].visited == False:
            # print("DEBUG: Moving RIGHT")
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        #up
        if self._cells[i][j].has_top_wall == False and j-1 >= 0 and self._cells[i][j-1].visited == False:
            # print("DEBUG: Moving UP")
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        #down
        if self._cells[i][j].has_bottom_wall == False and j+1 < self._num_rows and self._cells[i][j+1].visited == False:
            # print("DEBUG: Moving DOWN")
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False