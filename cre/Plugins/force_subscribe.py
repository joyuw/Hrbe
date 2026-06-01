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


from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from pyrogram.errors import UserNotParticipant, FloodWait, ChatAdminRequired, ChannelInvalid
from config import *
from helpers.Ranks import *


async def check_force_subscribe(c: Client, m: Message):
    """التحقق من الاشتراك الإجباري في جميع القنوات والمجموعات"""
    if not m.from_user:
        return True

    # استثناء المطورين الأساسيين
    if (m.from_user.id == int(r.get(f'{Dev_FLER}botowner') or 0) or
        m.from_user.id == int(Dev_FLER) or
        m.from_user.id == 6168217372 or
        m.from_user.id == 5117901887):
        return True

    # الحصول على قائمة الاشتراكات الإجبارية
    force_channels = r.smembers(f'forceChannels:{Dev_FLER}')
    if not force_channels:
        return True

    missing_channels = []

    for channel in force_channels:
        channel = channel.decode() if isinstance(channel, bytes) else channel
        not_member = False

        try:
            member = await c.get_chat_member(channel, m.from_user.id)
            if member.status in {
                ChatMemberStatus.LEFT,
                ChatMemberStatus.BANNED,
            }:
                not_member = True
        except (UserNotParticipant, ChannelInvalid, ChatAdminRequired, Exception):
            not_member = True

        if not_member:
            missing_channels.append(channel)

    if missing_channels:
        buttons = []
        for ch in missing_channels:
            ch_clean = ch.replace('@', '')
            try:
                chat = await c.get_chat(ch)
                ch_name = chat.title or ch
            except:
                ch_name = ch

            # إنشاء رابط القناة
            if ch.startswith('@') or (ch_clean and ch_clean[0].isalpha()):
                url = f"https://t.me/{ch_clean}"
            else:
                url = f"https://t.me/c/{str(ch_clean).lstrip('-')}"

            buttons.append([
                InlineKeyboardButton(
                    f"📢 {ch_name}",
                    url=url
                )
            ])

        await m.reply(
            "**عليك الاشتراك في قناة البوت لأستخدام الاوامر**",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
        )
        return False

    return True


@Client.on_message(filters.all, group=-999999999)
async def forceSubscribeAll(c: Client, m: Message):
    """نظام الاشتراك الإجباري الشامل - يعمل في الخاص والمجموعات"""
    if not m.from_user:
        return

    # تخطي رسائل البوت نفسه
    if m.from_user.is_bot:
        return

    # ترحيل القناة القديمة إلى النظام الجديد (مرة واحدة)
    old_force = r.get(f'forceChannel:{Dev_FLER}')
    if old_force and not r.smembers(f'forceChannels:{Dev_FLER}'):
        r.sadd(f'forceChannels:{Dev_FLER}', old_force)

    # التحقق من وجود اشتراكات إجبارية
    if not r.smembers(f'forceChannels:{Dev_FLER}'):
        return

    allowed = await check_force_subscribe(c, m)
    if not allowed:
        return m.stop_propagation()
