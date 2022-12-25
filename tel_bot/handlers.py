from aiogram import types, Dispatcher
import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start'])
    dp.register_message_handler(commands.exit, commands=['no'])
    dp.register_message_handler(commands.player_turn)