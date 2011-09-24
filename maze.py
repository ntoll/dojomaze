#!/usr/bin/env python



def make_maze(width=10, height=10):
    maze = []
    for i in range(width):
        column = []
        maze.append(column)
        for j in range(height):
            # top, right, bottom, left, visited flags
            newNode = (False, False, False, False, False)
            column.append(newNode)
    return maze

def carve_maze(maze):
    pass

def show_maze(maze):
    pass

if __name__ == "__main__":
    make_maze()

