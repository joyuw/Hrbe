import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
import json

# استيراد redis للبيانات
from redis_client import r
from helpers.Ranks import get_rank
from helpers.get_create import get_creation_date

# قراءة التوكن من config
try:
    from config import token, Dev_FLER
except ImportError:
    token = "YOUR_TOKEN_HERE"
    Dev_FLER = token.split(':')[0]

# إنشاء البوت والـ Dispatcher
bot = Bot(token=token)
dp = Dispatcher()

# Custom Emoji IDs
EMOJI_IDS = {
    'start_1': '5794164805065514131',
    'end_1': '5891156376473836675',
    'start_2': '5794085322400733645',
    'end_2': '6030537810509828330',
    'start_3': '5794280000383358988',
    'end_3': '5084979757905347540',
    'start_4': '5794241397217304511',
    'end_4': None,
    'start_5': '5793985348446984682',
    'end_5': '5769635757211784031',
    'start_6': '5794324702402976226',
    'end_6': None,
}

def format_usernames(user):
    """تنسيق أسماء المستخدمين"""
    if user.username:
        return f"@{user.username}"
    return "لا يوجد معرف"

async def get_user_info(user_id: int, chat_id: int):
    """جلب معلومات المستخدم من Redis"""
    try:
        msgs = int(r.get(f'{Dev_FLER}{chat_id}:TotalMsgs:{user_id}') or 0)
    except:
        msgs = 0
    
    try:
        edits = int(r.get(f'{chat_id}:TotalEDMsgs:{user_id}{Dev_FLER}') or 0)
    except:
        edits = 0
    
    try:
        rank = get_rank(user_id, chat_id)
    except:
        rank = "غير معروف"
    
    try:
        create_date = get_creation_date(user_id)
    except:
        create_date = "غير متوفر"
    
    return {
        'msgs': msgs,
        'edits': edits,
        'rank': rank,
        'create_date': create_date
    }

def build_id_text(user: types.User, user_info: dict):
    """بناء رسالة الـ ID بـ Custom Emoji"""
    emoji_start_1 = f'<tg-emoji emoji-id="{EMOJI_IDS["start_1"]}">⌯</tg-emoji>'
    emoji_end_1 = f'<tg-emoji emoji-id="{EMOJI_IDS["end_1"]}">⌯</tg-emoji>'
    
    emoji_start_2 = f'<tg-emoji emoji-id="{EMOJI_IDS["start_2"]}">⌯</tg-emoji>'
    emoji_end_2 = f'<tg-emoji emoji-id="{EMOJI_IDS["end_2"]}">⌯</tg-emoji>'
    
    emoji_start_3 = f'<tg-emoji emoji-id="{EMOJI_IDS["start_3"]}">⌯</tg-emoji>'
    emoji_end_3 = f'<tg-emoji emoji-id="{EMOJI_IDS["end_3"]}">⌯</tg-emoji>'
    
    emoji_start_4 = f'<tg-emoji emoji-id="{EMOJI_IDS["start_4"]}">⌯</tg-emoji>'
    
    emoji_start_5 = f'<tg-emoji emoji-id="{EMOJI_IDS["start_5"]}">⌯</tg-emoji>'
    emoji_end_5 = f'<tg-emoji emoji-id="{EMOJI_IDS["end_5"]}">⌯</tg-emoji>'
    
    emoji_start_6 = f'<tg-emoji emoji-id="{EMOJI_IDS["start_6"]}">⌯</tg-emoji>'
    
    username = format_usernames(user)
    name = user.first_name or "لا يوجد"
    
    text = f'''<b>👤 معلومات المستخدم</b>

{emoji_start_1} يوزَر حسابَك ⌯ {username} {emoji_end_1}
{emoji_start_2} عَدَد رسائلَك ⌯ {user_info['msgs']} {emoji_end_2}
{emoji_start_3} رتبتَك ⌯ {user_info['rank']} {emoji_end_3}
{emoji_start_4} ايدي حسابَك ⌯ <code>{user.id}</code>
{emoji_start_5} تَعديلاتَك ⌯ {user_info['edits']} {emoji_end_5}
{emoji_start_6} انشاء حسابَك ⌯ {user_info['create_date']}

<i>Made with ❤️</i>
'''
    return text

def create_id_keyboard():
    """إنشاء لوحة المفاتيح ملونة بـ Custom Emoji"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💬 الملف الشخصي",
                    callback_data="view_profile"
                ),
                InlineKeyboardButton(
                    text="📊 الإحصائيات",
                    callback_data="view_stats"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ الخيارات",
                    callback_data="view_options"
                )
            ]
        ]
    )
    return keyboard

@dp.message(Command("id"))
@dp.message(F.text.in_(["ايدي", "ا", "id"]))
async def id_handler(message: types.Message):
    """معالج أمر الـ ID"""
    try:
        # إذا كان الرد على رسالة
        if message.reply_to_message and message.reply_to_message.from_user:
            user = message.reply_to_message.from_user
        else:
            user = message.from_user
        
        # جلب معلومات المستخدم
        user_info = await get_user_info(user.id, message.chat.id)
        
        # بناء الرسالة
        text = build_id_text(user, user_info)
        
        # إرسال الرسالة مع لوحة المفاتيح
        keyboard = create_id_keyboard()
        
        await message.reply(
            text=text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    
    except Exception as e:
        print(f"Error in id_handler: {e}")
        await message.reply("❌ حدث خطأ في جلب المعلومات")

@dp.callback_query(F.data == "view_profile")
async def handle_profile(callback: types.CallbackQuery):
    """معالج عرض الملف الشخصي"""
    try:
        user = callback.from_user
        text = f'''<b>👤 الملف الشخصي الكامل</b>

<b>الاسم:</b> {user.first_name} {user.last_name or ''}
<b>المعرف:</b> {format_usernames(user)}
<b>الايدي:</b> <code>{user.id}</code>
<b>الحالة:</b> {'محقق ✅' if user.is_premium else 'عادي'}

<i>Made with ❤️</i>
'''
        await callback.answer(text, show_alert=True)
    except Exception as e:
        print(f"Error in profile handler: {e}")
        await callback.answer("❌ حدث خطأ", show_alert=True)

@dp.callback_query(F.data == "view_stats")
async def handle_stats(callback: types.CallbackQuery):
    """معالج عرض الإحصائيات"""
    try:
        user_info = await get_user_info(callback.from_user.id, callback.message.chat.id)
        
        text = f'''<b>📊 الإحصائيات</b>

<b>عدد الرسائل:</b> {user_info['msgs']:,}
<b>عدد التعديلات:</b> {user_info['edits']}
<b>الرتبة:</b> {user_info['rank']}

<i>Made with ❤️</i>
'''
        await callback.answer(text, show_alert=True)
    except Exception as e:
        print(f"Error in stats handler: {e}")
        await callback.answer("❌ حدث خطأ", show_alert=True)

@dp.callback_query(F.data == "view_options")
async def handle_options(callback: types.CallbackQuery):
    """معالج عرض الخيارات"""
    try:
        text = '''<b>⚙️ الخيارات المتاحة</b>

الأوامر المتاحة:
• <b>ايدي</b> - عرض معلومات المستخدم
• <b>كشف</b> - كشف معلومات مفصلة
• <b>افتار</b> - عرض الصورة الشخصية

<i>Made with ❤️</i>
'''
        await callback.answer(text, show_alert=True)
    except Exception as e:
        print(f"Error in options handler: {e}")
        await callback.answer("❌ حدث خطأ", show_alert=True)

async def main():
    """تشغيل البوت"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("🚀 aiogram ID Bot started!")
    asyncio.run(main())
