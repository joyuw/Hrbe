from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
from config import *
from helpers.Ranks import *

DEFAULT_MAZAD_TEXT = """<b>〔 𝙓 • 𝘽𝙇𝘼𝘾𝙆 〕</b>
المزاودة بَلَـشَت تكدَر تسَوم .
⌯ الزياده تدريجياً تخالف تاكل انذار . 
⌯ تسَوم وانت مو كَد السوم تتقَيَد
⌯ المزاد هنا : @zmaecv"""


_mazad_skip = (
    "تفعيل المزاد", "تعطيل المزاد", "تعديل المزاد",
    "تفعيل", "تعطيل", "تعديل", "رفع", "تنزيل", "حظر", "كتم", "طرد",
    "انذار", "حذف انذار", "الانذارات", "مسح الانذارات",
    "مسح", "الاوامر", "ايدي", "كشف", "كشف القيود", "الحظر", "الطرد",
    "الكتم", "الانذار", "الانذارات", "مسح الانذارات", "شنو يكول",
    "انطق", "انطقي", "غردي", "ابلاغ", "الرابط", "انشاء رابط",
    "تثبيت", "الغاء تثبيت", "كشف البوت", "كشف القيود",
    "الادمنيه", "المحظورين", "المقيدين", "مسح المحظورين",
    "مسح المقيدين", "تاك", "تاك للكل", "all", "تاج", "تاج للكل",
    "زواج", "طلاق", "طلقني", "طلكني", "زوجني", "جواز", "نسخ",
    "قفل", "فتح", "قفل ال", "فتح ال",
)

def _is_cmd(text):
    if not text:
        return False
    low = text.strip()
    for cmd in _mazad_skip:
        if low.startswith(cmd):
            return True
    return False


def _owner_check(user_id, chat_id):
    if user_id == 7285544053 or user_id == 7285544053:
        return True
    if user_id == int(Dev_FLER):
        return True
    if r.get(f'{user_id}:rankDEV2:{Dev_FLER}') or r.get(f'{user_id}:rankDEV:{Dev_FLER}'):
        return True
    if r.get(f'{chat_id}:rankGOWNER:{user_id}{Dev_FLER}') or r.get(f'{chat_id}:rankOWNER:{user_id}{Dev_FLER}'):
        return True
    return False

@Client.on_message(filters.group & filters.text, group=-5)
async def enable_mazad(c: Client, m: Message):
    if not m.from_user:
        return
    text = (m.text or '').strip()
    if text != 'تفعيل المزاد':
        return
    if not _owner_check(m.from_user.id, m.chat.id):
        return await m.reply("هذا الامر يخص (المالك وفوق) بس")

    r.set(f'mazad_enabled:{m.chat.id}:{Dev_FLER}', '1')
    if not r.get(f'mazad_text:{m.chat.id}:{Dev_FLER}'):
        r.set(f'mazad_text:{m.chat.id}:{Dev_FLER}', DEFAULT_MAZAD_TEXT)

    await m.reply("<b>تم تفعيل المزاد</b>")


@Client.on_message(filters.group & filters.text, group=-4)
async def disable_mazad(c: Client, m: Message):
    if not m.from_user:
        return
    text = (m.text or '').strip()
    if text != 'تعطيل المزاد':
        return
    if not _owner_check(m.from_user.id, m.chat.id):
        return await m.reply("هذا الامر يخص (المالك وفوق) بس")

    r.delete(f'mazad_enabled:{m.chat.id}:{Dev_FLER}')
    await m.reply("<b>تم تعطيل المزاد</b>")


@Client.on_message(filters.group & filters.text, group=-3)
async def edit_mazad_cmd(c: Client, m: Message):
    if not m.from_user:
        return
    text = (m.text or '').strip()
    if text != 'تعديل المزاد':
        return
    if not _owner_check(m.from_user.id, m.chat.id):
        return await m.reply("هذا الامر يخص (المالك وفوق) بس")

    r.set(f'mazad_edit:{m.from_user.id}:{m.chat.id}:{Dev_FLER}', '1')
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("❌ الغاء", callback_data=f"mazad_cancel:{m.from_user.id}:{m.chat.id}")]
    ])
    await m.reply("<b>ارسل الشكل الجديد للمزاد:</b>", reply_markup=kb)


@Client.on_callback_query(filters.regex("^mazad_cancel:"))
async def mazad_cancel_cb(c: Client, m):
    parts = m.data.split(":")
    user_id = int(parts[1])
    chat_id = int(parts[2])
    if m.from_user.id != user_id:
        return await m.answer("مو الامر مالك", show_alert=True)

    r.delete(f'mazad_edit:{user_id}:{chat_id}:{Dev_FLER}')
    await m.edit_message_text("<b>تم الغاء تعديل المزاد</b>")


@Client.on_message(filters.group & filters.text, group=9999)
async def mazad_edit_handler(c: Client, m: Message):
    if not m.from_user:
        return
    if r.get(f'mazad_edit:{m.from_user.id}:{m.chat.id}:{Dev_FLER}'):
        r.delete(f'mazad_edit:{m.from_user.id}:{m.chat.id}:{Dev_FLER}')
        r.set(f'mazad_text:{m.chat.id}:{Dev_FLER}', m.text.html)
        await m.reply("<b>تم تغيير كليشة المزاد</b>")


@Client.on_message(filters.group & ~filters.me, group=-10)
async def mazad_auto_reply(c: Client, m: Message):
    if m.from_user:
        return
    if not m.sender_chat:
        return
    if not r.get(f'mazad_enabled:{m.chat.id}:{Dev_FLER}'):
        return
    if _is_cmd(m.text):
        return

    text = r.get(f'mazad_text:{m.chat.id}:{Dev_FLER}')
    if text:
        await m.reply(text, parse_mode=ParseMode.HTML)
