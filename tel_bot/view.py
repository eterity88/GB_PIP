from bot_config import bot

total = 150


async def start_game(message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Давай сыграем в игру с\n'
                                                 f'конфетами. Правила такие: на столе лежит 150 \n'
                                                 f'конфет. Ходим по очереди. Первый ход определяется\n'
                                                 f'жеребьёвкой. За один ход можно забрать не более  28 конфет.\n'
                                                 f'Выиграл тот, кто забирает конфеты последним.')


async def player_take(message):
    global total
    await bot.send_message(message.from_user.id, f'Твой ход! Сейчас на столе {total} конфет.\n')


async def player_info(message, name1, take_candy, total, name2):
    await bot.send_message(message.from_user.id, f'Ты взял {take_candy} конфет. На столе осталось\n'
                                                 f'{total} конфет. Теперь я хожу!')


async def bot_info(message, name1, take_candy, total, name2):
    await bot.send_message(message.from_user.id, f'Я взял {take_candy} конфет. На столе осталось\n'
                                                 f'{total} конфет. Твой ход!')


async def win(message, name, take_candy):
    await bot.send_message(message.from_user.id, f'{name} взял {take_candy} конфет и победил! Если Хочешь сыграть еще раз?\n'
                                                 f'/start /no')


async def error_take(message):
    await bot.send_message(message.from_user.id, f'Ну иы и жадина!Бери не больше 28 конфет')