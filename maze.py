"""
Maze generation module using recursive backtracking algorithm.

This module implements maze generation using the recursive backtracking algorithm,
which creates perfect mazes (mazes with exactly one path between any two points).
"""

import random
import numpy as np
from cell import Cell


class Maze:
    """
    Generates and manages maze structures using recursive backtracking.

    The Maze class creates a perfect maze where there is exactly one path between
    any two points. It uses a recursive backtracking algorithm to carve passages
    through a grid of cells.

    Attributes:
        delta (dict): Direction vectors for movement (N, S, E, W).
        nx (int): Width of the maze (number of columns).
        ny (int): Height of the maze (number of rows).
        maze_grid (np.ndarray): 2D array of Cell objects representing the maze.
        end (list): Coordinates [x, y] of the maze exit point.
    """
    delta = {'N': (0, -1),
             'S': (0, 1),
             'W': (-1, 0),
             'E': (1, 0)}

    def __init__(self, nx, ny, start_):
        """
        Initialize and generate a new maze.

        Args:
            nx (int): Width of the maze (number of columns).
            ny (int): Height of the maze (number of rows).
            start_ (list): Starting coordinates [x, y] for maze generation.
        """
        self.end = None
        self.nx, self.ny = nx, ny
        self.maze_grid = np.array(
            [[Cell(x, y) for y in range(ny)] for x in range(nx)])
        self.__make_maze(start_)

    def cell_at(self, x, y):
        """
        Get the cell at the specified coordinates.

        Args:
            x (int): X-coordinate of the cell.
            y (int): Y-coordinate of the cell.

        Returns:
            Cell: The cell object at the given coordinates.
        """
        return self.maze_grid[x][y]

    def find_valid_neighbors(self, cell):
        """
        Find all valid neighboring cells that can be visited.

        A valid neighbor is within the maze boundaries and has all walls intact
        (hasn't been visited yet during maze generation).

        Args:
            cell (Cell): The current cell to find neighbors for.

        Returns:
            list: List of tuples (direction, neighbor_cell) for valid neighbors.
        """
        neighbors = []
        for direction, (dx, dy) in self.delta.items():
            neighbor_x, neighbor_y = cell.x + dx, cell.y + dy
            if (0 <= neighbor_x < self.nx) and (0 <= neighbor_y < self.ny):
                neighbor = self.cell_at(neighbor_x, neighbor_y)
                if neighbor.has_all_walls():
                    neighbors.append((direction, neighbor))
        return neighbors

    def __make_maze(self, start_coords):
        """
        Generate the maze using recursive backtracking algorithm.

        This private method implements the recursive backtracking algorithm to create
        a perfect maze. It ensures that the start and end points are different by
        regenerating the maze if they coincide.

        The algorithm works by:
        1. Starting from the given coordinates
        2. Randomly selecting unvisited neighbors
        3. Carving passages by removing walls
        4. Backtracking when no unvisited neighbors are available
        5. Continuing until all cells are visited

        Args:
            start_coords (list): Starting coordinates [x, y] for maze generation.
        """
        while True:
            n = self.nx * self.ny
            cell_stack = []
            current_cell = self.cell_at(start_coords[0], start_coords[1])
            current_cell.status = 'Start'
            n_visited = 1

            while n_visited < n:
                neighbors = self.find_valid_neighbors(current_cell)

                if not neighbors:
                    # Backtrack to previous cell
                    current_cell = cell_stack.pop()
                    continue

                # Choose random neighbor and carve passage
                direction, next_cell = random.choice(neighbors)
                current_cell.knock_down_wall(next_cell, direction)
                cell_stack.append(current_cell)
                current_cell = next_cell
                n_visited += 1

                # Mark the last visited cell as the end
                if n_visited == n:
                    current_cell.status = 'End'
                    self.end = [current_cell.x, current_cell.y]

            # Ensure start and end are different points
            if self.end != start_coords:
                break
