"""
Cell module for maze generation.

This module defines the Cell class used to represent individual cells in a maze grid.
Each cell maintains information about its walls and can interact with neighboring cells.
"""


class Cell:
    """
    Represents a single cell in a maze grid.

    Each cell has four walls (North, South, East, West) and can be connected to
    neighboring cells by removing walls between them.

    Attributes:
        wall_pairs (dict): Mapping of wall directions to their opposites.
        x (int): X-coordinate of the cell in the grid.
        y (int): Y-coordinate of the cell in the grid.
        walls (dict): Dictionary indicating which walls are present (True) or removed (False).
        status (str): Special status of the cell ('Start', 'End', or None).
    """
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """
        Initialize a new cell at the given coordinates.

        Args:
            x (int): X-coordinate of the cell.
            y (int): Y-coordinate of the cell.
        """
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
        self.status = None

    def has_all_walls(self):
        """
        Check if the cell has all four walls intact.

        Returns:
            bool: True if all walls are present, False otherwise.
        """
        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        """
        Remove the wall between this cell and another cell.

        This method removes the specified wall from this cell and the corresponding
        opposite wall from the neighboring cell, creating a passage between them.

        Args:
            other (Cell): The neighboring cell to connect to.
            wall (str): The direction of the wall to remove ('N', 'S', 'E', or 'W').
        """
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False
