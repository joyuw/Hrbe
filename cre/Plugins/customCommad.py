
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

@Client.on_message(filters.text & filters.group, group=999)
def customCummandHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=addcommand,args=(c,m,k)).start()


def addcommand(c,m,k):
   if not m.from_user:  return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   name = r.get(f'{Dev_FLER}:BotName') if r.get(f'{Dev_FLER}:BotName') else 'FLER'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={text}')
   if r.get(f'Custom:{Dev_FLER}&text={text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')

   if r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_FLER}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')

   if re.search("^ترتيب الاوامر$", text):
      if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
      else:
          ar = {
              "ا":"ايدي",
              "م":"رفع مميز",
              "اد":"رفع ادمن",
              "مد":"رفع مدير",
              "تعط":"تعطيل الايدي بالصوره",
              "تفع":"تفعيل الايدي بالصوره",
              "ر":"الرابط",
              "تغ":"تغيير الايدي",
              "رف":"رفع القيود",
              "مع":"معاني",
              "حذ":"حذف رد",
              "رد":"اضف رد",
              "رر":"الردود",
              "ق ك":"قفل الكل",
              "ف ت":"فتح الكل",
              "ام":"امسح",
              "ت":"تثبيت",
              "،،":"مسح المكتومين",
              "الغ":"الغاء الحظر",
              "رس":"مسح رسائلي",
              "تك":"تنزيل الكل",
              "فف":"فتح الاشعارات",
              "قق":"قفل الاشعارات",
              "ك":"كشف",
              "ند":"نداء",
              "ثن":"ثنائي",
              "اساسي":"رفع مطور اساسي",
              "ثانوي":"رفع مطور ثانوي",
              "زز":"زوجني",
              "طط":"طلاق",
              "ز":"زواج",
              "عم":"تحديد عمولة",
              "حذع":"حذف عمولة",
              "ع":"العمولات",
          }

          # إضافة الأوامر المختصرة
          added_commands = []
          for short_cmd, full_cmd in ar.items():
              # التحقق من أن الأمر الكامل موجود (لا نريد إضافة اختصارات لأوامر غير موجودة)
              r.set(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={short_cmd}', full_cmd)
              r.sadd(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}', short_cmd)
              added_commands.append(f'{short_cmd} ~ ( {full_cmd} )')

          response_text = f'{k} تم اضافة الاوامر التالية:\n\n'
          for i, cmd in enumerate(added_commands, 1):
              response_text += f'{i}) {cmd}\n'
          response_text += '\n༄'

          return m.reply(quote=True, text=response_text)

   if text == 'الاوامر المضافه' or text == 'الاوامر المضافة':
      if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
      else:
          if not r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}'):
            return m.reply(quote=True,text=f'{k} ماكو اوامر مضافه')
          else:
              text = 'الاوامر المضافة:\n'
              count = 0
              for cmnd in r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}'):
                 count += 1
                 command = cmnd
                 cc = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n༄'
              return m.reply(quote=True,text=text)

   if text == 'اضف امر' or text == 'تغيير امر':
     if not r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}'):
       if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}',1)
          m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم علمود اغيره')
          return

   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_FLER}')
      r.set(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_FLER}', m.text)
      m.reply(quote=True,text=f'{k} حلو علمود تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد هسة\n☆')
      return

   if r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_FLER}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_FLER}')
      command_n = m.text
      r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_FLER}')
      r.set(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={command_n}', command_o)
      r.sadd(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}', command_n)
      m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return

   # أمر النداء
   if text == 'نداء':
      if not admin_pls(m.from_user.id, m.chat.id):
         return m.reply(quote=True, text=f'{k} ⇜ هذا الأمر يخص ( الادمن وفوق ) بس')

      # قائمة الرسائل العشوائية
      call_messages = [
         "يـا قمـري ❤️‍🔥",
         "حنسوي العاب تعا 🌚💗",
         "وين طامس يحلو 🌚❤️‍🔥 : ~ 💕💕",
         "تعا نورنه 😉🤍 : ~",
         "مس يحلو 🌚🤍 : ~",
         "تعال لك وين طامس : ~",
         "الطف مخلوق حياتي 💖 : ~",
         "تعا نورنه 😉🤍 : ~"
      ]

      try:
         # الحصول على قائمة أعضاء المجموعة
         members_list = []
         for member in m.chat.get_members(limit=200):
            if (member.user and
                not member.user.is_deleted and
                not member.user.is_bot and
                member.user.id != m.from_user.id):  # استبعاد المرسل والبوتات
               members_list.append(member.user)

         if not members_list:
            return m.reply(quote=True, text=f'{k} ماكو أعضاء متاحين للنداء')

         # اختيار عضو عشوائي
         random_member = random.choice(members_list)

         # اختيار رسالة عشوائية
         random_message = random.choice(call_messages)

         # إنشاء المنشن بطريقة صحيحة
         if random_member.username:
            mention = f"@{random_member.username}"
         else:
            mention = f"[{random_member.first_name}](tg://user?id={random_member.id})"

         # إرسال الرسالة مع المنشن
         m.reply(quote=True, text=f"• {random_message} {mention}")

      except Exception as e:
         print(f"خطأ في أمر النداء: {e}")
         return m.reply(quote=True, text=f'{k} حدث خطأ في تنفيذ الأمر')

      return

   # أمر ثنائي
   if text == 'ثنائي':
      if not mod_pls(m.from_user.id, m.chat.id):
         return m.reply(quote=True, text=f'{k} ⇜ هذا الأمر يخص ( المدير وفوق ) بس')

      try:
         # الحصول على قائمة أعضاء المجموعة
         members_list = []
         for member in m.chat.get_members(limit=200):
            if (member.user and
                not member.user.is_deleted and
                not member.user.is_bot and
                member.user.id != m.from_user.id):  # استبعاد المرسل والبوتات
               members_list.append(member.user)

         if len(members_list) < 2:
            return m.reply(quote=True, text=f'{k} يجب وجود عضوين على الأقل في المجموعة')

         # اختيار عضوين مختلفين عشوائياً
         selected_members = random.sample(members_list, 2)
         member1 = selected_members[0]
         member2 = selected_members[1]

         # إنشاء المنشن بطريقة صحيحة للعضو الأول
         if member1.username:
            mention1 = f"@{member1.username}"
         else:
            mention1 = f"[{member1.first_name}](tg://user?id={member1.id})"

         # إنشاء المنشن بطريقة صحيحة للعضو الثاني
         if member2.username:
            mention2 = f"@{member2.username}"
         else:
            mention2 = f"[{member2.first_name}](tg://user?id={member2.id})"

         # النص الثابت دائماً "ثنائي اليوم"
         response_text = f"- ثنائي اليوم\n - {mention1} + {mention2}"

         # إرسال الرسالة مع المنشن
         m.reply(quote=True, text=response_text)

      except Exception as e:
         print(f"خطأ في أمر ثنائي: {e}")
         return m.reply(quote=True, text=f'{k} حدث خطأ في تنفيذ الأمر')

      return


@Client.on_message(filters.text & filters.group, group=1000)
def delCustomCommandHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=delcommand,args=(c,m,k)).start()


def delcommand(c,m,k):
   if not m.from_user:  return
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}'):  return
   text = m.text
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={m.text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={m.text}')

   if r.get(f'Custom:{Dev_FLER}&text={m.text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={m.text}')

   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر ')

   if text == 'مسح الاوامر' or text == 'مسح الاوامر المضافة':
     if not mod_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس')
     else:
       if not r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}'):
         return m.reply(quote=True,text=f'{k} ماكو اوامر مضافه')
       else:
         count = 0
         for cmnd in r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}'):
           command = cmnd
           r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={command}')
           r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} تمام مسحت {count} أمر\n☆'
         return m.reply(quote=True,text=text)


   if text == 'مسح امر':
     if not r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}'):
       if not mod_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}',1)
          m.reply(quote=True,text=f'{k} ارسل الامر هسة')
          return


   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_FLER}')
      if not r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={m.text}'):
         return m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_FLER}', m.text)
      r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_FLER}&text={m.text}')
      m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} تمام مسحت الأمر\n☆')
      return




############ global CustomCommand



@Client.on_message(filters.text, group=1001)
def customCummandGlobalHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=addcommandg,args=(c,m,k)).start()


def addcommandg(c,m,k):
   if not m.from_user:
      return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   if r.get(f'Custom:{Dev_FLER}&text={m.text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={m.text}')

   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')

   if r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_FLER}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')

   if text == 'الاوامر العامه' or text == 'الاوامر المضافه العامه' and not m.chat.type == ChatType.PRIVATE:
      if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
      else:
          if not r.smembers(f'listCustom:{Dev_FLER}'):
            return m.reply(quote=True,text=f'{k} ماكو اوامر عامه مضافه')
          else:
              text = 'الاوامر العامه:\n'
              count = 0
              for cmnd in r.smembers(f'listCustom:{Dev_FLER}'):
                 count += 1
                 command = cmnd
                 cc = r.get(f'Custom:{Dev_FLER}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n☆'
              return m.reply(quote=True,text=text)

   if text == 'اضف امر عام' or text == 'تغيير امر عام':
     if not r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}'):
       if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}',1)
          m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم علمود اغيره')
          return

   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_FLER}')
      r.set(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_FLER}', m.text)
      m.reply(quote=True,text=f'{k} حلو علمود تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد هسة\n☆')
      return

   if r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_FLER}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_FLER}')
      command_n = m.text
      r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_FLER}')
      r.set(f'Custom:{Dev_FLER}&text={command_n}', command_o)
      r.sadd(f'listCustom:{Dev_FLER}', command_n)
      m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return


@Client.on_message(filters.text , group=1002)
def delCustomCommandGHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    Thread(target=delcommandg,args=(c,m,k)).start()


def delcommandg(c,m,k):
   if not m.from_user:
      return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return
   text = m.text
   if r.get(f'Custom:{Dev_FLER}&text={m.text}'):
       text = r.get(f'Custom:{Dev_FLER}&text={m.text}')

   if r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر عام')

   if text == 'مسح الاوامر العامه':
     if not dev_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
     else:
       if not r.smembers(f'listCustom:{Dev_FLER}'):
         return m.reply(quote=True,text=f'{k} ماكو اوامر عامه مضافه')
       else:
         count = 0
         for cmnd in r.smembers(f'listCustom:{Dev_FLER}'):
           command = cmnd
           r.delete(f'Custom:{Dev_FLER}&text={command}')
           r.srem(f'listCustom:{Dev_FLER}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} تمام مسحت {count} أمر عام\n☆'
         return m.reply(quote=True,text=text)


   if text == 'مسح امر عام':
     if not r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}'):
       if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}',1)
          m.reply(quote=True,text=f'{k} ارسل الامر هسة')
          return

   if re.match("^فتح امر ",text):
     if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       if not r.hget(Dev_FLER+f"locks-{m.chat.id}", txt):
         return m.reply("الامر مو مقفول من قبل")
       r.hdel(Dev_FLER+f"locks-{m.chat.id}", txt)
       return m.reply("تم فتح الامر بنجاح")

   if text == "الاوامر المقفوله":
      if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not r.hgetall(Dev_FLER+f"locks-{m.chat.id}"):
          return m.reply(f"{k} ماكو اوامر مقفولة")
        else:
          commands = r.hgetall(Dev_FLER+f"locks-{m.chat.id}")
          txt = "الاوامر المقفوله:\n\n"
          count = 1
          for command in commands:
            cc = int(commands[command])
            if cc == 0:
              rank = "مالك اساسي"
            elif cc == 1:
              rank = "مالك وفوق"
            elif cc == 2:
              rank = "مدير و فوق"
            elif cc == 3:
              rank = "ادمن وفوق"
            elif cc == 4:
              rank = "مميز و فوق"
            txt += f"{count} ) {command} - ( {rank} )\n"
            count += 1
          return m.reply(txt, disable_web_page_preview=True)

   if text == "مسح الاوامر المقفوله":
      if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not r.hgetall(Dev_FLER+f"locks-{m.chat.id}"):
          return m.reply(f"{k} ماكو اوامر مقفولة")
        else:
          count = len(list(r.hgetall(Dev_FLER+f"locks-{m.chat.id}").keys()))
          r.delete(Dev_FLER+f"locks-{m.chat.id}")
          return m.reply(f"{k} تمام مسحت ( {count} )")

   if re.match("^قفل امر ",text):
     if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       return m.reply(
          f"{k} حسناً عزيزي اختار نوع الرتبه :\n{k} سيتم وضع امر ↤︎( {txt} ) له فقط",
          reply_markup=InlineKeyboardMarkup(
            [
              [
                InlineKeyboardButton (
                   "مالك اساسي",
                   callback_data=f"gowner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مالك",
                   callback_data=f"owner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مدير",
                   callback_data=f"mod+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "ادمن",
                   callback_data=f"admin+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مميز",
                   callback_data=f"pre+{m.from_user.id}"
                )
              ]
            ]
          )
       )

   if r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_FLER}')
      if not r.get(f'Custom:{Dev_FLER}&text={m.text}'):
         return m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      r.srem(f'listCustom:{Dev_FLER}', m.text)
      r.delete(f'Custom:{Dev_FLER}&text={m.text}')
      m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} تمام مسحت الأمر العام\n☆')
      return


