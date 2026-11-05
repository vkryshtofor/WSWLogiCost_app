import asyncio
import json
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "9078489050:AAFY85VRntNZ01JLcpZWt04r7J1sri7j42M"
WEBAPP_URL = "https://vkryshtofor.github.io/WSWLogiCost_app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🧮 Відкрити калькулятор", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await message.answer(
        "Вітаю! Натисніть кнопку нижче, щоб відкрити калькулятор собівартості рейсу:", 
        reply_markup=kb
    )

# Обробка даних, надісланих з Mini App через tg.sendData()
@dp.message(F.web_app_data)
async def handle_webapp_data(message: Message):
    data = json.loads(message.web_app_data.data)
    
    response = (
        f"📊 **Розрахунок рейсу ({data['distance']} км):**\n\n"
        f"• Собівартість 1 км: `{data['costPerKm']} €`\n"
        f"• Рекомендована ставка 1 км: `{data['ratePerKm']} €`\n"
        f"💰 **Загальна вартість рейсу:** `{data['totalPrice']} €`"
    )
    await message.answer(response, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
