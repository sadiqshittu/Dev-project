import random

class MazeGenerator:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.solution_path = []
    self.maze = [['#' for _ in range(width)] for _ in range(height)]
    
  def generate_maze(self):
    # Start from position (1, 1)
    start_x, start_y = 1, 1
    self.maze[start_y][start_x] = ' '
    
    # Stack for backtracking
    stack = [(start_x, start_y)]
    
    while stack:
      current_x, current_y = stack[-1]
      neighbors = self._get_unvisited_neighbors(current_x, current_y)
      
      if neighbors:
        next_x, next_y = random.choice(neighbors)
        # Remove wall between current and next cell
        wall_x = current_x + (next_x - current_x) // 2
        wall_y = current_y + (next_y - current_y) // 2
        self.maze[wall_y][wall_x] = ' '
        self.maze[next_y][next_x] = ' '
        stack.append((next_x, next_y))
      else:
        stack.pop()
  
  def _get_unvisited_neighbors(self, x, y):
    neighbors = []
    directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]  # Up, Right, Down, Left
    
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if (1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and 
        self.maze[ny][nx] == '#'):
        neighbors.append((nx, ny))
    
    return neighbors
  
  def set_start_end(self):
    # Set start point (top-left area)
    self.start = (1, 1)
    self.maze[1][1] = 'S'
    
    # Set end point (bottom-right area)
    self.end = (self.width - 2, self.height - 2)
    self.maze[self.height - 2][self.width - 2] = 'E'
  
  def print_maze(self):
    print("\nGenerated Maze:")
    print("S = Start, E = End, # = Wall, ' ' = Path")
    print("-" * (self.width * 2))
    
    for row in self.maze:
      print(''.join(row))
    
    print("-" * (self.width * 2))
    print(f"Start: {self.start}")
    print(f"End: {self.end}")

def main():
  print("Maze Generator")
  print("Choose difficulty:")
  print("1. Simple (15x15)")
  print("2. Medium (25x25)")
  print("3. Complex (35x35)")
  
  choice = input("Enter choice (1-3): ")
  
  if choice == '1':
    width, height = 15, 15
  elif choice == '2':
    width, height = 25, 25
  elif choice == '3':
    width, height = 35, 35
  else:
    print("Invalid choice, using medium difficulty")
    width, height = 25, 25
  
  # Ensure odd dimensions for proper maze generation
  if width % 2 == 0:
    width += 1
  if height % 2 == 0:
    height += 1
  
  maze_gen = MazeGenerator(width, height)
  maze_gen.generate_maze()
  maze_gen.set_start_end()
  maze_gen.print_maze()

if __name__ == "__main__":
  main()