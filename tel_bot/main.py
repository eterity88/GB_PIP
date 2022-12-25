from aiogram.utils import executor
from bot_config import dp
import handlers


async def bot_start(_):
    print('Бот запущен')


handlers.registred_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=bot_start)