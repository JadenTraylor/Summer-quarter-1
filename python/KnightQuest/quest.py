import pgzrun
# Game grid settings
GRID_WIDTH = 16   # Number of squares wide
GRID_HEIGHT = 12  # Number of squares tall
GRID_SIZE = 50
# Window size
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
# Map layout — all rows must be exactly 16 characters
MAP = [
    "WWWWWWWWWWWWWWWW",
    "W              W",
    "W              W",
    "W   W    KG    W",
    "W   WWWWWWWWWW W",
    "W              W",
    "W   WWWWWWWWW  W",
    "W      P    W  W",
    "W              W",
    "W              W",
    "W              D",
    "WWWWWWWWWWWWWWWW"
]
# Convert grid (x, y) to screen pixel coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# Draw floor tiles
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))

##########################
# This function takes in an actor as an argument &
# returns the postion of the actor on the grid
def GetActorGridPos(actor):
    return(round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
##########################

# Setup player
def SetupGame():
    global player
    player = Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            row = MAP[y].ljust(GRID_WIDTH)  # pad in case row is short
            if row[x].upper() == "P":
                player.pos = GetScreenCoords(x, y)
# Draw walls and doors
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            pos = GetScreenCoords(x, y)
            if square == "W":
                screen.blit("wall", pos)
            elif square == "D":
                screen.blit("door", pos)
            # You can add more tile types like "K", "G" here later

##########################
def DrawActors():
    player.Draw()
##########################

# Main draw loop
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    player.draw()

##########################
def MovePlayer(dx, dy):
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        return
    player.pos = GetScreenCoords(x, y)
##########################

##########################
# This Function gets a key from the user and moves the player based on the input 
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0) # Player mover left one on the grid
    elif key == keys.UP:
        MovePlayer(0, -1) # Player mover up one on the grid
    elif key == keys.RIGHT:
        MovePlayer(1, 0) # Player mover right one on the grid
    elif key == keys.DOWN:
        MovePlayer(0, 1) # Player mover down one on the grid
##########################
# Setup and run
SetupGame()
pgzrun.go()


