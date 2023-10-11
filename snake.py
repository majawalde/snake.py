import random
from uib_inf100_graphics.event_app import run_app
from snake_view import draw_board

def app_started(app):
    app.direction = "east"
    app.debug_mode = True
    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.snake_size = 3
    app.head_pos = (3,4)
    app.state = "mainmenu"
    app.timer_delay = 200

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...
    if app.debug_mode == False and app.state == "active":
        move_snake(app)

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...
    if app.state == "active":
        if event.key == "Up":
            app.direction = "north"
        elif event.key == "Down":
            app.direction = "south"
        elif event.key == "Left":
            app.direction = "west"
        elif event.key == "Right":
            app.direction = "east"
        elif event.key == "d":
            app.debug_mode = not app.debug_mode
        
        if event.key == "Space":
            move_snake(app)

def mouse_pressed(app, event):
    if app.state == "mainmenu":
        x0, y0, x1, y1 = app.width/4, app.height/2 - 25, 3*app.width/4, app.height/2 + 25
        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            app.state = "active"
            start_over(app)

    elif app.state == "gameover":
        x0, y0, x1, y1 = app.width/4, app.height/2 - 25, 3*app.width/4, app.height/2 + 25 

        x0_, y0_, x1_, y1_ = app.width/4 + 40, app.height/2 + 50, 3*app.width/4 - 40, app.height/2 + 75

        if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            start_over(app)

        elif x0_ <= event.x <= x1_ and y0_ <= event.y <= y1_:
            app.state = "mainmenu"
            app_started(app)


def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    ...
    if app.debug_mode:
        canvas.create_text(app.width / 2, 10, text=f"app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction='{app.direction}' app.state={app.state}")
    
    if app.state == "mainmenu":
        canvas.create_rectangle(0, 0, app.width, app.height, fill="black")
        
        canvas.create_text(app.width / 2, app.height / 3 - 20, text="Snake Game", font="Arial 36 bold")
        
        canvas.create_rectangle(app.width/4 + 40, app.height/2 - 25, 3*app.width/4 - 40, app.height/2 + 25, fill="gray", outline="black")
        
        canvas.create_text(app.width/2, app.height / 2, text="Click to Start", font="Arial 16 bold")

        instructions = [
            "Controls:",
            " - Use arrow keys to move the snake.",
            " - Eat apples to grow and earn points.",
            " - Press 'd' to turn on/off debug mode.",
            " - Don't hit the walls or yourself."
        ]

        instruction_start = app.height / 2 + 60
        for line in instructions:
            canvas.create_text(app.width / 2, instruction_start, text=line, fill="white", font="Arial 14")
            instruction_start += 20

    
    if not app.debug_mode and app.state == "active":
        canvas.create_text(app.width / 2, 10, text=f"Your score: {app.snake_size - 3}", font="Arial 16 bold")
    
    if app.state == "active":
        draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.debug_mode)
    
    elif app.state == "gameover":
        canvas.create_rectangle(0, 0, app.width, app.height, fill="black")

        canvas.create_text(app.width / 2, app.height / 4, text="Game Over!", font="Arial 24 bold")
        
        canvas.create_text(app.width / 2, app.height / 3, text=f"Your score: {app.snake_size - 3}", font="Arial 20")
        y0, y1 = app.height / 2 - 25, app.height / 2 + 25
        
        canvas.create_rectangle(app.width/4 + 40, y0, 3*app.width/4 - 40, y1, fill="green", outline="black")
        
        canvas.create_text(app.width/2, (y0 + y1) / 2, text="Restart Game", font="Arial 16 bold")

        y0, y1 = app.height / 2 +50, app.height / 2 + 75

        canvas.create_rectangle(app.width/4 + 40, y0, 3*app.width/4 - 40, y1, fill="gray", outline="black")
        
        canvas.create_text(app.width/2, (y0 + y1) / 2, text="Return to Main Menu", font="Arial 16 bold")


def move_snake(app):
  updated_head_pos = get_next_head_position(app.head_pos, app.direction)
  updated_row, updated_col = updated_head_pos

  if not is_legal_move(updated_head_pos, app.board):
      app.state = "gameover"
      return

  if app.board[updated_row][updated_col] == -1:
      app.snake_size += 1
      add_apple_at_random_location(app.board)

  else:
      subtract_one_from_all_positives(app.board)

  app.head_pos = updated_head_pos
  app.board[updated_row][updated_col] = app.snake_size


def get_next_head_position(head_pos, direction):
    row, col = head_pos

    if direction == "north":
        return(row-1, col)
    elif direction == "east":
        return (row, col+1)
    elif direction == "south":
        return (row+1, col)
    elif direction == "west":
        return (row, col-1)


def subtract_one_from_all_positives(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 0:
                grid[row][col] -= 1


def add_apple_at_random_location(grid):
    available_locations = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                available_locations.append((row,col))
    
    if available_locations:
        a, b = random.choice(available_locations)
        grid[a][b] = -1


def is_legal_move(pos,board):
    row, col = pos
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] <= 0:
        return True
    else:
        return False


def start_over(app):
    app.direction = "east"
    app.debug_mode = True
    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.snake_size = 3
    app.head_pos = (3,4)
    app.state = "active"
    app.timer_delay = 200


run_app(width=500, height=400, title="Snake")


