"""
Main application for interactive maze generation and visualization.

This module provides a command-line interface for creating mazes with user-specified
dimensions and starting positions. It generates a maze using recursive backtracking
and saves a visual representation as a PNG image.

Usage:
    python3 main.py

The program will prompt for:
    - Maze dimensions (width and height)
    - Starting coordinates (x, y)
"""

from maze import Maze
from draw import draw_maze
import pandas as pd


def my_print(matrix):
    """
    Print a readable representation of a matrix using pandas DataFrame.

    This utility function formats numerical matrices in a readable table format
    with labeled rows and columns for easier analysis and debugging.

    Args:
        matrix (np.ndarray): The matrix to display.
    """
    labels = [str(x) for x in range(matrix.shape[0])]
    df = pd.DataFrame(matrix, columns=labels, index=labels)
    pd.set_option('display.max_rows', None)
    print(df.to_string())


def main():
    """
    Main function that handles user interaction and maze generation.

    This function:
    1. Prompts the user for maze dimensions with validation
    2. Prompts the user for starting coordinates with validation
    3. Creates a maze using the specified parameters
    4. Generates and saves a visual representation of the maze
    """
    # Get maze dimensions with input validation
    while True:
        try:
            dimensions = input('Enter maze dimensions separated by a space: ').split()
            dimension1, dimension2 = int(dimensions[0]), int(dimensions[1])
            if 0 < dimension1 and 0 < dimension2:
                break
            else:
                print("Maze dimensions cannot be 0.")
        except ValueError:
            print("Dimensions must be integers.")

    # Get starting coordinates with input validation
    while True:
        try:
            start = input('Enter x and y coordinates of the maze start separated by a space: ').split()
            start_x, start_y = int(start[0]), int(start[1])
            if 0 <= start_x < dimension1 and 0 <= start_y < dimension2:
                break
            else:
                print("Start coordinates should be inside the maze. Numbering is zero-based.")
        except ValueError:
            print("Start coordinates must be integers.")

    # Create and visualize the maze
    print(f"Generating {dimension1}x{dimension2} maze starting at ({start_x}, {start_y})...")
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    draw_maze(maze)
    print("Maze generated and saved as 'maze.png'")


if __name__ == "__main__":
    main()




