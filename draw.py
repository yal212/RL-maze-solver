from cell import Cell
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Some predefined values for the visualization
margin = 80
cell_side = 100
line_thickness = 10


class PathNotFound(Exception):
    """Exception raised when maze path is not found."""

    def __init__(self, message="Maze path was not found, unable to draw a gif. Please try different parameters."):
        self.message = message
        super().__init__(self.message)


def draw_cell(cell, image, color="black", count=0, wide=5, method="grid"):
    # Cell coordinates on the image calculated from its (x, y) coordinates,
    # cell side length (100 pt), image margin (90 pt) and line thickness (10 pt).
    x = margin + line_thickness + cell.x * cell_side
    y = margin + line_thickness + cell.y * cell_side

    lines = [(x - cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y - cell_side / 2)], \
        [(x - cell_side / 2, y + cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
        [(x + cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
        [(x - cell_side / 2, y - cell_side / 2),
         (x - cell_side / 2, y + cell_side / 2)]

    shown_walls = [i for (i, v) in zip(lines, cell.walls.values()) if v]
    for wall in shown_walls:
        image.line(wall, fill=color, width=wide)
    if cell.status == 'Start' or cell.status == 'End':
        try:
            font = ImageFont.truetype("Arial Unicode.ttf", 18)
            image.text((x - 25, y - 10), cell.status.upper(),
                       (255, 0, 0), font=font)
        except OSError:
            font = ImageFont.load_default()
            image.text((x - 25, y - 10), cell.status.upper(),
                       (255, 0, 0), font=font)
    else:
        if method == "grid":
            try:
                font = ImageFont.truetype("Arial Unicode.ttf", 18)
                image.text((x - 35, y - 35), str(count),
                           fill="#D3D3D3", font=font)
            except OSError:
                font = ImageFont.load_default()
                image.text((x - 35, y - 35), str(count),
                           fill="#D3D3D3", font=font)


def draw_grid(image, x_cells, y_cells):
    cells_ = {}
    count = 0
    for i in range(x_cells):
        for j in range(y_cells):
            cell_name = count
            count += 1
            cells_[cell_name] = Cell(i, j)
    for num, cel in cells_.items():
        draw_cell(cel, image, "lightgray", num)


def draw_image(maze_img, cells):
    draw_grid(maze_img, cells.shape[0], cells.shape[1])
    for cell in cells.flatten():
        draw_cell(cell, maze_img, method="not_grid")


def draw_agent(cell, image, color="blue"):
    x = margin + line_thickness + cell.x * cell_side
    y = margin + line_thickness + cell.y * cell_side
    image.ellipse((x - cell_side / 3, y - cell_side / 3, x +
                  cell_side / 3, y + cell_side / 3), fill=color)


def make_movie(maze, feasibility, path, filename="maze_path.gif"):
    """Function for drawing a visualization of how the agent moves through the labyrinth."""
    images = []
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)

    if 'break' in path:
        raise PathNotFound

    for position in path:
        ind1 = np.where(feasibility.numbered_grid == position)[0][0]
        ind2 = np.where(feasibility.numbered_grid == position)[1][0]
        cell = maze.maze_grid[ind1, ind2]

        im = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        draw_image(draw, maze.maze_grid)
        draw_agent(cell, draw)
        images.append(im)

    images[0].save(filename, save_all=True, append_images=images[1:],
                   optimize=False, duration=400, loop=0)


def draw_maze(maze, filename="maze.png"):
    """Function for drawing a static image of the maze."""
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (width, height), (255, 255, 255))
    cells = maze.maze_grid
    maze_img = ImageDraw.Draw(img)
    draw_grid(maze_img, cells.shape[0], cells.shape[1])
    for cell in cells.flatten():
        draw_cell(cell, maze_img, method="not_grid")
    img.save(filename)
