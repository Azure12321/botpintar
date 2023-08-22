# Telegram Bot OpenAI ChatGPT version Python by Wannazid
import openai
from aiogram import Bot, Dispatcher, types, executor

bot_tkn = '6536595310:AAEEBRUZoB5edG4xexWD8VZUCQVGeGFpC28'
openai.api_key = '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'

bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)
	
@dp.message_handler(lambda message: message.text)
async def ai_answer(message: types.Message):
	respon = openai.Completion.create(model='text-davinci-003', prompt=message.text, temperature=0, max_tokens=1000)
	parse = respon['choices'][0]['text']
	await message.reply(parse)
	
print('Bot berjalan !')	
executor.start_polling(dp)
