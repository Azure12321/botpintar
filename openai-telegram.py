# Telegram Bot OpenAI ChatGPT version Python by Wannazid
import openai
from aiogram import Bot, Dispatcher, types, executor

bot_tkn = '6257940664:AAFVnJUI5UcDC7mym3bwzb8a5h3GI1kFHBw'
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
