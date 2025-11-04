from maze import Maze
from convert import Feasibility
from draw import draw_maze
import pandas as pd


# This function is needed to print a readable representation of the feasibility matrix.
def my_print(matrix):
    labels = [str(x) for x in range(matrix.shape[0])]
    df = pd.DataFrame(matrix, columns=labels, index=labels)
    pd.set_option('display.max_rows', None)
    print(df.to_string())


if __name__ == "__main__":
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

    while True:
        try:
            start = input('Enter x and y coordinates of the maze start separated by a space: ').split()
            start_x, start_y = int(start[0]), int(start[1])
            if start_x <= dimension1 and start_y <= dimension2:
                break
            else:
                print("Start coordinates should be inside the maze. Numbering is zero-based.")
        except ValueError:
            print("Start coordinates must be integers.")

    # Create the Maze
    maze = Maze(dimension1, dimension2, [start_x, start_y])

    # This will draw the maze and save it to the file maze.png
    draw_maze(maze)




