#!/usr/bin/env python

import random

def make_maze(width=10, height=10, random_maze=False):
    maze = []
    for i in range(width):
        column = []
        maze.append(column)
        for j in range(height):
            if random_maze:
                top = random.randrange(0,2) == 0
                right = random.randrange(0,2) == 0
                bottom = random.randrange(0,2) == 0
                left = random.randrange(0,2) == 0
                visited = random.randrange(0,2) == 0
                newNode = [top, right, bottom, left, visited]
            else:
                # top, right, bottom, left, visited flags
                newNode = [False, False, False, False, False]
            column.append(newNode)
    return maze


def carve_maze(maze):
    visit(maze, 0, 0, [])

def show_maze(maze):
    for row in maze:
        # for each row, print two lines
        # first line is +-+- ...
        line1 = []
        for node in row:
            line1.append('+')
            if node[0]:
                line1.append(' ')
            else:
                line1.append('-')
        line1.append('+')
        # line 2 is | | |
        line2 = []
        for node in row:
            if node[3]:
                line2.append(' ')
            else:
                line2.append('|')
            line2.append(' ')
        if row[-1][1]:
            line2.append(' ')
        else:
            line2.append('|')
        print ''.join(line1)
        print ''.join(line2)
    lastline = []
    for node in maze[-1]:
        lastline.append('+')
        if node[2]:
            lastline.append(' ')
        else:
            lastline.append('-')
    lastline.append('+')
    print ''.join(lastline)

    print ''

def move(maze, x, y, stack, xoff, yoff, direction):
    if y + yoff < 0:
        return
    if x + xoff < 0:
        return
    if y + yoff >= len(maze[x]):
        return
    if x + xoff >= len(maze):
        return

    current = maze[x][y]
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
    random.shuffle(possibles_to_visit)

    for direction in possibles_to_visit:
        if direction == 1:
            move(maze, x, y, stack, 0, -1, direction)
        elif direction == 2:
            move(maze, x, y, stack, 1, 0, direction)
        elif direction == 3:
            move(maze, x, y, stack, 0, 1, direction)
        elif direction == 4:
            move(maze, x, y, stack, -1, 0, direction)

    show_maze(maze)
    stack.pop()

if __name__ == "__main__":
    maze = make_maze(random_maze=True)
    carve_maze(maze)

