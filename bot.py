# -*- coding: utf-8 -*-
import json
import asyncio
import logging
import keyboards as kb
import sqlite3
import requests
import config

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, UserProfilePhotos
from aiogram.types.message import ContentTypes
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN



storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://telegra.ph/file/2f5f388db3c2bbaf9decf.png", caption="Цена на рекламу:\n👉<a href='https://t.me/work_rabota_ua'>Работа.Подработка.Украина</a>\n\n📌 Закреп сообщения => 150грн/день\n\n📝 Текст в приветствии => 150грн/день\n\n🤖 Бот-рассылка => 100грн/день\n\n🕹 Кнопка => 50грн/день\n\n<b>При заказе от 3-х дней, скидка 30%</b>", reply_markup=kb.markup_start)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'При любом вопросе обращаться 👉 @mmmoneyadmin\n\nРазработчик бота @krsvski')


@dp.callback_query_handler(lambda callback_query: True)
async def some_callback_handler(callback_query: types.CallbackQuery):
    if callback_query.data == "bot":
        await bot.edit_message_media(media=types.InputMediaPhoto("https://telegra.ph/file/9fa8d41276a025759b3c0.jpg", caption="📌 Закрепить объявление!\nВаше объявление закреплено в шапке группы."), chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=kb.markup_buy)
    elif callback_query.data == "zakrep":
        await bot.edit_message_media(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, media=types.InputMediaPhoto("https://telegra.ph/file/9fa8d41276a025759b3c0.jpg", caption="📌 Закрепить объявление!\nВаше объявление закреплено в шапке группы."), reply_markup=kb.markup_buy)
    elif callback_query.data == "textre":
        await bot.edit_message_media(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, media=types.InputMediaPhoto("https://telegra.ph/file/08bdbed12a9a34c9b41c8.jpg", caption="📝 Ваш текст добавляется в приветствие.\nКаждый раз когда новый пользователь входит в чат оно отправляется ему + остальные участники группы видят это сообщение (ваше объявление)"), reply_markup=kb.markup_buy)
    elif callback_query.data == "knopka":
        await bot.edit_message_media(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, media=types.InputMediaPhoto("https://telegra.ph/file/a9c931af32b2e354f029d.jpg", caption="🕹 Кнопка.\nНажимая на кнопку под приветствием перебрасывает пользователя куда вам нужно, это может быть как объявления в чате так и сайт в интернете или сразу к вам в лс"), reply_markup=kb.markup_buy)
    elif callback_query.data == "back":
        await bot.edit_message_media(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, media=types.InputMediaPhoto("https://telegra.ph/file/2f5f388db3c2bbaf9decf.png", caption="Цена на рекламу:\n👉<a href='https://t.me/work_rabota_ua'>Работа.Подработка.Украина</a>\n\n📌 Закреп сообщения => 150грн/день\n\n📝 Текст в приветствии => 150грн/день\n\n🤖 Бот-рассылка => 100грн/день\n\n🕹 Кнопка => 50грн/день\n\n<b>При заказе от 3-х дней, скидка 30%</b>"), reply_markup=kb.markup_start)
    else:
        pass



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
