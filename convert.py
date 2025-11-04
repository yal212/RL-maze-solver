"""
Maze to feasibility matrix conversion module.

This module converts maze structures into mathematical representations suitable
for reinforcement learning algorithms. It creates feasibility matrices that
encode the connectivity between maze cells.
"""

import numpy as np
from maze import Maze


def find_reachable_neighbors(maze, cell):
    """
    Find all cells reachable from the given cell without crossing walls.

    Args:
        maze (Maze): The maze object containing the grid structure.
        cell (Cell): The cell to find neighbors for.

    Returns:
        list: List of Cell objects that are directly reachable from the given cell.
    """
    neighbors = []
    for direction, (dx, dy) in maze.delta.items():
        if not cell.walls[direction]:
            neighbors.append(maze.cell_at(cell.x + dx, cell.y + dy))
    return neighbors


class Feasibility:
    """
    Converts maze structure into a feasibility matrix for reinforcement learning.

    The feasibility matrix is a mathematical representation where each cell in the
    maze is assigned a unique number, and the matrix indicates which cells are
    directly connected (reachable without crossing walls).

    Attributes:
        cells (int): Total number of cells in the maze.
        F_matrix (np.ndarray): Binary matrix indicating cell connectivity.
        numbered_grid (np.ndarray): 2D array mapping cell coordinates to unique numbers.
    """

    def __init__(self, maze_):
        """
        Initialize the feasibility matrix from a maze.

        Args:
            maze_ (Maze): The maze object to convert into a feasibility matrix.
        """
        self.cells = maze_.maze_grid.shape[0] * maze_.maze_grid.shape[1]
        self.F_matrix = np.zeros(shape=[self.cells, self.cells], dtype=int)
        self.numbered_grid = np.arange(self.cells).reshape(
            (maze_.maze_grid.shape[0], maze_.maze_grid.shape[1]))
        self.get_neighbors(maze_)

    def get_neighbors(self, maze: Maze):
        """
        Populate the feasibility matrix with cell connectivity information.

        This method iterates through all cells in the maze and marks connected
        cells in the feasibility matrix. The matrix is symmetric since if cell A
        can reach cell B, then cell B can also reach cell A.

        Args:
            maze (Maze): The maze object to analyze for connectivity.
        """
        for x in range(maze.nx):
            for y in range(maze.ny):
                cell_number = self.numbered_grid[x][y]
                neighbors = find_reachable_neighbors(
                    maze, maze.maze_grid[x][y])
                for neighbor in neighbors:
                    neighbor_number = self.numbered_grid[neighbor.x][neighbor.y]
                    self.F_matrix[cell_number][neighbor_number] = 1
                    self.F_matrix[neighbor_number][cell_number] = 1
