import tkinter as tk
import random
import time

# --- Configuration ---
CELL_SIZE = 20
MAZE_WIDTH = 30
MAZE_HEIGHT = 20
WINDOW_BG = "#1e1e1e"
WALL_COLOR = "#d4d4d4"
PATH_COLOR = "#4a90e2"
SOLUTION_COLOR = "#32cd32"
DELAY = 0.01  # Animation delay in seconds

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Generator and Solver")
        self.canvas = tk.Canvas(
            root,
            width=MAZE_WIDTH * CELL_SIZE,
            height=MAZE_HEIGHT * CELL_SIZE,
            bg=WINDOW_BG,
        )
        self.canvas.pack()

        self.generate_and_solve()

    def draw_maze(self, grid, solution_path=None):
        self.canvas.delete("all")
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                x1, y1 = x * CELL_SIZE, y * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                if cell == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=WALL_COLOR, outline="")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=WINDOW_BG, outline="")
        
        if solution_path:
            for x, y in solution_path:
                x1, y1 = x * CELL_SIZE + 2, y * CELL_SIZE + 2
                x2, y2 = x1 + CELL_SIZE - 4, y1 + CELL_SIZE - 4
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=SOLUTION_COLOR, outline="")
        self.root.update()


    def generate_maze(self):
        grid = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
        stack = [(0, 0)]
        grid[0][0] = 0

        while stack:
            x, y = stack[-1]
            neighbors = []
            for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and grid[ny][nx] == 1:
                    neighbors.append((nx, ny))
            
            if neighbors:
                nx, ny = random.choice(neighbors)
                grid[ny][nx] = 0
                grid[y + (ny - y) // 2][x + (nx - x) // 2] = 0
                stack.append((nx, ny))
                # --- Animation Step ---
                self.draw_maze(grid)
                time.sleep(DELAY / 2)
            else:
                stack.pop()
        
        grid[MAZE_HEIGHT - 1][MAZE_WIDTH - 1] = 0 # Ensure exit is open
        return grid

    def solve_maze(self, grid):
        start, end = (0, 0), (MAZE_WIDTH - 1, MAZE_HEIGHT - 1)
        stack = [(start, [start])]
        visited = {start}

        while stack:
            (x, y), path = stack.pop()
            
            # --- Animation Step ---
            self.draw_maze(grid, path)
            time.sleep(DELAY)

            if (x, y) == end:
                return path

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and grid[ny][nx] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_path = path + [(nx, ny)]
                    stack.append(((nx, ny), new_path))
        return None

    def generate_and_solve(self):
        self.canvas.create_text(
            (MAZE_WIDTH * CELL_SIZE) / 2,
            (MAZE_HEIGHT * CELL_SIZE) / 2,
            text="Generating Maze...",
            fill="white",
            font=("Arial", 20)
        )
        self.root.update()
        time.sleep(1)

        maze_grid = self.generate_maze()
        
        self.canvas.create_text(
            (MAZE_WIDTH * CELL_SIZE) / 2,
            (MAZE_HEIGHT * CELL_SIZE) / 2,
            text="Solving...",
            fill="white",
            font=("Arial", 20)
        )
        self.root.update()
        time.sleep(1)

        solution_path = self.solve_maze(maze_grid)
        if solution_path:
            self.draw_maze(maze_grid, solution_path)
            
        self.root.after(5000, self.generate_and_solve) # Restart after 5 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()