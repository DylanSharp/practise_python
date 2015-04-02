import random
import logging

logging.basicConfig(filename="maize_game.log", level = logging.DEBUG)

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    trap = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if trap == door or trap == start or door == start:
        return get_locations()

    return trap, door, start

def move_player(player, move):
    # player = x, y
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x, y

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # player = (x, y)

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    return moves

def draw_map():
    print (' ___ ___ ___')
    tile = "|{}"

    for index, cell in enumerate(CELLS):
        if index in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format("_X_"), end="")
            elif cell == trap:
                print(tile.format("_!_"), end="")

            else:
                print(tile.format("___"), end="")
        else:
                if cell == player:
                    print(tile.format("_X_|"))
                else:
                    print(tile.format("___|"))

trap, door, player = get_locations()
logging.info("Trap: {}, Door: {}, Player: {}".format(trap, door, player))

print("Welcome to the maze!")
print("Key: X → You")
print("Key: ! → Trap")
print("Move you player by typing 'up', 'down', 'left' or 'right'")
print("Escape the maze by finding the invisible door")

while True:
    moves = get_moves(player)
    draw_map()
    print("\nEnter QUIT to quit")

    move = input(">  ").upper()

    if move == "QUIT":
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("You can't move in that direction - there is a wall there!")
        continue

    if player == door:
        print("You escaped!!!")
        break
    elif player == trap:
        print("Uh - oh! You fell into the trap!")
        break
