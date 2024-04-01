import os
import time
from termcolor import colored

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.1
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

    def drawSquare(self, size):
        for _ in range(0,size):
            scribe.right()
        for _ in range(0,size):
            scribe.down()
        for _ in range(0,size):
            scribe.left()
        for _ in range(0,size):
            scribe.up()

canvas = Canvas(30,30)
scribe = TerminalScribe(canvas)
scribe.drawSquare(5)


def inputDrawing():
    go = 1
    while go == 1:
        print('Please enter the size of the square canvas: [TYPE AN INTEGER]')
        size = int(input())
        if size != None:
            go = 0
    go = 1
    canvas = Canvas(size, size)
    scribe = TerminalScribe(canvas)
    print('Press any one of WASD keys, then enter to move the cursor. E will end the program')
    while go == 1:
        key = input()
        if key == 'w':
            scribe.up()
        if key == 's':
            scribe.down()
        if key == 'a':
            scribe.left()
        if key == 'd':
            scribe.right()
        if key == 'e':
            go = 0

inputDrawing()


