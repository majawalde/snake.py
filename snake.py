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

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...
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

def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    ...
    if app.debug_mode:
        canvas.create_text(app.width / 2, 10, text=f"app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction='{app.direction}'")
    
    draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.debug_mode)

def move_snake(app):

    head_row, head_col = app.head_pos  # Lagre slangens nåværende hodeposisjon

    if app.direction == "north":
        head_row -= 1
    elif app.direction == "south":
        head_row += 1
    elif app.direction == "west":
        head_col -= 1
    elif app.direction == "east":
        head_col += 1

    app.head_pos = (head_row, head_col)  # Oppdater slangens hodeposisjon

    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if app.board[row][col] > 0:
                app.board[row][col] -= 1

run_app(width=500, height=400, title="Snake")
