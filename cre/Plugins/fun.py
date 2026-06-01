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


@Client.on_message(filters.text & filters.group, group=34)
def funHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    channel = r.get(f'{Dev_FLER}:BotChannel') if r.get(f'{Dev_FLER}:BotChannel') else 'RobinSource'
    Thread(target=funFunc,args=(c,m,k,channel)).start()

def funFunc(c,m,k,channel):
   if not m.from_user:  return
   if r.get(f'{m.chat.id}:disableFun:{Dev_FLER}'):  return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
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
   ################# CAKE #################
   if text == 'رفع كيك' or text == 'رفع كيكه' or text == 'رفع كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:CakeList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} كيكه من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:CakeList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:CakeName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته كيكه 🍰\n☆')

   if text == 'تنزيل كيك' or text == 'تنزيل كيكه' or text == 'تنزيل كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:CakeList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو كيكه من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:CakeList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:CakeName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من كيكه\n☆')

   if text == 'قائمه الكيك' or text == 'قائمة الكيك':
     if not r.smembers(f'{Dev_FLER}:CakeList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الكيك فارغة')
     else:
       txt = '- قائمة الكيك 🍰\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:CakeList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:CakeName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الكيك' or text == 'مسح قائمه الكيك':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:CakeList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الكيك فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الكيك')
         for cake in r.smembers(f'{Dev_FLER}:CakeList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:CakeList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:CakeName:{cake}')

   ################# CAKE #################

   ################# 3SL #################
   if text == 'رفع عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:3SLList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} عسل من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:3SLList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:3SLName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته عسل 🍯\n☆')

   if text == 'تنزيل عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:3SLList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو عسل من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:3SLList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:3SLName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من عسل\n☆')

   if text == 'قائمه العسل' or text == 'قائمة العسل':
     if not r.smembers(f'{Dev_FLER}:3SLList:{m.chat.id}'):
       return m.reply(f'{k} قائمة العسل فارغة')
     else:
       txt = '- قائمة العسل 🍯\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:3SLList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:3SLName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة العسل' or text == 'مسح قائمه العسل':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:3SLList:{m.chat.id}'):
         return m.reply(f'{k} قائمة العسل فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة العسل')
         for cake in r.smembers(f'{Dev_FLER}:3SLList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:3SLList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:3SLName:{cake}')

   ################# 3SL #################

   ################# ZQ #################
   if text == 'رفع زق':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:ZQZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} زق من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:ZQZQList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:ZQZQName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته زق 💩\n☆')

   if text == 'تنزيل زق':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:ZQZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو زق من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:ZQZQList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:ZQZQName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من زق\n☆')

   if text == 'قائمه الزق' or text == 'قائمة الزق':
     if not r.smembers(f'{Dev_FLER}:ZQZQList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الزق فارغة')
     else:
       txt = '- قائمة الزق 💩\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:ZQZQList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:ZQZQName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الزق' or text == 'مسح قائمه الزق':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:ZQZQList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الزق فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الزق')
         for cake in r.smembers(f'{Dev_FLER}:ZQZQList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:ZQZQList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:ZQZQName:{cake}')

   ################# ZQ #################
   if text == 'رفع نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:ZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} نصاب من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:ZQList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:ZQName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته نصاب 🥷\n☆')

   if text == 'تنزيل نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:ZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو نصاب من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:ZQList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:ZQName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من نصاب\n☆')

   if text == 'قائمه النصابين' or text == 'قائمة النصابين':
     if not r.smembers(f'{Dev_FLER}:ZQList:{m.chat.id}'):
       return m.reply(f'{k} قائمة النصابين فارغة')
     else:
       txt = '- قائمة النصابين 🥷\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:ZQList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:ZQName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة النصابين' or text == 'مسح قائمه النصابين':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:ZQList:{m.chat.id}'):
         return m.reply(f'{k} قائمة النصابين فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة النصابين')
         for cake in r.smembers(f'{Dev_FLER}:ZQList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:ZQList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:ZQName:{cake}')

   ################# ZQ #################

   ################# 7MR #################
   if text == 'رفع حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:7MRList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} حمار من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:7MRList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:7MRName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته حمار 🦓\n☆')

   if text == 'تنزيل حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:7MRList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو حمار من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:7MRList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:7MRName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من حمار\n☆')

   if text == 'قائمه الحمير' or text == 'قائمة الحمير':
     if not r.smembers(f'{Dev_FLER}:7MRList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الحمير فارغة')
     else:
       txt = '- قائمة الحمير 🦓\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:7MRList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:7MRName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الحمير' or text == 'مسح قائمه الحمير':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:7MRList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الحمير فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الحمير')
         for cake in r.smembers(f'{Dev_FLER}:7MRList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:7MRList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:7MRName:{cake}')

   ################# 7MR #################

   ################# COW #################
   if text == 'رفع بقرة' or text == 'رفع بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:COWList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} بقرة من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:COWList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:COWName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته بقرة 🐄\n☆')

   if text == 'تنزيل بقرة' or text == 'تنزيل بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:COWList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو بقرة من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:COWList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:COWName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من بقرة\n☆')

   if text == 'قائمه البقر' or text == 'قائمة البقر':
     if not r.smembers(f'{Dev_FLER}:COWList:{m.chat.id}'):
       return m.reply(f'{k} قائمة البقر فارغة')
     else:
       txt = '- قائمة البقر 🐄\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:COWList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:COWName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة البقر' or text == 'مسح قائمه البقر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:COWList:{m.chat.id}'):
         return m.reply(f'{k} قائمة البقر فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة البقر')
         for cake in r.smembers(f'{Dev_FLER}:COWList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:COWList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:COWName:{cake}')

   ################# COW #################

   ################# DOG #################
   if text == 'رفع كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:DOGList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} كلب من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:DOGList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:DOGName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته كلب 🐩\n☆')

   if text == 'تنزيل كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:DOGList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو كلب من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:DOGList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:DOGName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من كلب\n☆')

   if text == 'قائمه الكلاب' or text == 'قائمة الكلاب':
     if not r.smembers(f'{Dev_FLER}:DOGList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الكلاب فارغة')
     else:
       txt = '- قائمة الكلاب 🐩\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:DOGList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:DOGName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الكلاب' or text == 'مسح قائمه الكلاب':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:DOGList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الكلاب فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الكلاب')
         for cake in r.smembers(f'{Dev_FLER}:DOGList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:DOGList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:DOGName:{cake}')

   ################# DOG #################

   ################# MON #################
   if text == 'رفع قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:MONList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} قرد من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:MONList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:MONName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته قرد 🐒\n☆')

   if text == 'تنزيل قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:MONList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو قرد من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:MONList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:MONName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من قرد\n☆')

   if text == 'قائمه القرود' or text == 'قائمة القرود':
     if not r.smembers(f'{Dev_FLER}:MONList:{m.chat.id}'):
       return m.reply(f'{k} قائمة القرود فارغة')
     else:
       txt = '- قائمة القرود 🐒\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:MONList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:MONName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة القرود' or text == 'مسح قائمه القرود':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:MONList:{m.chat.id}'):
         return m.reply(f'{k} قائمة القرود فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة القرود')
         for cake in r.smembers(f'{Dev_FLER}:MONList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:MONList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:MONName:{cake}')

   ################# MON #################

   ################# TES #################
   if text == 'رفع تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:TESList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تيس من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:TESList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:TESName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته تيس 🐐\n☆')

   if text == 'تنزيل تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:TESList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو تيس من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:TESList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:TESName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من تيس\n☆')

   if text == 'قائمه التيس' or text == 'قائمة التيس':
     if not r.smembers(f'{Dev_FLER}:TESList:{m.chat.id}'):
       return m.reply(f'{k} قائمة التيوس فارغة')
     else:
       txt = '- قائمة التيوس 🐐\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:TESList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:TESName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة التيس' or text == 'مسح قائمه التيس':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:TESList:{m.chat.id}'):
         return m.reply(f'{k} قائمة التيوس فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة التيوس')
         for cake in r.smembers(f'{Dev_FLER}:TESList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:TESList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:TESName:{cake}')

   ################# TES #################


   ################# TOR #################
   if text == 'رفع ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:TORList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ثور من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:TORList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:TORName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته ثور 🐂\n☆')

   if text == 'تنزيل ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:TORList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو ثور من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:TORList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:TORName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من ثور\n༄')

   if text == 'قائمه الثور' or text == 'قائمة الثور':
     if not r.smembers(f'{Dev_FLER}:TORList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الثور فارغة')
     else:
       txt = '- قائمة الثور 🐂\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:TORList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:TORName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الثور' or text == 'مسح قائمه الثور':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:TORList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الثور فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الثور')
         for cake in r.smembers(f'{Dev_FLER}:TORList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:TORList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:TORName:{cake}')

   ################# TOR #################


   ################# B3S #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:B3SList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} هكر من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:B3SList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:B3SName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته هكر 🏅\n☆')

   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:B3SList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو هكر من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:B3SList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:B3SName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من هكر\n☆')

   if text == 'قائمه الهكر' or text == 'قائمة الهكر':
     if not r.smembers(f'{Dev_FLER}:B3SList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الهكر فارغة')
     else:
       txt = '- قائمة الهكر 🏅\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:B3SList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:B3SName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الهكر' or text == 'مسح قائمه الهكر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:B3SList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الهكر فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الهكر')
         for cake in r.smembers(f'{Dev_FLER}:B3SList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:B3SList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:B3SName:{cake}')

   ################# B3S #################

   ################# DJJ #################
   if text == 'رفع دجاجه' or text == 'رفع دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:DJJList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} دجاجه من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:DJJList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:DJJName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته دجاجه 🐓\n☆')

   if text == 'تنزيل دجاجه' or text == 'تنزيل دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:DJJList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو دجاجه من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:DJJList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:DJJName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من دجاجه\n☆')

   if text == 'قائمه الدجاج' or text == 'قائمة الدجاج':
     if not r.smembers(f'{Dev_FLER}:DJJList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الدجاج فارغة')
     else:
       txt = '- قائمة الدجاج 🐓\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:DJJList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:DJJName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الدجاج' or text == 'مسح قائمه الدجاج':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:DJJList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الدجاج فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الدجاج')
         for cake in r.smembers(f'{Dev_FLER}:DJJList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:DJJList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:DJJName:{cake}')

   ################# DJJ #################

   ################# HTF #################
   if text == 'رفع ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:HTFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ملكه من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:HTFList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:HTFName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته ملكه 🧱\n☆')

   if text == 'تنزيل ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:HTFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو ملكه من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:HTFList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:HTFName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من ملكه\n☆')

   if text == 'قائمه الهطوف' or text == 'قائمة الهطوف':
     if not r.smembers(f'{Dev_FLER}:HTFList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الهطوف فارغة')
     else:
       txt = '- قائمة الهطوف 🧱\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:HTFList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:HTFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الهطوف' or text == 'مسح قائمه الهطوف':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:HTFList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الهطوف فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الهطوف')
         for cake in r.smembers(f'{Dev_FLER}:HTFList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:HTFList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:HTFName:{cake}')

   ################# HTF #################

   ################# SYD #################
   if text == 'رفع صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:SYDList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} صياد من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:SYDList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:SYDName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته صياد 🔫\n☆')

   if text == 'تنزيل صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:SYDList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو صياد من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:SYDList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:SYDName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من صياد\n☆')

   if text == 'قائمه الصيادين' or text == 'قائمة الصيادين':
     if not r.smembers(f'{Dev_FLER}:SYDList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الصيادين فارغة')
     else:
       txt = '- قائمة الصيادين 🔫\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:SYDList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:SYDName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الصيادين' or text == 'مسح قائمه الصيادين':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:SYDList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الصيادين فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الصيادين')
         for cake in r.smembers(f'{Dev_FLER}:SYDList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:SYDList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:SYDName:{cake}')

   ################# SYD #################

   ################# 5RF #################
   if text == 'رفع خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:5RFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} خروف من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:5RFList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:5RFName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته خروف 🐏\n☆')

   if text == 'تنزيل خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:5RFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو خروف من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:5RFList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:5RFName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من خروف\n☆')

   if text == 'قائمه الخرفان' or text == 'قائمة الخرفان':
     if not r.smembers(f'{Dev_FLER}:5RFList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الخرفان فارغة')
     else:
       txt = '- قائمة الخرفان 🐏\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:5RFList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:5RFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة الخرفان' or text == 'مسح قائمه الخرفان':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:5RFList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الخرفان فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة الخرفان')
         for cake in r.smembers(f'{Dev_FLER}:5RFList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:5RFList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:5RFName:{cake}')

   ################# 5RF #################

   ################# TEZ #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_FLER}:TEZList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} هكر من قبل\n☆')
       else:
         r.sadd(f'{Dev_FLER}:TEZList:{m.chat.id}',id)
         r.set(f'{Dev_FLER}:TEZName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام رفعته هكر ♕\n☆')

   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_FLER}:TEZList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو هكر من قبل\n☆')
       else:
         r.srem(f'{Dev_FLER}:TEZList:{m.chat.id}',id)
         r.delete(f'{Dev_FLER}:TEZName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تمام نزلته من هكر\n☆')

   if text == 'قائمه هكر' or text == 'قائمة هكر':
     if not r.smembers(f'{Dev_FLER}:TEZList:{m.chat.id}'):
       return m.reply(f'{k} قائمة هكر فارغة')
     else:
       txt = '- قائمة هكر ♕\n'
       count = 1
       for cake in r.smembers(f'{Dev_FLER}:TEZList:{m.chat.id}'):
          mention = r.get(f'{Dev_FLER}:TEZName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح قائمة هكر' or text == 'مسح قائمه هكر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_FLER}:TEZList:{m.chat.id}'):
         return m.reply(f'{k} قائمة هكر فارغة')
       else:
         m.reply(f'{k} تمام مسحت قائمة هكر')
         for cake in r.smembers(f'{Dev_FLER}:TEZList:{m.chat.id}'):
           r.srem(f'{Dev_FLER}:TEZList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_FLER}:TEZName:{cake}')

   ################# TEZ #################

   ################# 🔮 #################

   if text == 'رفع لقلبي' and m.reply_to_message:
     return m.reply('{} رفعته لقلبك\n{} اللهم حسد 😔'.format(k,k))

   if text == 'تنزيل من قلبي' and m.reply_to_message:
     return m.reply('اح اح ماتوصل')

   ################# 🔮 #################








