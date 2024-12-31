from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

bot = Bot(token='7715430802:AAF6c0T5_9iUPWFCTSk3WYoJiQYqsSrqGnE')
dispatcher = Dispatcher()


@dispatcher.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer("I'm echo Bot! Write something!")


@dispatcher.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer("Write something and I'll repeat that!")


@dispatcher.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Type is not supported')


if __name__ == '__main__':
    dispatcher.run_polling(bot)