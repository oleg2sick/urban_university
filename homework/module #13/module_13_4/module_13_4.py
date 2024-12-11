from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

API = '123'
bot = Bot(token = API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Введите слово Calories, '
                         'чтобы узнать подходящий для Вас калораж')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    date = await state.get_data()
    result = 10*int(date['weight']) + 6.25*int(date['growth']) + 5*int(date['age']) + 5
    await message.answer(f'Калораж для Вас: {result}')
    await state.finish()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
