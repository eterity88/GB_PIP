from random import randint as rnd

game = False
player_name = ''
total = 150


async def set_game():
    global game
    global player_name
    global total
    if game == False:
        game = True
    else:
        player_name = ''
        total = 150
        game = False


async def get_game():
    global game
    return game


async def set_player_name(name):
    global player_name
    player_name = name


async def get_player_name():
    global player_name
    return player_name


async def bot_take():
    global total
    take_candy = total % 29 if total % 29 != 0 else rnd(1, 28)
    return take_candy


async def set_total(take_candy):
    global total
    total -= take_candy


async def get_total():
    global total
    return total