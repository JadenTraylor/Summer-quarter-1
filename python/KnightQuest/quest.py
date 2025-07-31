########## 1.3 ##########
import pgzrun
import random

GRID_WIDTH = 20
GRID_HEIGHT = 15
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.6
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
PLAYER_MOVE_INTERVAL = 0.1
BACKGROUND_SPEED = 12345

########## 1.5 ##########
MAP = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W  G   K     W   G  W",
    "W WWWWW WWW WWWWW WW",
    "W W   W   W     W  W",
    "W W W WWW W WWW W WW",
    "W W W   W   W W W  W",
    "W WWWWW WWWWW W WW W",
    "W   G     P    W   W",
    "W WWWWW WWWWW WWWWWW",
    "W   K   W   W     KW",
    "WWW WWWWW W WWWWW WW",
    "W   W   K W     G  W",
    "W WWW W WWWWWWWWW WW",
    "W  G           K  DW",
    "WWWWWWWWWWWWWWWWWWWW"
]

########## 1.4 ##########
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def DrawBackground():
    random.seed(BACKGROUND_SPEED)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if x % 2 == y % 2:
                screen.blit("floor1", GetScreenCoords(x, y))
            else:
                screen.blit("floor2", GetScreenCoords(x, y))

            n = random.randint(0, 99)
            if n < 5:
                screen.blit("crack1", GetScreenCoords(x, y))
            elif n < 10:
                screen.blit("crack2", GetScreenCoords(x, y))  # Assuming you have crack2

def SetupGame():
    global player, keysToCollect, gameOver, guards, playerWon

    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False
    playerWon = False

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == 'P':
                player.pos = GetScreenCoords(x, y)
            elif square == 'K':
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == 'G':
                guard = Actor("guard", anchor=("left", "top"), pos=GetScreenCoords(x, y))
                guards.append(guard)

def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()

def on_key_up(key):
    if key == keys.SPACE and gameOver:
        SetupGame()

def MovePlayer(dx, dy):
    global gameOver, playerWon
    if gameOver:
        return

    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy

    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) > 0:
            return
        else:
            gameOver = True
            playerWon = True

    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break

    animate(player, pos=GetScreenCoords(x, y), duration=PLAYER_MOVE_INTERVAL)

def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

def DrawGameOver():
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    screen.draw.text("Game Over", midbottom=screenMiddle,
                     fontsize=GRID_SIZE * 2, color="cyan", owidth=1)

    if playerWon:
        screen.draw.text("YOU WIN!", midtop=screenMiddle,
                         fontsize=GRID_SIZE, color="green", owidth=1)
    else:
        screen.draw.text("YOU LOSE!", midtop=screenMiddle,
                         fontsize=GRID_SIZE, color="red", owidth=1)

def MoveGuard(guard):
    global gameOver
    if gameOver:
        return

    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)

    if playerX > guardX and MAP[guardY][guardX + 1] != 'W':
        guardX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != 'W':
        guardX -= 1

    if playerY > guardY and MAP[guardY + 1][guardX] != 'W':
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != 'W':
        guardY -= 1

    animate(guard, pos=GetScreenCoords(guardX, guardY), duration=GUARDMOVEINTERVAL)

    if guardX == playerX and guardY == playerY:
        gameOver = True

def MoveGuards():
    for guard in guards:
        MoveGuard(guard)

# Run the game
SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()