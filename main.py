
from aiogram.types import Message
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from parsing import shedules

BOT_TOKEN = "5335988030:AAENlU5sNbsQHcM1-6YaPiE0DVplGsUBvEE"
admin_id="749783684"

bot = Bot(token = BOT_TOKEN, parse_mode = "HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привіт {0.first_name}👋!\n\nЯ бот-помічник, створений аби допомогти ліцеїстам не губитися у розкладі занять📋\n\nОбери групу, в якій ти навчаєшся..📚'.format(message.from_user), reply_markup =nav.mainMenu)

@dp.message_handler()
async def menu (message:Message):
   if message.text == 'Слава Україні!':
       await bot.send_message(chat_id=message.from_user.id, text='Героям слава')

   elif message.text == 'I-21':
       await bot.send_message(chat_id=message.from_user.id, text='Чудово! Тепер обери підгрупу', reply_markup =nav.otherMenu)

   elif message.text == '1-а Підгрупа':
       await bot.send_message(chat_id=message.from_user.id, text="Обери день тижня",
                              reply_markup=nav.Shedule)

   elif message.text == '2-а Підгрупа':
       await bot.send_message(chat_id=message.from_user.id, text="Обери день тижня",
                              reply_markup=nav.Shedule2)
   elif message.text == 'Головне меню':
       await bot.send_message(message.from_user.id, 'Привіт {0.first_name}👋!\n\nЯ бот-помічник, створений аби допомогти ліцеїстам не губитися у розкладі занять📋\n\nОбери групу, в якій ти навчаєшся..📚'.format(message.from_user), reply_markup =nav.mainMenu)
   if message.text == 'Понеділок😴':
       mon = ' '
       for i in range(0,len(shedules[1][0])):
           mon = mon+f"{shedules[1][0][i]}\n"
       await bot.send_message(chat_id=message.from_user.id, text=mon,
                              reply_markup=nav.Shedule)
   elif message.text == 'Вівторок🌼':
       tue = ' '
       for i in range(0, len(shedules[1][1])):
           tue = tue + f"{shedules[1][1][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=tue,
                              reply_markup=nav.Shedule)
   elif message.text == 'Середа✨':
       wed = ' '
       for i in range(0, len(shedules[1][2])):
           wed = wed + f"{shedules[1][2][i]}\n"
       await bot.send_message(chat_id=message.from_user.id, text=wed,
                              reply_markup=nav.Shedule)
   elif message.text == 'Четвер🔬':
       thu = ' '
       for i in range(0, len(shedules[1][3])):
           thu = thu + f"{shedules[1][3][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=thu,
                              reply_markup=nav.Shedule)
   elif message.text == "П'ятниця📚":
       fri = ' '
       for i in range(0, len(shedules[1][4])):
           fri = fri + f"{shedules[1][4][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=fri,
                              reply_markup=nav.Shedule)
   elif message.text == 'Субота😎':
       sat = ' '
       for i in range(0, len(shedules[1][5])):
           sat = sat + f"{shedules[1][5][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=sat,
                              reply_markup=nav.Shedule)

   elif message.text == 'Понеділок😵‍💫':
       mon2 = ' '
       for i in range(0, len(shedules[0][0])):
           mon2 = mon2 + f"{shedules[0][0][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=mon2,
                              reply_markup=nav.Shedule2)
   elif message.text == 'Вівторок📖':
       tue2 = ' '
       for i in range(0, len(shedules[0][1])):
           tue2 = tue2 + f"{shedules[0][1][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=tue2,
                              reply_markup=nav.Shedule2)
   elif message.text == 'Середа🏝':
       wed2 = ' '
       for i in range(0, len(shedules[0][2])):
           wed2 = wed2 + f"{shedules[0][2][i]}\n"
       await bot.send_message(chat_id=message.from_user.id, text=wed2,
                              reply_markup=nav.Shedule2)
   elif message.text == 'Четвер🌺':
       thu2 = ' '
       for i in range(0, len(shedules[0][3])):
           thu2 = thu2 + f"{shedules[0][3][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=thu2,
                              reply_markup=nav.Shedule2)
   elif message.text == "П'ятниця🍹":
       fri2 = ' '
       for i in range(0, len(shedules[0][4])):
           fri2 = fri2 + f"{shedules[0][4][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=fri2,
                              reply_markup=nav.Shedule2)
   elif message.text == 'Субота🥰':
       sat2 = ' '
       for i in range(0, len(shedules[0][5])):
           sat2 = sat2 + f"{shedules[0][5][i]}\n"

       await bot.send_message(chat_id=message.from_user.id, text=sat2,
                              reply_markup=nav.Shedule2)

@dp.message_handler()
async def echo (message:Message):
    text = "Героям Слава!"
    if message.text == "Слава Україні!":
        await bot.send_message(chat_id="-1001609344671", text=text)
    else:
        print(message.text)


if __name__ == "__main__":

    executor.start_polling(dp)


