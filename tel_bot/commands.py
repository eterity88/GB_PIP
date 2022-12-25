from bot_config import dp, bot
from aiogram import types
import view, model
from aiogram import Bot, Dispatcher
from random import randint as rnd


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await model.set_game()
    await view.start_game(message)
    name = message.from_user.first_name
    await model.set_player_name(name)
    first_turn = rnd(1, 2)
    if first_turn == 1:
        await view.player_take(message)
    else:
        await bot_turn(message)


@dp.message_handler(commands='no')
async def exit(message: types.Message):
    await message.answer(f'Ну не сильно-то и хотелось')


@dp.message_handler()
async def player_turn(message: types.Message):
    game = await model.get_game()
    if game:
        if message.text == '/start':
            return
        else:
            if 0 < int(message.text) < 29:
                take_candy = int(message.text)
                await model.set_total(take_candy)
                name = await model.get_player_name()
                total = await model.get_total()
                if total > 0:
                    await view.player_info(message, name, take_candy, total, 'Я')
                    await bot_turn(message)
                else:
                    await view.win(message, 'Ты', take_candy)
                    await model.set_game()
            else:
                await view.error_take(message)

async def bot_turn(message):
    take_candy = await model.bot_take()
    await model.set_total(take_candy)
    name = await model.get_player_name()
    total = await model.get_total()
    if total > 0:
        await view.bot_info(message, 'Я', take_candy, total, name)
    else:
        await view.win(message, 'Я', take_candy)
        await model.set_game()