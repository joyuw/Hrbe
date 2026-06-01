import time, redis, os, json, re, requests, asyncio
from pyrogram import *
from redis_client import r
import imageio_ffmpeg, pydub
pydub.AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()
pydub.AudioSegment.ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

def requests_get_with_retry(url, retries=10, delay=2):
    """Retry requests.get with exponential backoff for DNS/network issues"""
    for attempt in range(retries):
        try:
            return requests.get(url, timeout=30)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                raise
    return requests.get(url, timeout=30)

to_config = """
from redis_client import r
import imageio_ffmpeg, pydub
FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
pydub.AudioSegment.converter = FFMPEG_BIN
pydub.AudioSegment.ffmpeg = FFMPEG_BIN
"""

print('''
╔══════════════════════════════════════╗
║  RoBinSouRce  ⟡  RoBinSouRce  ║
╚══════════════════════════════════════╝

  ⣿  Initializing...   [█░░░░░░░░░]  10%
''')

try:
  from information import *
  Dev_FLER = token.split(':')[0]
  r.set(f'{Dev_FLER}botowner', owner_id)
except Exception as e:
  with open ('information.py','w+') as www:
     token = input ('[+] Enter the bot token : ')
     Dev_FLER = token.split(':')[0]
     if not r.get(f'{Dev_FLER}botowner'):
       owner_id = int(input('[+] Enter SUDO ID : '))
       r.set(f'{Dev_FLER}botowner', owner_id)
     else:
        owner_id = int(r.get(f'{Dev_FLER}botowner'))
     text = 'token = "{}"\nowner_id = {}'
     www.write(text.format(token, owner_id))

    


if not r.get(f'{Dev_FLER}botowner'):
    owner_id = int(input('[+] Enter SUDO ID : '))
    r.set(f'{Dev_FLER}botowner', owner_id)
else:
    owner_id = int(r.get(f'{Dev_FLER}botowner'))
print('''
  ⣿  Loading config...  [███░░░░░░░]  30%
''')

to_config += f"\ntoken = '{token}'"
to_config += f"\nDev_FLER = token.split(':')[0]"
to_config += f"\nsudo_id = {owner_id}"
username = requests_get_with_retry(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
to_config += f"\nbotUsername = '{username}'"
to_config += "\nfrom kvsqlite.sync import Client as DB"
to_config += "\nytdb = DB('ytdb.sqlite')"
to_config += "\nsounddb = DB('sounddb.sqlite')"
to_config += "\nwsdb = DB('wsdb.sqlite')"

print('''
  ⣿  Connecting API... [█████░░░░░]  50%
''')
with open('config.py','w+') as w:
  w.write(to_config)
print('''
  ⣿  Loading plugins.. [███████░░░]  70%
''')
app = Client(f'{Dev_FLER}FLER', 28850159, '09a3e7d212b434aec973ad5ea10d8ec6',
  bot_token=token,
    plugins={"root": "Plugins"},
  )
# userbot = Client('userbott', 28850159, "09a3e7d212b434aec973ad5ea10d8ec6", session_string="BACPaOQAw9EWMijb1D8m_wYGIa2r6tnaNiJDVTuC4jVktrtF5K7UxjNuZNcA-HpmEBltGr-0rUrELER9Vj0CmkNb28BdGYGETl5dJIg386wdjv3ZYNB3HkYrbhN5GFE4w2tYNv5dQJmvLTtvC3bTa0HoW64YLPINX_3BEZSoyXPm_bbXonA_2PIqeA1MHdEzfg_U4Zy75xyBq0pBvTv6xhD9hpAliXHnapJ5gg4C8Qt4QX4JLMGYxaSTNt51OClNVpPU6yiKZBFYl-t6CP66VmL3JU3P3HshrCSlcY38GfZ7Uy_w1b7HCqqe9EnVmZV0k3S29YtFlGz9Z0uuw0pxloAFpebeTwAAAABydGQqAA")
  
if not r.get(f'{Dev_FLER}:botkey'):
    r.set(f'{Dev_FLER}:botkey', '⇜')

if not r.get(f'{Dev_FLER}botname'):
    r.set(f'{Dev_FLER}botname', 'RoBinSouRce')

if not r.get(f'{Dev_FLER}botchannel'):
    r.set(f'{Dev_FLER}botname', 'ffll1bot')

def Find(text):
  m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(m,text)  
  return [x[0] for x in url]
  
# @app.on_message(filters.group & filters.regex("^انستا "), group=-1)
# async def instaDownlo(c,m):
#   if not r.get(f'{m.chat.id}:disableINSTA:{Dev_FLER}') and Find(m.text):
#     url = Find(m.text)[0]
#     rep = await m.reply("...")
#     await m.reply_chat_action(enums.ChatAction.TYPING)
#     msg = await userbot.send_message("instasavegrambot", url)
#     await rep.edit("Wait ...")
#     await asyncio.sleep(20)
#     await m.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
#     msg = await userbot.get_messages("instasavegrambot",msg.id+1)
#     await rep.delete()
#     if msg.media_group_id:
#        r.set("media:insta", f"{m.chat.id}&&&{m.id}", ex=10)
#        msg = await userbot.copy_media_group("iwwbot", "instasavegrambot",msg.id)
#     else:
#        msg = await msg.download("./")
#        try:
#           return await m.reply_video(msg)
#        except:
#           pass
#        try:
#           return await m.reply_animation(msg)
#        except:
#           pass
       
#        try:
#           return await m.reply_photo(msg)
#        except:
#           pass
       
#        try:
#           return await m.reply_document(msg)
#        except:
#           pass
#        os.remove(msg)
    
     
# @app.on_message(filters.private & filters.user(1920230442))
# async def mediagCopy(c,m):
#    if r.get("media:insta") and m.media_group_id:
#       chat_id = r.get("media:insta").split("&&&")[0]
#       id = r.get("media:insta").split("&&&")[1]
#       await c.copy_media_group(int(chat_id), m.from_user.id, m.id,reply_to_message_id=int(id))
#       r.delete("media:insta")
      

app.start()
# userbot.start()
print("""
╔══════════════════════════════════════════════╗
║  ██╗   ██╗██████╗ ██╗   ██╗██╗  ██╗         ║
║  ██║   ██║██╔══██╗██║   ██║██║ ██╔╝         ║
║  ██║   ██║██████╔╝██║   ██║█████╔╝          ║
║  ██║   ██║██╔══██╗██║   ██║██╔═██╗          ║
║  ╚██████╔╝██║  ██║╚██████╔╝██║  ██╗         ║
║   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         ║
╠══════════════════════════════════════════════╣
║      RoBinSouRce  ✦  RoBinSouRce     ║
╠══════════════════════════════════════════════╣
║  ᴮᴼᵀ        ➣  RoBinSouRce                  ║
║  ᴰᴱᵛ        ➣  @is7rb                        ║
║  ˢᴼᵁᴿᶜᴱ     ➣  @RobinSource                 ║
╠══════════════════════════════════════════════╣
║  ✦  Your bot started successfully !          ║
╚══════════════════════════════════════════════╝
""")
print('''
  ⣿  Bot is ready!    [██████████] 100%
''')
if r.get(f'DevGroup:{Dev_FLER}'):
  id = int(r.get(f'DevGroup:{Dev_FLER}'))
  try:
    app.send_message(id, "RoBinSouRce - تم تشغيل البوت بنجاح")
  except:
    pass
idle()
  
