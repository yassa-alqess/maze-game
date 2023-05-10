class MazeUtil:
    def __init__(self, maze):
        self.maze = maze
    offsets = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
    }
    
    directions = list(offsets.values())
    
    @staticmethod
    def is_valid_pos(maze, pos) -> bool:
        row, col = pos
        if row >= 0 and row < len(maze.grid) and col >= 0 and col < len(maze.grid[0]) and maze.grid[row][col] not in maze.props.invalid_chars:
            return True
        return False
    
    def print_solved_maze(maze,path): #without overwriting the original maze
        solved_maze = maze.grid[:] #O(n^2)
        for row, col in path[1:-1]:
            solved_maze[row][col] = "O"
        for row in solved_maze:
            print("".join(row))

                
    