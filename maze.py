#!/usr/bin/env python

import random

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
    visit(maze, 0, 0, [])

def show_maze(maze):
    pass

def move(maze, x, y, stack, xoff, yoff, direction):
    if y + yoff < 0:
        return
    if x + xoff < 0:
        return
    if y + yoff > len(maze[x]):
        return
    if x + xoff > len(maze):
        return

    neighbour = maze[x + xoff][y + yoff]
    if neighbour[4]: # already visited?
        return

    # direction 1 is north, cell[0], etc.
    current[direction - 1] = True
    opposite_direction = ((direction + 2) % 4) + 1
    neighbour[opposite_direction] = True

    visit(maze, x + xoff, y + yoff, stack)

def visit(maze, x, y, stack):
    stack.append((x, y))
    current = maze[x][y]
    current[4] = True # now visited

    possibles_to_visit = [1, 2, 3, 4]
    possibles_to_visit.shuffle()

    for direction in possibles_to_visit:
        if direction == 1:
            move(maze, x, y, stack, 0, -1, direction)
        elif direction == 2:
            move(maze, x, y, stack, 1, 0, direction)
        elif direction == 3:
            move(maze, x, y, stack, 0, 1, direction)
        elif direction == 4:
            move(maze, x, y, stack, -1, 0, direction)

    stack.pop()

if __name__ == "__main__":
    maze = make_maze()
    carve_maze(maze)

