from uib_inf100_graphics.simple import canvas, display

def draw_board(canvas, x1, y1, x2, y2, board, debug_mode):
    #canvas is the canvas to draw on
    #x1 and y 1 are the coordinates of the top left corner of the board
    #x2 and y2 are the coordinates of the bottom right corner of the board
    #board is a 2D list of numbers representing the board.
    #debug_mode is a boolean representing whether debug mode is on or not

    #draw the board
    num_rows = len(board)
    num_cols = len(board[0])

    cell_width = (x2 - x1) / num_cols
    cell_height = (y2 - y1) / num_rows

    for row in range(num_rows):
        for col in range(num_cols):
            left = x1 + col * cell_width
            top = y1 + row * cell_height
            right = left + cell_width
            bottom = top + cell_height

            if board[row][col] == 0:
                color = "lightgray"
            elif board[row][col] > 0:
                color = "orange"
            else:
                color = "cyan"
            
            canvas.create_rectangle(left, top, right, bottom, fill=color)

            if debug_mode:
                # Skriv ut tekst i ruten med posisjon og tallverdi
                canvas.create_text(left + 5, top + 5, anchor="nw", text=f"{row},{col}\n{board[row][col]}")

