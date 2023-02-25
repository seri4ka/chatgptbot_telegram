import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keys import api_key, tg_token

tg = tg_token
openai.api_key = api_key

bot = Bot(tg_token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model='text-davinci-003',
    prompt=message.text,
    temperature=0.3,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=['You:']
)


    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
