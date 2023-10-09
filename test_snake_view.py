from uib_inf100_graphics.simple import canvas, display
from snake_view import draw_board

test_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9,10,11, 0,-1, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 6, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 1, 2, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

draw_board(canvas, 25, 25, 375, 375, test_board, True)
display(canvas)
