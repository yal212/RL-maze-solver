import numpy as np

from maze import Maze


def find_reachable_neighbors(maze, cell):
    neighbors = []
    for direction, (dx, dy) in maze.delta.items():
        if not cell.walls[direction]:
            neighbors.append(maze.cell_at(cell.x + dx, cell.y + dy))
    return neighbors


class Feasibility:
    def __init__(self, maze_):
        self.cells = maze_.maze_grid.shape[0] * maze_.maze_grid.shape[1]
        self.F_matrix = np.zeros(shape=[self.cells, self.cells], dtype=int)
        self.numbered_grid = np.arange(self.cells).reshape(
            (maze_.maze_grid.shape[0], maze_.maze_grid.shape[1]))
        self.get_neighbors(maze_)

    def get_neighbors(self, maze: Maze):
        for x in range(maze.nx):
            for y in range(maze.ny):
                cell_number = self.numbered_grid[x][y]
                neighbors = find_reachable_neighbors(
                    maze, maze.maze_grid[x][y])
                for neighbor in neighbors:
                    neighbor_number = self.numbered_grid[neighbor.x][neighbor.y]
                    self.F_matrix[cell_number][neighbor_number] = 1
                    self.F_matrix[neighbor_number][cell_number] = 1
