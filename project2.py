import random

class MazeGenerator:
  """A class to generate random mazes using depth-first search algorithm."""
  
  def __init__(self, width, height):
    """
    Initialize the maze generator with specified dimensions.
    
    Args:
      width (int): Width of the maze
      height (int): Height of the maze
    """
    self.width = width
    self.height = height
    self.solution_path = []  # Will store the solution path (currently unused)
    # Initialize maze filled with walls ('#')
    self.maze = [['#' for _ in range(width)] for _ in range(height)]
  
  def generate_maze(self):
    """Generate a maze using depth-first search with backtracking."""
    # Start from position (1, 1) to ensure odd coordinates
    start_x, start_y = 1, 1
    # Mark starting position as empty space
    self.maze[start_y][start_x] = ' '
    
    # Stack for backtracking - stores coordinates of visited cells
    stack = [(start_x, start_y)]
    
    # Continue until all reachable cells are visited
    while stack:
      # Get current position (top of stack)
      current_x, current_y = stack[-1]
      # Find unvisited neighboring cells
      neighbors = self._get_unvisited_neighbors(current_x, current_y)
      
      if neighbors:
        # Randomly choose one unvisited neighbor
        next_x, next_y = random.choice(neighbors)
        # Calculate wall position between current and next cell
        wall_x = current_x + (next_x - current_x) // 2
        wall_y = current_y + (next_y - current_y) // 2
        # Remove wall between current and next cell
        self.maze[wall_y][wall_x] = ' '
        # Mark next cell as visited (empty space)
        self.maze[next_y][next_x] = ' '
        # Add next cell to stack for further exploration
        stack.append((next_x, next_y))
      else:
        # No unvisited neighbors - backtrack by removing current cell from stack
        stack.pop()
  
  def _get_unvisited_neighbors(self, x, y):
    """
    Find all unvisited neighboring cells that are 2 steps away.
    
    Args:
      x (int): Current x coordinate
      y (int): Current y coordinate
      
    Returns:
      list: List of tuples containing coordinates of unvisited neighbors
    """
    neighbors = []
    # Check 4 directions: Up, Right, Down, Left (2 steps away for proper maze generation)
    directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    
    for dx, dy in directions:
      # Calculate neighbor coordinates
      nx, ny = x + dx, y + dy
      # Check if neighbor is within bounds and unvisited (still a wall)
      if (1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and 
        self.maze[ny][nx] == '#'):
        neighbors.append((nx, ny))
    
    return neighbors
  
  def set_start_end(self):
    """Set the start and end points of the maze."""
    # Set start point at top-left area (1,1)
    self.start = (1, 1)
    self.maze[1][1] = 'S'
    
    # Set end point at bottom-right area
    self.end = (self.width - 2, self.height - 2)
    self.maze[self.height - 2][self.width - 2] = 'E'
  
  def print_maze(self):
    """Display the generated maze with formatting and legend."""
    print("\nGenerated Maze:")
    print("S = Start, E = End, # = Wall, ' ' = Path")
    print("-" * (self.width * 2))  # Top border
    
    # Print each row of the maze
    for row in self.maze:
      print(''.join(row))
    
    print("-" * (self.width * 2))  # Bottom border
    # Display start and end coordinates
    print(f"Start: {self.start}")
    print(f"End: {self.end}")

def main():
  """Main function to run the maze generator with user input."""
  print("Maze Generator")
  print("Choose difficulty:")
  print("1. Simple (15x15)")
  print("2. Medium (25x25)")
  print("3. Complex (35x35)")
  
  # Get user's difficulty choice
  choice = input("Enter choice (1-3): ")
  
  # Set maze dimensions based on user choice
  if choice == '1':
    width, height = 15, 15
  elif choice == '2':
    width, height = 25, 25
  elif choice == '3':
    width, height = 35, 35
  else:
    # Default to medium if invalid choice
    print("Invalid choice, using medium difficulty")
    width, height = 25, 25
  
  # Ensure odd dimensions for proper maze generation algorithm
  if width % 2 == 0:
    width += 1
  if height % 2 == 0:
    height += 1
  
  # Create maze generator instance and generate the maze
  maze_gen = MazeGenerator(width, height)
  maze_gen.generate_maze()     # Generate the maze structure
  maze_gen.set_start_end()     # Add start and end points
  maze_gen.print_maze()        # Display the final maze

# Entry point - run main function if script is executed directly
if __name__ == "__main__":
  main()