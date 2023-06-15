#import aiogram
from aiogram import Bot, Dispatcher, executor, types

bot = Bot('5635058672:AAFtSvfzcqRkY4BUCGPvAix_rDoq-8-G7G4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello')
    await message.answer('Hello')


@dp.message_handler()
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://itproger.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


executor.start_polling(dp)