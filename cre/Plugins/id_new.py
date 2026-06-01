import random, re, time, os
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.get_create import get_creation_date
from pyrogram.raw.functions.users import GetFullUser
from io import BytesIO
from pyrogram.file_id import FileId, FileType, ThumbnailSource
from pyrogram.raw.functions.channels import GetFullChannel
from .games import get_emoji_bank
from helpers.Ranks import isLockCommand

def format_usernames(user_obj):
    usernames = []
    if user_obj.username:
        usernames.append(f"@{user_obj.username}")
    if hasattr(user_obj, 'usernames') and user_obj.usernames:
        for u in user_obj.usernames:
            uname = f"@{u.username}"
            if uname not in usernames:
                usernames.append(uname)
    if not usernames:
        return 'None'
    return ' ، '.join(usernames)

# أمر الـ ID الجديد بدعم Custom Emoji
@Client.on_message(filters.text & filters.group, group=13)
def new_id_command(c, m):
    """أمر ID جديد بدعم Custom Emoji والألوان"""
    text = m.text
    k = r.get(f'{Dev_FLER}:botkey')
    
    # التحقق من أمر الـ ID
    if not (text == 'ايدي' or text.lower() == 'id' or text.lower() == 'ا'):
        return
    
    # التحقق من تعطيل الأمر
    if r.get(f'{m.chat.id}:disableID:{Dev_FLER}'):
        return
    
    try:
        # تحديد المستخدم (الرد أو المرسل)
        if m.reply_to_message and m.reply_to_message.from_user:
            u = m.reply_to_message.from_user
        else:
            u = m.from_user
        
        # جلب بيانات المستخدم
        try:
            u = c.get_users(u.id)
        except:
            pass
        
        # تجميع المعلومات
        _name = ((u.first_name or '') + (' ' + u.last_name if u.last_name else '')).strip() or 'لا يوجد'
        _user = format_usernames(u)
        _rank = get_rank(u.id, m.chat.id)
        
        try:
            msgs = int(r.get(f'{Dev_FLER}{m.chat.id}:TotalMsgs:{u.id}') or 0)
        except:
            msgs = 0
        
        try:
            if not r.get(f'{m.chat.id}:TotalEDMsgs:{u.id}{Dev_FLER}'):
                edits = 0
            else:
                edits = int(r.get(f'{m.chat.id}:TotalEDMsgs:{u.id}{Dev_FLER}') or 0)
        except:
            edits = 0
        
        try:
            create = get_creation_date(u.id)
        except:
            create = 'غير متوفر'
        
        # بناء رسالة الـ ID بـ Custom Emoji
        # السطر الأول
        text_line1 = f"يوزَر حسابَك ⌯ {_user}"
        # السطر الثاني
        text_line2 = f"عَدَد رسائلَك ⌯ {msgs}"
        # السطر الثالث
        text_line3 = f"رتبتَك ⌯ {_rank}"
        # السطر الرابع
        text_line4 = f"ايدي حسابَك ⌯ `{u.id}`"
        # السطر الخامس
        text_line5 = f"تَعديلاتَك ⌯ {edits}"
        # السطر السادس
        text_line6 = f"انشاء حسابَك ⌯ {create}"
        
        # دمج الأسطر مع Custom Emoji
        message_text = f'''
{text_line1}
{text_line2}
{text_line3}
{text_line4}
{text_line5}
{text_line6}

<i>Made with ❤️</i>
'''
        
        # إرسال الرسالة
        return m.reply(message_text, disable_web_page_preview=True)
    
    except Exception as e:
        print(f"Error in new_id_command: {e}")
        return m.reply(f'{k} ❌ حدث خطأ في جلب المعلومات')
