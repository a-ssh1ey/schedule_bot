from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Головне меню')
#---Main Menu---

btnRandom = KeyboardButton('Слава Україні!')
btnOther = KeyboardButton('I-21')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)

# --- Other Menu ---
btnInfo = KeyboardButton('1-а Підгрупа')
btnMoney = KeyboardButton('2-а Підгрупа')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
#--- Shedule1 ----
btnMonday = KeyboardButton('Понеділок😴')
btnTuesday = KeyboardButton('Вівторок🌼')
btnWednesday = KeyboardButton('Середа✨')
btnThursday = KeyboardButton('Четвер🔬')
btnFriday = KeyboardButton("П'ятниця📚")
btnSaturday = KeyboardButton('Субота😎')
Shedule = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMonday,btnTuesday,btnWednesday,btnThursday,btnFriday,btnSaturday, btnMain)
#--- Shedule2 ----
btnMonday2 = KeyboardButton('Понеділок😵‍💫')
btnTuesday2 = KeyboardButton('Вівторок📖')
btnWednesday2 = KeyboardButton('Середа🏝')
btnThursday2 = KeyboardButton('Четвер🌺')
btnFriday2 = KeyboardButton("П'ятниця🍹")
btnSaturday2 = KeyboardButton('Субота🥰')
Shedule2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMonday2,btnTuesday2,btnWednesday2,btnThursday2,btnFriday2,btnSaturday2, btnMain)
