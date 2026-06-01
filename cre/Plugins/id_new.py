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

@Client.on_message(filters.text & filters.group, group=13)
def new_id_command(c, m):
    """أمر ID جديد بدعم Custom Emoji"""
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
        
        # بناء رسالة الـ ID مع Custom Emoji IDs
        # استخدام تاغ HTML لـ Custom Emoji
        emoji_start_1 = '<emoji id="5794164805065514131">⌯</emoji>'
        emoji_end_1 = '<emoji id="5891156376473836675">⌯</emoji>'
        
        emoji_start_2 = '<emoji id="5794085322400733645">⌯</emoji>'
        emoji_end_2 = '<emoji id="6030537810509828330">⌯</emoji>'
        
        emoji_start_3 = '<emoji id="5794280000383358988">⌯</emoji>'
        emoji_end_3 = '<emoji id="5084979757905347540">⌯</emoji>'
        
        emoji_start_4 = '<emoji id="5794241397217304511">⌯</emoji>'
        
        emoji_start_5 = '<emoji id="5793985348446984682">⌯</emoji>'
        emoji_end_5 = '<emoji id="5769635757211784031">⌯</emoji>'
        
        emoji_start_6 = '<emoji id="5794324702402976226">⌯</emoji>'
        
        # بناء الرسالة مع الـ Custom Emoji
        message_text = f'''<b>👤 معلومات حسابك</b>

{emoji_start_1} يوزَر حسابَك ⌯ {_user} {emoji_end_1}
{emoji_start_2} عَدَد رسائلَك ⌯ {msgs} {emoji_end_2}
{emoji_start_3} رتبتَك ⌯ {_rank} {emoji_end_3}
{emoji_start_4} ايدي حسابَك ⌯ <code>{u.id}</code>
{emoji_start_5} تَعديلاتَك ⌯ {edits} {emoji_end_5}
{emoji_start_6} انشاء حسابَك ⌯ {create}

<i>Made with ❤️</i>
'''
        
        # إرسال الرسالة باستخدام HTML parsing
        return m.reply(message_text, parse_mode=enums.ParseMode.HTML)
    
    except Exception as e:
        print(f"Error in new_id_command: {e}")
        return m.reply(f'{k} ❌ حدث خطأ في جلب المعلومات')
