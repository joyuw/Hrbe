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

import json, random, re, time, pytz
from datetime import datetime
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *


@Client.on_message(filters.group, group=21)
def addCustomReplyDone(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=addreply2,args=(c,m,k)).start()
    
def addreply2(c,m,k):
   if not m.from_user:
      return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return 
   
   TIME_ZONE = "Asia/Riyadh"
   ZONE = pytz.timezone(TIME_ZONE)
   TIME = datetime.now(ZONE)
   date = TIME.strftime("%d/%m/%Y %I:%M:%S %p")
   
   if m.text:
     if m.text == 'الغاء' and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}'):
       r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
       m.reply(f'{k} من عيوني لغيت اضافة الرد')
     
     if r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
       text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
       r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type=text&text={m.text.html}')
       r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','نص')
       r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
       r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
       r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
       return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.photo and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&photo={photo}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','صوره')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.video and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&video={video}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','فيديو')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.animation and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&animation={anim}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','متحركه')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.audio and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&audio={aud}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','صوت')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.voice and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&voice={voice}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','بصمه')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.document and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&doc={doc}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','ملف')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.sticker and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{text}:filter:{Dev_FLER}{m.chat.id}', f'type={type}&sticker={stic}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_FLER}','ستيكر')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_FLER}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)

   # ====== اضف رد متعدد - جمع الردود ======
   def _store_multi_reply(data_dict):
       temp_key = f'{m.chat.id}:addMultiFilterTemp:{m.from_user.id}{Dev_FLER}'
       r.rpush(temp_key, json.dumps(data_dict))
       count = r.llen(temp_key)
       return count

   if m.text:
     if r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
       if m.text == 'الغاء':
          pass  # let addreply (group=22) handle cancellation
       else:
          rep = {"type":"text","text":m.text.html}
          count = _store_multi_reply(rep)
          return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.photo and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      photo = m.photo.file_id
      caption = m.caption.html if m.caption else 'None'
      count = _store_multi_reply({"type":"photo","photo":photo,"caption":caption})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.video and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      video = m.video.file_id
      caption = m.caption.html if m.caption else 'None'
      count = _store_multi_reply({"type":"video","video":video,"caption":caption})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.animation and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      anim = m.animation.file_id
      caption = m.caption.html if m.caption else 'None'
      count = _store_multi_reply({"type":"animation","animation":anim,"caption":caption})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.audio and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      aud = m.audio.file_id
      caption = m.caption.html if m.caption else 'None'
      count = _store_multi_reply({"type":"audio","audio":aud,"caption":caption})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.voice and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      voice = m.voice.file_id
      caption = m.caption.html if m.caption else 'None'
      count = _store_multi_reply({"type":"voice","voice":voice,"caption":caption})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.document and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      doc = m.document.file_id
      caption = m.caption.html if m.caption else 'None'
      count = _store_multi_reply({"type":"doc","doc":doc,"caption":caption})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if m.sticker and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      stic = m.sticker.file_id
      count = _store_multi_reply({"type":"sticker","sticker":stic})
      return m.reply(f'<b>{k} تم اضافة الرد رقم {count}</b>\n{k} ارسل الرد التالي او ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)
   

@Client.on_message(filters.text & filters.group, group=22)
def addCustomReply(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=addreply,args=(c,m,k)).start()
    
def addreply(c,m,k):
   if not m.from_user:  return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return    
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}'):  return 

   TIME_ZONE = "Asia/Riyadh"
   ZONE = pytz.timezone(TIME_ZONE)
   TIME = datetime.now(ZONE)
   date = TIME.strftime("%d/%m/%Y %I:%M:%S %p")

   text = m.text
   name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'FLER'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}')
   if r.get(f'Custom:{Dev_FLER}&text={text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_FLER}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد')
     return 
   
   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}')
     m.reply(f'{k} من عيوني لغيت مسح الرد')
     return 

   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_FLER}', m.text)
      r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_FLER}')
      m.reply(f'{k} حلو هسة ارسل جواب الرد\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
      return 

   if text.startswith('الرد ') and len(m.text.split()) > 1 and mod_pls(m.from_user.id,m.chat.id):
      reply = m.text.split(None,1)[1]
      if not r.get(f'{reply}:filterInfo:{m.chat.id}{Dev_FLER}'):
        return m.reply(f'{k} الرد مو مضاف')
      else:
        get = r.get(f'{reply}:filterInfo:{m.chat.id}{Dev_FLER}')
        split = get.split('by=')[1]
        by = split.split('&date=')[0]
        date = split.split('&date=')[1]
        type = r.get(f'{reply}:filtertype:{m.chat.id}{Dev_FLER}')
        text = f'{k} الرد ↢ [{reply}](tg://user?id={by})\n{k} تاريخ الاضافة ↢\n( {date} )\n{k} نوع الرد {type}\n☆'
        m.reply(text)
        return 
   
   if text == 'تعطيل الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_filter:{Dev_FLER}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_filter:{Dev_FLER}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} تمام عطلت الردود\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_filter:{Dev_FLER}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_filter:{Dev_FLER}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} تمام فعلت الردود\n☆',parse_mode=ParseMode.HTML)
  
   if text == 'تعطيل ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_filterMEM:{Dev_FLER}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_filterMEM:{Dev_FLER}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} تمام عطلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_filterMEM:{Dev_FLER}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_filterMEM:{Dev_FLER}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} تمام فعلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}'):
       return m.reply(f'{k} ماكو ردود اعضاء مضافه')
      else:
       text = 'ردود الاعضاء:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}'):
          rep = reply.split("&&&&")[0]
          type = reply.split("&&&&")[1]
          try:
            mention=c.get_users(int(type)).mention
          except:
            mention=f'<a href="tg://user?id={type}">{type}</a>'
          text += f'\n{count} - ( {rep} ) ࿓ ( {mention} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}'):
        return m.reply(f'{k} ماكو ردود اعضاء مضافه')
      else:
        total = 0
        for reply in r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}'):
           rep = reply
           r.delete(f'{rep}:filterMEM:{Dev_FLER}{m.chat.id}')
           r.srem(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}', rep)
           r.delete(f"{rep.split('&&&&')[1]}:FILT:{m.chat.id}{Dev_FLER}")
           total += 1
        return m.reply(f'{k} تمام مسحت ( {total} ) من ردود الاعضاء')
   
   if text == 'الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersList:{Dev_FLER}'):
       return m.reply(f'{k} ماكو ردود مضافه')
      else:
       text = 'ردود المجموعه:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:FiltersList:{Dev_FLER}'):
          rep = reply.decode() if isinstance(reply, bytes) else reply
          type = r.get(f'{rep}:filtertype:{m.chat.id}{Dev_FLER}')
          if not type:
              type = r.get(f'{rep}:multifiltertype:{Dev_FLER}{m.chat.id}') or 'متعدد'
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود المتعددة':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      total = 0
      for reply in r.smembers(f'{m.chat.id}:FiltersList:{Dev_FLER}'):
           rep = reply.decode() if isinstance(reply, bytes) else reply
           if r.get(f'{rep}:multifilter:{Dev_FLER}{m.chat.id}'):
               r.delete(f'{rep}:multifilter:{Dev_FLER}{m.chat.id}')
               r.delete(f'{rep}:multifiltertype:{Dev_FLER}{m.chat.id}')
               r.delete(f'{rep}:multifilterInfo:{Dev_FLER}{m.chat.id}')
               r.srem(f'{m.chat.id}:FiltersList:{Dev_FLER}', rep)
               total += 1
      if total == 0:
        return m.reply(f'{k} ماكو ردود متعددة مضافه')
      return m.reply(f'{k} تمام مسحت ( {total} ) من الردود المتعددة')

   if text == 'مسح الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersList:{Dev_FLER}'):
        return m.reply(f'{k} ماكو ردود مضافه')
      else:
        total = 0
        for reply in r.smembers(f'{m.chat.id}:FiltersList:{Dev_FLER}'):
           rep = reply
           r.delete(f'{rep}:filter:{Dev_FLER}{m.chat.id}')
           r.delete(f'{rep}:filtertype:{m.chat.id}{Dev_FLER}')
           r.delete(f'{rep}:filterInfo:{m.chat.id}{Dev_FLER}')
           r.delete(f'{rep}:multifilter:{Dev_FLER}{m.chat.id}')
           r.delete(f'{rep}:multifiltertype:{Dev_FLER}{m.chat.id}')
           r.delete(f'{rep}:multifilterInfo:{Dev_FLER}{m.chat.id}')
           r.srem(f'{m.chat.id}:FiltersList:{Dev_FLER}', rep)
           total += 1
        return m.reply(f'{k} تمام مسحت ( {total} ) من الردود')

   if text == 'حذف رد متعدد':
     if not r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        r.set(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}',1)
        m.reply(f'<b>{k} تمام عيني</b>\n{k} هسة ارسل الكلمة علمود امسح الرد المتعدد\n☆',parse_mode=ParseMode.HTML)
        return

   if text == 'الردود المتعددة':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      text = 'الردود المتعددة:\n'
      count = 1
      found = False
      for reply in r.smembers(f'{m.chat.id}:FiltersList:{Dev_FLER}'):
          rep = reply.decode() if isinstance(reply, bytes) else reply
          if r.get(f'{rep}:multifilter:{Dev_FLER}{m.chat.id}'):
              found = True
              mftype = r.get(f'{rep}:multifiltertype:{Dev_FLER}{m.chat.id}') or 'متعدد'
              text += f'\n{count} - ( {rep} ) ࿓ ( {mftype} )'
              count += 1
      if not found:
          return m.reply(f'{k} ماكو ردود متعددة مضافه')
      text += '\n☆'
      return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)

   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      if not r.get(f'{m.text}:filterInfo:{m.chat.id}{Dev_FLER}') and not r.get(f'{m.text}:multifilterInfo:{Dev_FLER}{m.chat.id}'):
        r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}')
        return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
      else:
           r.delete(f'{m.text}:filter:{Dev_FLER}{m.chat.id}')
           r.delete(f'{m.text}:filtertype:{m.chat.id}{Dev_FLER}')
           r.delete(f'{m.text}:filterInfo:{m.chat.id}{Dev_FLER}')
           r.delete(f'{m.text}:multifilter:{Dev_FLER}{m.chat.id}')
           r.delete(f'{m.text}:multifiltertype:{Dev_FLER}{m.chat.id}')
           r.delete(f'{m.text}:multifilterInfo:{Dev_FLER}{m.chat.id}')
           r.srem(f'{m.chat.id}:FiltersList:{Dev_FLER}', m.text)
           r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}')
           return m.reply(f'( {m.text} )\n{k} وحذفنا الرد ياحلو')
   
   if text == 'اضف ردي':
      if r.get(f'{m.chat.id}:lock_filterMEM:{Dev_FLER}'):
        return m.reply(f'{k} تم تعطيل ردود الأعضاء')
      if r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_FLER}"):
        name = r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_FLER}")
        return m.reply(f"{k} عندك رد مضاف من قبل و هو ( {name} )")
      else:
        m.reply(f'{k} حلو ، هسة ارسل اسمك')
        r.set(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_FLER}',1,ex=600)
        return 
   
   if r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_FLER}') and text == "الغاء":
     r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_FLER}')
     return m.reply(f"{k} تمام لغيت اضافة ردك")
     
   
   if r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_FLER}') and len(m.text) <= 50:
     name = m.text
     if r.sismember(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}',name):
       return m.reply(f"{k} هذا الإسم محجوز")
     else:
       r.sadd(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}',f"{name}&&&&{m.from_user.id}")
       r.sadd(f'{m.chat.id}:FiltersListMEMM:{Dev_FLER}',m.from_user.id)
       r.set(f'{name}:filterMEM:{Dev_FLER}{m.chat.id}',m.from_user.id)
       r.set(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_FLER}",name)
       r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_FLER}')
       return m.reply(f"{k} تمام ضفت ردك ( {name} )")
   
   if text == 'مسح ردي':
     if r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_FLER}"):
       rep=r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_FLER}")
       r.delete(f'{rep}:filterMEM:{Dev_FLER}{m.chat.id}')
       r.srem(f'{m.chat.id}:FiltersListMEM:{Dev_FLER}', f"{rep}&&&&{m.from_user.id}")
       r.delete(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_FLER}")
       return m.reply(f"{k} تمام مسحت ردك ( {rep} )")
     else:
       return m.reply(f"{k} ماعندك رد")
        
   if text == 'اضف رد':
     if not r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_FLER}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        m.reply(f'{k} حلو ، هسة ارسل الكلمة اللي تريدها')
        r.set(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_FLER}',1)
        return

   if text == 'اضف رد متعدد':
     if not r.get(f'{m.chat.id}:addMultiFilter:{m.from_user.id}{Dev_FLER}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        m.reply(f'<b>{k} حلو ، هسة ارسل الكلمة اللي تريدها</b>', parse_mode=ParseMode.HTML)
        r.set(f'{m.chat.id}:addMultiFilter:{m.from_user.id}{Dev_FLER}',1)
        return

   if r.get(f'{m.chat.id}:addMultiFilter:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
      word = m.text
      r.delete(f'{m.chat.id}:addMultiFilter:{m.from_user.id}{Dev_FLER}')
      r.set(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}', word)
      r.delete(f'{m.chat.id}:addMultiFilterTemp:{m.from_user.id}{Dev_FLER}')
      return m.reply(f'<b>{k} حلو هسة ارسل الرد الاول</b>\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف,ستيكر )\n{k} ارسل <b>الغاء</b> لحفظ الردود', parse_mode=ParseMode.HTML)

   if text == 'الغاء' and r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}'):
      word = r.get(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}')
      temp_key = f'{m.chat.id}:addMultiFilterTemp:{m.from_user.id}{Dev_FLER}'
      count = r.llen(temp_key)
      if count == 0:
         r.delete(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}')
         r.delete(temp_key)
         return m.reply(f'{k} من عيوني لغيت اضافة الرد المتعدد')
      else:
         # نقل الردود من temp إلى permanent
         permanent_key = f'{word}:multifilter:{Dev_FLER}{m.chat.id}'
         r.delete(permanent_key)
         for item in r.lrange(temp_key, 0, -1):
            r.rpush(permanent_key, item.decode() if isinstance(item, bytes) else item)
         r.set(f'{word}:multifiltertype:{Dev_FLER}{m.chat.id}','متعدد')
         r.set(f'{word}:multifilterInfo:{Dev_FLER}{m.chat.id}', f'by={m.from_user.id}&date={date}')
         r.sadd(f'{m.chat.id}:FiltersList:{Dev_FLER}', f'{word}')
         r.delete(f'{m.chat.id}:addMultiFilter2:{m.from_user.id}{Dev_FLER}')
         r.delete(temp_key)
         return m.reply(f'<b>{k} تمام ضفت الرد المتعدد ( {word} )</b>\n{k} بعدد ( {count} ) رد\n☆', parse_mode=ParseMode.HTML)
        
   if text == 'حذف رد':
     if not r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        r.set(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_FLER}',1)
        m.reply(f'{k} تمام عيني\n{k} هسة ارسل الرد علمود امسحه\n☆',parse_mode=ParseMode.HTML)
        return
   
   
   
   
   

   

@Client.on_message(filters.group & filters.text, group=23)
def addCustomReplyRandom(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=addreplyrandom,args=(c,m,k)).start()
   

def addreplyrandom(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}'):  return 
   text = m.text
   name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'FLER'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}')
   if r.get(f'Custom:{Dev_FLER}&text={text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return

   if r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_FLER}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد المميز')
     return 
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     rep = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}')
     r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}')
     r.delete(f'{rep}:randomfilter:{m.chat.id}{Dev_FLER}')
     m.reply(f'{k} من عيوني لغيت اضافه الرد المميز')
     return 
     
   if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}')
     return m.reply(f'{k} من عيوني لغيت مسح الرد المميز')
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}') and text == 'تم':
     text = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}')
     count = len(r.smembers((f'{text}:randomfilter:{m.chat.id}{Dev_FLER}')))
     r.set(f'{text}:randomFilter:{m.chat.id}{Dev_FLER}', 1)
     r.sadd(f'{m.chat.id}:RFiltersList:{Dev_FLER}', text)
     r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}')
     return m.reply(f'{k} تم اضافه الرد المميز ( {text} )\n{k} بـ ( {count} ) جواب رد\n☆',parse_mode=ParseMode.HTML)
   
   if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:randomFilter:{m.chat.id}{Dev_FLER}'):
       r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}')
       return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
     else:
       r.delete(f'{m.text}:randomFilter:{m.chat.id}{Dev_FLER}')
       r.delete(f'{m.text}:randomfilter:{m.chat.id}{Dev_FLER}')
       r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}')
       r.srem(f'{m.chat.id}:RFiltersList:{Dev_FLER}',m.text)
       return m.reply(f'{k} تمام مسحت الرد العشوائي ')
       
   
   if r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_FLER}')
     r.set(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}',m.text)
     return m.reply(f'{k} حلو هسة ارسل اجوبة الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}') and mod_pls(m.from_user.id,m.chat.id):
     text = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}')
     r.sadd(f'{text}:randomfilter:{m.chat.id}{Dev_FLER}', m.text.html)
     return m.reply(f'{k} حلو ضفت هذا الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المميزه':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:RFiltersList:{Dev_FLER}'):
       return m.reply(f'{k} ماكو ردود عشوائيه مضافه')
      else:
       text = 'الردود المميزه:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:RFiltersList:{Dev_FLER}'):
          rep = reply
          ttt = len(r.smembers(f'{rep}:randomfilter:{m.chat.id}{Dev_FLER}'))
          text += f'\n{count} - ( {rep} ) ☆ ( {ttt} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المميزه':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:RFiltersList:{Dev_FLER}'):
         return m.reply(f'{k} ماكو ردود مميزه مضافه')
       else:
         count = 0
         for reply in r.smembers(f'{m.chat.id}:RFiltersList:{Dev_FLER}'):
            rep = reply
            r.delete(f'{rep}:randomfilter:{m.chat.id}{Dev_FLER}')
            r.srem(f'{m.chat.id}:RFiltersList:{Dev_FLER}', rep)
            r.delete(f'{rep}:randomFilter:{m.chat.id}{Dev_FLER}')
            count += 1
         return m.reply(f'{k} تمام مسحت ( {count} ) رد مميز ')
            
   if text == 'اضف رد مميز' and not r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_FLER}') and not r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_FLER}'):
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_FLER}',1)
       return m.reply(f'{k} حلو ، ارسل هسة الكلمة الي تريدها')
   
   if text == 'حذف رد مميز' and not r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}'):
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_FLER}',1)
       return m.reply(f'{k} تمام عيني\n{k} هسة ارسل الرد علمود امسحه\n☆',parse_mode=ParseMode.HTML)
   
   
     
     
     
