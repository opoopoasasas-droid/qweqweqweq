import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

API_TOKEN = "8332179689:AAHWtY_VwyBXBLHifOmj6m2DjBjixJCesKg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📢 Перейти на канал", url="https://t.me/+P0mtu8OihqhiNWM6"),
            InlineKeyboardButton(text="🛠 Поддержка", url="https://opoopoasasas-droid.github.io/waka/")
        ]
    ])

    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в магазин 🛍️ WakaTDK!\n"
        "Здесь вы найдете лучшие товары.\n\n"
        "Выберите действие ниже 👇",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
