'''


[ = This plugin is a part from RoBinSouRce code = ]
{"Developer":"https://t.me/is7rb"}

'''

import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand

@Client.on_message(filters.text & filters.group, group=12)
def getRanksHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    channel = r.get(f'{Dev_FLER}:BotChannel') if r.get(f'{Dev_FLER}:BotChannel') else 'RobinSource'
    Thread(target=get_ranks_func,args=(c,m,k,channel)).start()

def get_ranks_func(c,m,k,channel):
   if not m.from_user:  return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return

   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}'):  return
   text = m.text
   name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'RoBinSouRce'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}')
   if r.get(f'Custom:{Dev_FLER}&text={text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if text == 'قائمه Dev':
      if not devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص مبرمج السورس فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{Dev_FLER}DEV2'):
           return m.reply(f'<b>{k} ماكو قائمة مطورين ثانويين</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>قائمة المطورين الثانويين</b>\n\n'
          count = 1
          for dev2 in r.smembers(f'{Dev_FLER}DEV2'):
             if count == 101: break
             try:
               user = c.get_users(int(dev2))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(dev2)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)



   if text == 'قائمه مطور اساسي':
      if not devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص مبرمج السورس فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{Dev_FLER}DEV2'):
           return m.reply(f'<b>{k} ماكو قائمة مطور اساسي</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>قائمة مطور اساسي</b>\n\n'
          count = 1
          for dev2 in r.smembers(f'{Dev_FLER}DEV2'):
             if count == 101: break
             try:
               user = c.get_users(int(dev2))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(dev2)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'قائمه مطور ثانوي':
      if not dev2_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{Dev_FLER}DEV'):
          return m.reply(f'<b>{k} ماكو مطور ثانوي</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>قائمة مطور ثانوي</b>\n\n'
          count = 1
          for dev in r.smembers(f'{Dev_FLER}DEV'):
             if count == 101: break
             try:
               user = c.get_users(int(dev))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(dev)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   cid = m.chat.id
   if text == 'المالكين الاساسيين':
      if not dev_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص المطور وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{cid}:listGOWNER:{Dev_FLER}'):
          return m.reply(f'<b>{k} ماكو مالكين اساسيين</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>المالكين الاساسيين</b>\n\n'
          count = 1
          for gowner in r.smembers(f'{cid}:listGOWNER:{Dev_FLER}'):
             if count == 101: break
             try:
               user = c.get_users(int(gowner))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(gowner)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'المالكين':
      if not gowner_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص المالك الاساسي فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{cid}:listOWNER:{Dev_FLER}'):
          return m.reply(f'<b>{k} ماكو مالكيين</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>المالكيين</b>\n\n'
          count = 1
          for owner in r.smembers(f'{cid}:listOWNER:{Dev_FLER}'):
             if count == 101: break
             try:
               user = c.get_users(int(owner))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(owner)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'المدراء':
      if not owner_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص المالك وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{cid}:listMOD:{Dev_FLER}'):
          return m.reply(f'<b>{k} ماكو مدراء</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>المدراء</b>\n\n'
          count = 1
          for mod in r.smembers(f'{cid}:listMOD:{Dev_FLER}'):
             if count == 101: break
             try:
               user = c.get_users(int(mod))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(mod)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'الادمنيه':
      if not mod_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص المدير وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{cid}:listADMIN:{Dev_FLER}'):
          return m.reply(f'<b>{k} ماكو ادمن</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>الادمنيه</b>\n\n'
          count = 1
          for ADM in r.smembers(f'{cid}:listADMIN:{Dev_FLER}'):
             if count == 101: break
             try:
               user = c.get_users(int(ADM))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(ADM)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'المشرفين':
      if not owner_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص المالك وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
          text = '<b>المشرفين</b>\n\n'
          count = 1
          for mm in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if count == 101: break
            if not mm.user.is_deleted and not mm.user.is_bot:
               id = mm.user.id
               fname = mm.user.first_name or ''
               if mm.user.username:
                 text += f'{count} ➣ @{mm.user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ <a href="tg://user?id={id}">{fname}</a> ☆ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'المميزين':
      if not admin_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص الادمن وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{cid}:listPRE:{Dev_FLER}'):
          return m.reply(f'<b>{k} ماكو مميزين</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>المميزين</b>\n\n'
          count = 1
          for PRE in r.smembers(f'{cid}:listPRE:{Dev_FLER}'):
             if count == 101: break
             try:
               user = c.get_users(int(PRE))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(PRE)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)

   if text == 'المكتومين':
      if not mod_pls(m.from_user.id,m.chat.id):
        return m.reply(f'<b>{k} هذا الامر يخص المدير وفوق فقط</b>', parse_mode=ParseMode.HTML)
      else:
        if not r.smembers(f'{cid}:listMUTE:{Dev_FLER}'):
          return m.reply(f'<b>{k} ماكو مكتومين</b>', parse_mode=ParseMode.HTML)
        else:
          text = '<b>المكتومين</b>\n\n'
          count = 1
          for PRE in r.smembers(f'{cid}:listMUTE:{Dev_FLER}'):
             if count == 101: break
             try:
               user = c.get_users(int(PRE))
               id = user.id
               fname = user.first_name or ''
               mention = f'<a href="tg://user?id={id}">{fname}</a>'
               if user.username:
                 text += f'{count} ➣ @{user.username} ☆ <code>{id}</code>\n'
               else:
                 text += f'{count} ➣ {mention} ☆ <code>{id}</code>\n'
               count += 1
             except:
               id = int(PRE)
               text += f'{count} ➣ <code>{id}</code>\n'
               count += 1
          m.reply(text, parse_mode=ParseMode.HTML)





