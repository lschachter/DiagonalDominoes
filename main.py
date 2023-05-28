from random import randrange

from graphics import GraphWin, Text, Point, color_rgb, Rectangle
from grid import Grid
from button import Button
from playerCollection import PlayerCollection
from gamePlay import GamePlay
from tile import Tile


def main():
    # creates the splash screen
    window = GraphWin("Diagonal Dominoes", 1000, 600)
    window.setCoords(0, 600, 1000, 0)
    window.setBackground("gray")
    text = Text(Point(500, 120), "Diagonal Dominoes")
    text.draw(window)
    text.setSize(36)
    gameB = Button(
        window, Point(350, 300), 200, 150, "Play Game", color="black", textColor="white"
    )
    gameB.setTextSize(24)
    instB = Button(
        window,
        Point(650, 300),
        200,
        150,
        "Instructions",
        color="black",
        textColor="white",
    )
    instB.setTextSize(24)
    x = 100
    y = 500
    for _ in range(6):
        c1 = color_rgb(randrange(255), randrange(255), randrange(255))
        c2 = color_rgb(randrange(255), randrange(255), randrange(255))
        tile = Tile(c1, c2, window)
        tile.drawTile(Point(x, y), Point(x + 50, y))
        x += 150
    pt = window.getMouse()
    # until the playgame button is clicked, gets new clicks and/or displays
    # instructions
    while not gameB.isClicked(pt):
        if instB.isClicked(pt):
            instRect = Rectangle(Point(245, 100), Point(755, 375))
            instRect.setFill("white")
            instRect.draw(window)
            instMess = Text(
                Point(530, 230),
                "In this two-person game, each player gets five tiles, each with\
            \ntwo colors (as below). The first tile chosen is placed \
            \nhorizontally on the bottom-left corner of the board.\
            \nThe next player must place a tile one slot above it and one\
            \nto the right, matching the left-most color of their new tile to\
            \nthe right-most color of the last tile placed on the board. The\
            \ngame ends when either a player has run out of tiles (they win),\
            \nor has no more valid moves to make (they lose). Give it a try\
            \nand it will start to make sense. Have fun!\n\n(click to return)",
            )
            instMess.draw(window)
            instMess.setSize(18)
            window.getMouse()
            instRect.undraw()
            instMess.undraw()
        pt = window.getMouse()

    # creates the game grid
    gameB.die()
    instB.die()
    grid = Grid(window)
    window.setBackground("gray")
    grid.drawGrid()
    quitB = grid.getQuitB()

    # sets up each player collection
    player1 = PlayerCollection(window, Point(120, 50), 1)
    player2 = PlayerCollection(window, Point(880, 50), 2)
    player1.displayTiles()
    player1.humanSetup()
    player2.displayTiles()

    # starts the game
    game = GamePlay(window, grid, player1, player2, quitB)
    game.playGame()


main()
