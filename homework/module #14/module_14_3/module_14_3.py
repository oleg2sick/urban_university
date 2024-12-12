from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

API = '75'
bot = Bot(token = API)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ручка', callback_data='product_buying')],
        [InlineKeyboardButton(text='Карандаш', callback_data='product_buying')],
        [InlineKeyboardButton(text='Кисть', callback_data='product_buying')],
        [InlineKeyboardButton(text='Фломастер', callback_data='product_buying')]
    ], resize_keyboard=True
)

new_kb = InlineKeyboardMarkup()
inline_button1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
inline_button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
new_kb.add(inline_button1)
new_kb.add(inline_button2)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('./pencil-500x421.png', 'rb') as img1:
        await message.answer_photo(img1, 'Название: ручка | Описание: синяя | Цена: 100')
    with open('./karandashi_206741254588e98_800x600.png', 'rb') as img2:
        await message.answer_photo(img2, 'Название: карандаш | Описание: мягкий | Цена: 200')
    with open('./a63d991d7677c1b03538189328a79b9d.png', 'rb') as img3:
        await message.answer_photo(img3, 'Название: кисть | Описание: тонкая | Цена: 300')
    with open('./1609316212_131432.png', 'rb') as img4:
        await message.answer_photo(img4, 'Название: фломастер | Описание: синий | Цена: 400')
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(text ='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = new_kb)


@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
                      'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
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
