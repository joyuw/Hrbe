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

def get_top(users):
    users = [tuple(i.items()) for i in users]
    top = sorted(users, key=lambda i: i[-1][-1], reverse=True)
    top = [dict(i) for i in top]
    return top

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

# أمر الـ ID الجديد بدعم Custom Emoji والألوان
@Client.on_message(filters.text & filters.group, group=12)
def new_id_handler(c, m):
    k = r.get(f'{Dev_FLER}:botkey')
    text = m.text
    
    if text == 'ايدي' or text.lower() == 'id' or text.lower() == 'ا':
        if not m.reply_to_message:
            if r.get(f'{m.chat.id}:disableID:{Dev_FLER}'):
                return
            
            try:
                u = m.from_user
                try:
                    u = c.get_users(u.id)
                except:
                    pass
                
                _name = ((u.first_name or '') + (' ' + u.last_name if u.last_name else '')).strip() or 'لا يوجد'
                _user = format_usernames(u)
                _rank = get_rank(u.id, m.chat.id)
                msgs = int(r.get(f'{Dev_FLER}{m.chat.id}:TotalMsgs:{u.id}') or 0)
                
                if not r.get(f'{m.chat.id}:TotalEDMsgs:{u.id}{Dev_FLER}'):
                    edits = 0
                else:
                    edits = int(r.get(f'{m.chat.id}:TotalEDMsgs:{u.id}{Dev_FLER}') or 0)
                
                create = get_creation_date(u.id)
                
                # تنسيق الرسالة بـ Custom Emoji
                text = f'''<b>👤 معلومات المستخدم</b>

<emoji id="5794164805065514131">⌯</emoji> يوزَر حسابَك ⌯ {_user} <emoji id="5891156376473836675">⌯</emoji>
<emoji id="5794085322400733645">⌯</emoji> عَدَد رسائلَك ⌯ {msgs} <emoji id="6030537810509828330">⌯</emoji>
<emoji id="5794280000383358988">⌯</emoji> رتبتَك ⌯ {_rank} <emoji id="5084979757905347540">⌯</emoji>
<emoji id="5794241397217304511">⌯</emoji> ايدي حسابَك ⌯ <code>{u.id}</code>
<emoji id="5793985348446984682">⌯</emoji> تَعديلاتَك ⌯ {edits} <emoji id="5769635757211784031">⌯</emoji>
<emoji id="5794324702402976226">⌯</emoji> انشاء حسابَك ⌯ {create}

<i>Made with ❤️</i>
'''
                
                # إنشاء أزرار ملونة بـ Custom Emoji
                keyboard = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            text="💬 الملف الشخصي",
                            callback_data=f"view_profile:{u.id}",
                            style="primary",
                            icon_custom_emoji_id="5794164805065514131"
                        ),
                        InlineKeyboardButton(
                            text="📊 الإحصائيات",
                            callback_data=f"view_stats:{u.id}",
                            style="success",
                            icon_custom_emoji_id="5794085322400733645"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="⚙️ الخيارات",
                            callback_data=f"view_options:{u.id}",
                            style="danger",
                            icon_custom_emoji_id="5794280000383358988"
                        )
                    ]
                ])
                
                return m.reply(text, reply_markup=keyboard)
            
            except Exception as e:
                print(f"Error in new_id_handler: {e}")
                return m.reply(f'{k} حدث خطأ في جلب المعلومات')
        
        else:
            # الرد على مستخدم
            if not m.reply_to_message.from_user:
                return m.reply(f'{k} لا يمكن جلب معلومات هذا الحساب')
            
            try:
                u = m.reply_to_message.from_user
                try:
                    u = c.get_users(u.id)
                except:
                    pass
                
                _name = ((u.first_name or '') + (' ' + u.last_name if u.last_name else '')).strip() or 'لا يوجد'
                _user = format_usernames(u)
                _rank = get_rank(u.id, m.chat.id)
                msgs = int(r.get(f'{Dev_FLER}{m.chat.id}:TotalMsgs:{u.id}') or 0)
                
                if not r.get(f'{m.chat.id}:TotalEDMsgs:{u.id}{Dev_FLER}'):
                    edits = 0
                else:
                    edits = int(r.get(f'{m.chat.id}:TotalEDMsgs:{u.id}{Dev_FLER}') or 0)
                
                create = get_creation_date(u.id)
                
                # تنسيق الرسالة بـ Custom Emoji
                text = f'''<b>👤 معلومات المستخدم</b>

<emoji id="5794164805065514131">⌯</emoji> يوزَر حسابَك ⌯ {_user} <emoji id="5891156376473836675">⌯</emoji>
<emoji id="5794085322400733645">⌯</emoji> عَدَد رسائلَك ⌯ {msgs} <emoji id="6030537810509828330">⌯</emoji>
<emoji id="5794280000383358988">⌯</emoji> رتبتَك ⌯ {_rank} <emoji id="5084979757905347540">⌯</emoji>
<emoji id="5794241397217304511">⌯</emoji> ايدي حسابَك ⌯ <code>{u.id}</code>
<emoji id="5793985348446984682">⌯</emoji> تَعديلاتَك ⌯ {edits} <emoji id="5769635757211784031">⌯</emoji>
<emoji id="5794324702402976226">⌯</emoji> انشاء حسابَك ⌯ {create}

<i>Made with ❤️</i>
'''
                
                # إنشاء أزرار ملونة بـ Custom Emoji
                keyboard = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            text="💬 الملف الشخصي",
                            callback_data=f"view_profile:{u.id}",
                            style="primary",
                            icon_custom_emoji_id="5794164805065514131"
                        ),
                        InlineKeyboardButton(
                            text="📊 الإحصائيات",
                            callback_data=f"view_stats:{u.id}",
                            style="success",
                            icon_custom_emoji_id="5794085322400733645"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="⚙️ الخيارات",
                            callback_data=f"view_options:{u.id}",
                            style="danger",
                            icon_custom_emoji_id="5794280000383358988"
                        )
                    ]
                ])
                
                return m.reply(text, reply_markup=keyboard)
            
            except Exception as e:
                print(f"Error in reply_id_handler: {e}")
                return m.reply(f'{k} حدث خطأ في جلب معلومات هذا المستخدم')


# معالج callbacks للأزرار
@Client.on_callback_query(filters.regex(r'^view_(profile|stats|options):(\d+)$'))
def handle_id_buttons(c, callback_query):
    k = r.get(f'{Dev_FLER}:botkey')
    data_parts = callback_query.data.split(':')
    action = data_parts[0].replace('view_', '')
    user_id = int(data_parts[1])
    
    try:
        user = c.get_users(user_id)
        
        if action == 'profile':
            response = f'''<b>👤 الملف الشخصي الكامل</b>

<b>الاسم:</b> {user.first_name} {user.last_name or ''}
<b>المعرف:</b> {format_usernames(user)}
<b>الايدي:</b> <code>{user.id}</code>
<b>الحالة:</b> {'محقق ✅' if user.is_verified else 'عادي'}

<i>Made with ❤️</i>
'''
        
        elif action == 'stats':
            msgs = int(r.get(f'{Dev_FLER}{callback_query.message.chat.id}:TotalMsgs:{user_id}') or 0)
            edits = int(r.get(f'{callback_query.message.chat.id}:TotalEDMsgs:{user_id}{Dev_FLER}') or 0)
            rank = get_rank(user_id, callback_query.message.chat.id)
            
            response = f'''<b>📊 الإحصائيات</b>

<b>عدد الرسائل:</b> {msgs:,}
<b>عدد التعديلات:</b> {edits}
<b>الرتبة:</b> {rank}

<i>Made with ❤️</i>
'''
        
        else:  # options
            response = f'''<b>⚙️ الخيارات المتاحة</b>

الأوامر المتاحة:
• <b>ايدي</b> - عرض معلومات المستخدم
• <b>كشف</b> - كشف معلومات مفصلة
• <b>افتار</b> - عرض الصورة الشخصية

<i>Made with ❤️</i>
'''
        
        callback_query.answer(response, show_alert=True)
    
    except Exception as e:
        print(f"Error in callback handler: {e}")
        callback_query.answer(f'{k} حدث خطأ في معالجة الطلب', show_alert=True)
