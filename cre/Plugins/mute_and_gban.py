'''


███████╗██╗     ███████╗██╗  ██╗
██╔════╝██║     ██╔════╝╚██╗██╔╝
█████╗  ██║     █████╗   ╚███╔╝ 
██╔══╝  ██║     ██╔══╝   ██╔██╗ 
██║     ███████╗███████╗██╔╝ ██╗
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝


[ = This plugin is a part from RoBinSouRce code = ]
{"Developer":"https://t.me/is7rb"}

'''
import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from pyrogram.errors import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand


@Client.on_message(filters.text & filters.group, group=20)
def mutesHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=mute_func,args=(c,m,k)).start()
    
    
def mute_func(c,m,k):
   if not m.from_user:  return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}:addCustomG:{m.from_user.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}'):  return 
   text = m.text
   name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'RoBinSouRce'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}')
   if r.get(f'Custom:{Dev_FLER}&text={text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return


   if text == 'كتم' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص المدير وفوق فقط</b>', parse_mode=ParseMode.HTML)
        if id == m.from_user.id:
           return m.reply(f'<b>{k} ما تكدر تكتم نفسك</b>', parse_mode=ParseMode.HTML)
        if pre_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
        if r.get(f'{id}:mute:{m.chat.id}{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مكتوم من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.set(f'{id}:mute:{m.chat.id}{Dev_FLER}', 1)
          r.sadd(f'{m.chat.id}:listMUTE:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} كتمته</b>''', parse_mode=ParseMode.HTML)
   
   if re.match("^كتم عام (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص المطور وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         return m.reply(f'<b>{k} ماكو يوزر هيج</b>', parse_mode=ParseMode.HTML)
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
      if r.get(f'{id}:mute:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مكتوم عام من قبل</b>''', parse_mode=ParseMode.HTML)
      else:
          r.set(f'{id}:mute:{Dev_FLER}', 1)
          r.sadd(f'listMUTE:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} كتمته عام</b>''', parse_mode=ParseMode.HTML)

   if re.match("^كتم (.*?)$", text) and len(text.split()) == 2:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not admin_pls(m.from_user.id,m.chat.id):
         return m.reply(f'<b>{k} هذا الامر يخص الادمن وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[1]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         return m.reply(f'<b>{k} ماكو يوزر هيج</b>', parse_mode=ParseMode.HTML)
      if id == m.from_user.id:
        return m.reply(f'<b>{k} ما تكدر تكتم نفسك</b>', parse_mode=ParseMode.HTML)
      if r.get(f'{id}:mute:{m.chat.id}{Dev_FLER}'):
         return m.reply(f'''<b>「 {mention} 」
{k} مكتوم من قبل</b>''', parse_mode=ParseMode.HTML)
      if pre_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
      r.set(f'{id}:mute:{m.chat.id}{Dev_FLER}', 1)
      r.sadd(f'{m.chat.id}:listMUTE:{Dev_FLER}', id)
      return m.reply(f'''<b>「 {mention} 」
{k} كتمته</b>''', parse_mode=ParseMode.HTML)
   
   if text == 'الغاء الكتم' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص الادمن وفوق فقط</b>', parse_mode=ParseMode.HTML)
        if not r.get(f'{id}:mute:{m.chat.id}{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو مكتوم من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.delete(f'{id}:mute:{m.chat.id}{Dev_FLER}')
          r.srem(f'{m.chat.id}:listMUTE:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} تمام الغيت كتمه</b>''', parse_mode=ParseMode.HTML)
   
   if re.match("^الغاء الكتم العام (.*?)$", text) and len(text.split()) ==  4:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[3]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f'<b>{k} ماكو مستخدم هيج</b>', parse_mode=ParseMode.HTML)
         mention = f'<a href="tg://user?id={id}">{id}</a>'
      if not r.get(f'{id}:mute:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو مكتوم عام من قبل</b>''', parse_mode=ParseMode.HTML)
      else:
          r.delete(f'{id}:mute:{Dev_FLER}')
          r.srem(f'listMUTE:{Dev_FLER}',id)
          return m.reply(f'''<b>「 {mention} 」
{k} لغيت كتمته عام</b>''', parse_mode=ParseMode.HTML)

   if re.match("^الغاء الكتم (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not mod_pls(m.from_user.id,m.chat.id):
         return m.reply(f'<b>{k} هذا الامر يخص المدير وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f'<b>{k} ماكو مستخدم هيج</b>', parse_mode=ParseMode.HTML)
         mention = f'<a href="tg://user?id={id}">{id}</a>'
      if not r.get(f'{id}:mute:{m.chat.id}{Dev_FLER}'):
         return m.reply(f'''<b>「 {mention} 」
{k} مو مكتوم من قبل</b>''', parse_mode=ParseMode.HTML)
      r.delete(f'{id}:mute:{m.chat.id}{Dev_FLER}')
      r.srem(f'{m.chat.id}:listMUTE:{Dev_FLER}', id)
      return m.reply(f'''<b>「 {mention} 」
{k} الغيت كتمه</b>''', parse_mode=ParseMode.HTML)
   
   if re.match("^حظر عام (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص المطور وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         return m.reply(f'<b>{k} ماكو يوزر هيج</b>', parse_mode=ParseMode.HTML)
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'<b>{k} ما تكدر تحظر {rank}</b>', parse_mode=ParseMode.HTML)
      if r.get(f'{id}:gban:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} محظور عام من قبل</b>''', parse_mode=ParseMode.HTML)
      else:
          r.set(f'{id}:gban:{Dev_FLER}', 1)
          r.sadd(f'listGBAN:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} حظرته عام</b>''', parse_mode=ParseMode.HTML)
   
   if re.match("^حظر عام من الالعاب (.*?)$", text) and len(text.split()) ==  5:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[4]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         return m.reply(f'<b>{k} ماكو يوزر هيج</b>', parse_mode=ParseMode.HTML)
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'<b>{k} ما تكدر تحظر {rank}</b>', parse_mode=ParseMode.HTML)
      if r.get(f'{id}:gbangames:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} محظور من الالعاب من قبل</b>''', parse_mode=ParseMode.HTML)
      else:
          r.set(f'{id}:gbangames:{Dev_FLER}', 1)
          r.sadd(f'listGBANGAMES:{Dev_FLER}', id)
          r.delete(f'{id}:Floos')
          r.srem("BankList",id)
          return m.reply(f'''<b>「 {mention} 」
{k} حظرته عام من الالعاب</b>''', parse_mode=ParseMode.HTML)
   
   if re.match("^الغاء الحظر العام من الالعاب (.*?)$", text) and len(text.split()) ==  6:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[5]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f'<b>{k} ماكو مستخدم هيج</b>', parse_mode=ParseMode.HTML)
         mention = f'<a href="tg://user?id={id}">{id}</a>'
      if not r.get(f'{id}:gbangames:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو محظور من الالعاب من قبل</b>''', parse_mode=ParseMode.HTML)
      else:
          r.delete(f'{id}:gbangames:{Dev_FLER}')
          r.srem(f'listGBANGAMES:{Dev_FLER}',id)
          return m.reply(f'''<b>「 {mention} 」
{k} لغيت حظره من الالعاب</b>''', parse_mode=ParseMode.HTML)

   if re.match("^الغاء الحظر العام (.*?)$", text) and len(text.split()) ==  4:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
      user = text.split()[3]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'<a href="tg://user?id={get.id}">{get.first_name}</a>'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f'<b>{k} ماكو مستخدم هيج</b>', parse_mode=ParseMode.HTML)
         mention = f'<a href="tg://user?id={id}">{id}</a>'
      if not r.get(f'{id}:gban:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو محظور عام من قبل</b>''', parse_mode=ParseMode.HTML)
      else:
          r.delete(f'{id}:gban:{Dev_FLER}')
          r.srem(f'listGBAN:{Dev_FLER}',id)
          return m.reply(f'''<b>「 {mention} 」
{k} لغيت حظره عام</b>''', parse_mode=ParseMode.HTML)

@Client.on_message(filters.group & ~filters.service & ~filters.bot, group=0)
def muteResponse(c,m):
    # التحقق من وجود المستخدم
    if not m.from_user:
        return
    # تجاهل رسائل البوت نفسه
    if m.from_user.id == c.me.id:
        return

    # فحص الحظر العام أولاً
    if r.get(f'{m.from_user.id}:gban:{Dev_FLER}'):
        try:
            c.ban_chat_member(m.chat.id, m.from_user.id)
        except:
            try:
                c.delete_messages(m.chat.id, m.id)
            except:
                pass
        return

    # فحص الكتم مع استثناء لحالة إنشاء الحساب البنكي
    if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}') or r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):
        # السماح بإنشاء الحساب البنكي حتى لو كان المستخدم مكتوم
        if not r.get(f'{m.from_user.id}:createBank:{m.chat.id}'):
            try:
                c.delete_messages(m.chat.id, m.id)
                return  # إيقاف معالجة الرسالة هنا
            except:
                try:
                    m.delete()
                    return
                except:
                    pass

    # التحقق من تفعيل البوت في المجموعة (بعد فحص الكتم)
    if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):
        return

# معالج إضافي للتأكد من حذف رسائل المكتومين
@Client.on_message(filters.all & filters.group, group=-1)
def muteResponseAll(c,m):
    if not m.from_user:
        return
    if m.from_user.id == c.me.id:
        return

    # فحص الحظر العام أولاً
    if r.get(f'{m.from_user.id}:gban:{Dev_FLER}'):
        try:
            c.ban_chat_member(m.chat.id, m.from_user.id)
        except:
            try:
                c.delete_messages(m.chat.id, m.id)
            except:
                pass
        return

    # فحص الكتم على جميع أنواع الرسائل مع استثناء لحالة إنشاء الحساب البنكي
    if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}') or r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):
        # السماح بإنشاء الحساب البنكي حتى لو كان المستخدم مكتوم
        if not r.get(f'{m.from_user.id}:createBank:{m.chat.id}'):
            try:
                c.delete_messages(m.chat.id, m.id)
            except:
                try:
                    m.delete()
                except:
                    pass

@Client.on_message(filters.text & filters.group, group=16)
def mutesHandlerG(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=mute_funcg,args=(c,m,k)).start()
    
    
def mute_funcg(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}:addCustomG:{m.from_user.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}'):  return 
   text = m.text
   name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'RoBinSouRce'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}')
   if r.get(f'Custom:{Dev_FLER}&text={text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={text}')
       
   if text == 'كتم عام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
        if r.get(f'{id}:mute:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مكتوم عام من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.set(f'{id}:mute:{Dev_FLER}', 1)
          r.sadd(f'listMUTE:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} كتمته عام</b>''', parse_mode=ParseMode.HTML)
      
   if text == 'حظر عام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تحظر {rank}</b>', parse_mode=ParseMode.HTML)
        if r.get(f'{id}:gban:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} محظور عام من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.set(f'{id}:gban:{Dev_FLER}', 1)
          r.sadd(f'listGBAN:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} حظرته عام</b>''', parse_mode=ParseMode.HTML)
   
   if text == 'حظر عام من الالعاب' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'<b>{k} هذا الامر يخص المطور وفوق فقط</b>', parse_mode=ParseMode.HTML)
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تحظر {rank}</b>', parse_mode=ParseMode.HTML)
        if r.get(f'{id}:gbangames:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} محظور من الالعاب من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.set(f'{id}:gbangames:{Dev_FLER}', 1)
          r.sadd(f'listGBANGAMES:{Dev_FLER}', id)
          r.delete(f'{id}:Floos')
          r.srem("BankList",id)
          return m.reply(f'''<b>「 {mention} 」
{k} حظرته عام من الالعاب</b>''', parse_mode=ParseMode.HTML)

   if text == 'الغاء الكتم العام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'<b>{k} هذا الامر يخص المطور وفوق فقط</b>', parse_mode=ParseMode.HTML)
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
        if not r.get(f'{id}:mute:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو مكتوم عام من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.delete(f'{id}:mute:{Dev_FLER}')
          r.srem(f'listMUTE:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} لغيت كتمته عام</b>''', parse_mode=ParseMode.HTML)
   
   if text == 'الغاء الحظر العام من الالعاب' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
        if not r.get(f'{id}:gbangames:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو محظور من الالعاب من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.delete(f'{id}:gbangames:{Dev_FLER}')
          r.srem(f'listGBANGAMES:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} لغيت حظره من الالعاب</b>''', parse_mode=ParseMode.HTML)

   if text == 'الغاء الحظر العام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'<b>{k} هذا الامر يخص مطور اساسي وفوق فقط</b>', parse_mode=ParseMode.HTML)
        id = m.reply_to_message.from_user.id
        fname = m.reply_to_message.from_user.first_name or ''
        mention = f'<a href="tg://user?id={id}">{fname}</a>'
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'<b>{k} ما تكدر تكتم {rank}</b>', parse_mode=ParseMode.HTML)
        if not r.get(f'{id}:gban:{Dev_FLER}'):
          return m.reply(f'''<b>「 {mention} 」
{k} مو محظور عام من قبل</b>''', parse_mode=ParseMode.HTML)
        else:
          r.delete(f'{id}:gban:{Dev_FLER}')
          r.srem(f'listGBAN:{Dev_FLER}', id)
          return m.reply(f'''<b>「 {mention} 」
{k} لغيت حظره عام</b>''', parse_mode=ParseMode.HTML)