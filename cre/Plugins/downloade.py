import yt_dlp, os, requests, re, time, wget, random, json 
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch as Y88F8
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
# from shazamio import Shazam
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand
from PIL import Image, ImageFilter


# shazam = Shazam()

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )
    
def Find(text):
  m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(m,text)  
  return [x[0] for x in url]

@Client.on_message(filters.text & filters.group, group=32)
def ytdownloaderHandler(c,m):
    k = r.get(f'{Dev_FLER}:botkey')
    channel = r.get(f'{Dev_FLER}:BotChannel') if r.get(f'{Dev_FLER}:BotChannel') else (c.me.username or 'RobinSource')
    Thread(target=yt_func,args=(c,m,k,channel)).start()
    
def yt_func(c,m,k,channel):
   if not m.from_user:  return False
   if not r.get(f'{m.chat.id}:enable:{Dev_FLER}'):
        return False 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_FLER}'):  return False
   if r.get(f'{m.chat.id}:mute:{Dev_FLER}') and not admin_pls(m.from_user.id,m.chat.id):  return False 
   if r.get(f'{m.from_user.id}:mute:{Dev_FLER}'):  return False 
   text = m.text
   bot_username = c.me.username or channel
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{bot_username}')
     ]]
   )

        
   
   if text.startswith('يوت '):
     if r.get(f'{m.chat.id}:disableYT:{Dev_FLER}'):  return
     if r.get(f':disableYT:{Dev_FLER}'):  return
     query = text.split(None,1)[1]
     loading_msg = m.reply('**صَبرَك هَسَه اجيبلَك طَـلَبَك ...**', parse_mode=ParseMode.MARKDOWN)
     
     results=Y88F8(query,max_results=1).to_dict()
     res = results[0]
     title = res['title']
     duration= int(time_to_seconds(res['duration']))
     duration_string = time.strftime('%M:%S', time.gmtime(duration))
     if ytdb.get(f'ytvideo{res["id"]}'):
        aud = ytdb.get(f'ytvideo{res["id"]}')
        duration_string = time.strftime('%M:%S', time.gmtime(aud["duration"]))
        loading_msg.delete()
        return m.reply_audio(aud["audio"],caption=f'@{bot_username} ~ {duration_string} ⏳',reply_markup=rep)
     url = f'https://youtu.be/{res["id"]}'
     vid_id = res["id"]
     # Step 1: get metadata only
     try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'cookiefile': 'cookies.txt'}) as ydl:
           info = ydl.extract_info(url, download=False)
     except Exception as e:
           loading_msg.delete()
           return m.reply(f'{k} فشل جلب معلومات الفيديو: {str(e)}', reply_markup=rep)
     if int(info.get('duration', 0)) > 32700:
        loading_msg.delete()
        return m.reply("صوت فوق 545 دقيقة ما اقدر انزله", reply_markup=rep)
     duration_string = time.strftime('%M:%S', time.gmtime(int(info['duration'])))
     # Step 2: download audio only with thumbnail
     ydl_ops = {
        "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio",
        "outtmpl": f"yt_{vid_id}.%(ext)s",
        "quiet": True,
        "no_warnings": True,
        "no_mtime": True,
        "writethumbnail": True,
        "cookiefile": "cookies.txt",
        "ignoreerrors": True,
        "prefer_ffmpeg": True,
     }
     try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
           dl_info = ydl.extract_info(url, download=True)
           if not dl_info:
              loading_msg.delete()
              return m.reply(f'{k} فشل تحميل الفيديو، حاول مرة ثانية', reply_markup=rep)
           audio_file = ydl.prepare_filename(dl_info)
     except Exception as e:
        import glob
        found = glob.glob(f"yt_{vid_id}.*")
        audio_file = found[0] if found else None
        if not audio_file:
           loading_msg.delete()
           return m.reply(f'{k} فشل التحميل: {str(e)}', reply_markup=rep)
     thumb = None
     try:
        thumb_file = f"yt_{vid_id}.jpg"
        if os.path.exists(thumb_file):
           thumb = thumb_file
        else:
           thumb_url = info.get('thumbnail', '')
           if thumb_url:
               thumb = wget.download(thumb_url, thumb_file)
     except:
        pass
     loading_msg.delete()
     a = m.reply_audio(
        audio_file,
        title=info.get('title', title),
        thumb=thumb,
        duration=int(info['duration']),
        caption=f'@{bot_username} ~ {duration_string} ⏳',
        performer=info.get('channel', info.get('uploader', '')),
        reply_markup=rep)
     if a and a.audio:
        ytdb.set(f'ytvideo{vid_id}', {"type":"audio", "audio":a.audio.file_id, "duration":a.audio.duration})
     try: os.remove(audio_file)
     except: pass
     if thumb:
        try: os.remove(thumb)
        except: pass
     return True

   if text.startswith('يوتيوب '):
     if r.get(f'{m.chat.id}:disableYT:{Dev_FLER}'):  return
     if r.get(f':disableYT:{Dev_FLER}'):  return
     query = text.split(None,1)[1]
     keyboard= []
     results=Y88F8(query,max_results=4).to_dict()
     for res in results:
       title = res['title']
       id = res['id']
       keyboard.append([InlineKeyboardButton (title, callback_data=f'{m.from_user.id}GET{id}')])     
     a = m.reply(f'{k} البحث ~ {query}',reply_markup=InlineKeyboardMarkup (keyboard), disable_web_page_preview=True)
     r.set(f'{a.id}:one_minute:{m.from_user.id}', 1, ex=60)
     return True

   if text.startswith('بحث ') or text.startswith('سيرش '):
     if r.get(f'{m.chat.id}:disableYT:{Dev_FLER}'):  return
     if r.get(f':disableYT:{Dev_FLER}'):  return
     query = text.split(None,1)[1]
     loading_msg = m.reply('**صَبرَك هَسَه اجيبلَك طَـلَبَك ...**', parse_mode=ParseMode.MARKDOWN)
     keyboard= []
     results=Y88F8(query,max_results=4).to_dict()
     for res in results:
       title = res['title']
       id = res['id']
       keyboard.append([InlineKeyboardButton (title, callback_data=f'{m.from_user.id}GET{id}')])     
     loading_msg.delete()
     a = m.reply(f'{k} البحث ~ {query}',reply_markup=InlineKeyboardMarkup (keyboard), disable_web_page_preview=True)
     r.set(f'{a.id}:one_minute:{m.from_user.id}', 1, ex=60)
     return True
  
   if text == "نسخة اليوتيوب" and m.from_user.id == 6168217372:
     if not ytdb.keys(): return m.reply("تخزين اليوتيوب فاضي")
     else:
        videos = []
        audios = []
        for key in ytdb.keys():
           get = {"key":key[0],"value":ytdb.get(key[0])}
           if get["value"]["type"] == "audio":
             audios.append(get)
           if get["value"]["type"] == "video":
             videos.append(get)
        id = random.randint(1,10000)
        if audios:
          with open(f"audios-{id}.json","w+") as f:
            f.write(json.dumps(audios, indent=4, ensure_ascii=False))
          m.reply_document(f"audios-{id}.json")
          os.remove(f"audios-{id}.json")
        if videos:
          with open(f"videos-{id}.json","w+") as f:
            f.write(json.dumps(videos, indent=4, ensure_ascii=False))
          m.reply_document(f"videos-{id}.json")
          os.remove(f"videos-{id}.json")
        return True

   if text.startswith('ساوند '):
     if r.get(f'{m.chat.id}:disableSound:{Dev_FLER}'):  return
     if r.get(f':disableYT:{Dev_FLER}'):  return
     #https://soundcloud.com
     query = text.split(None,1)[1]
     data = requests.get(f"https://m.soundcloud.com/search?q={query}")
     urls = re.findall(r'data-testid="cell-entity-link" href="([^"]+)', data.text)
     names = re.findall(r'<div class="Information_CellTitle__2KitR">([^<]+)', data.text)
     result = []
     for i in range(len(urls)): result.append({'name': names[i], 'url': f'{urls[i]}'})
     buttons = []
     btns = InlineKeyboardMarkup(buttons)
     count = 0
     for a in result:
       if count == 5:
         break
       url = a['url']
       buttons.append([
       InlineKeyboardButton (a['name'], switch_inline_query_current_chat=f'{url}#SOUND')
       ]
       )
       count += 1
     m.reply(f'{k} بحث الساوند ~ {query}', reply_markup=btns)
     return True
   
   if text.startswith('تيك '):
    if r.get(f'{m.chat.id}:disableTik:{Dev_FLER}'):  return
    if r.get(f':disableYT:{Dev_FLER}'):  return
    if Find(text):
      query = Find(text)[0]
    else:  return False
    
    loading = m.reply(f"{k} صبرك جاري التحميل ...")
    
    # Check for TikTok cookies file
    cookie_file = 'tiktok_cookies.txt' if os.path.exists('tiktok_cookies.txt') else None
    
    # Enhanced yt-dlp options for TikTok to bypass 429
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'cookiefile': cookie_file,
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.tiktok.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
        },
        'format': 'best[filesize<50M]/best',
        'outtmpl': 'tiktok_%(id)s.%(ext)s',
        'socket_timeout': 15,
        'retries': 10,
        'fragment_retries': 10,
        'n_threads': 8,
        'concurrent_fragment_downloads': 8,
        'skip_unavailable_fragments': True,
        'extractor_args': {
            'tiktok': {
                'api_hostname': ['api22-normal-useast2a.tiktokv.com'],
                'app_version': ['30.0.0'],
                'manifest_app_version': ['30.0.0'],
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    }
    
    try:
        # First try: extract info without download
        with yt_dlp.YoutubeDL({**ydl_opts, 'download': False, 'cookiefile': 'cookies.txt'}) as ytdl:
            vid_data = ytdl.extract_info(query, download=False)
        
        if not vid_data:
            loading.delete()
            return m.reply(f"{k} ما قدرت أجلب بيانات المقطع، جرب رابط ثاني.")
        
        title = vid_data.get('fulltitle', vid_data.get('title', 'TikTok'))
        duration = int(vid_data.get('duration', 0))
        string_d = time.strftime('%M:%S', time.gmtime(duration)) if duration else '0:00'
        views = vid_data.get('view_count', 0) or 0
        likes = vid_data.get('like_count', 0) or 0
        comments = vid_data.get('comment_count', 0) or 0
        reposts = vid_data.get('repost_count', 0) or 0
        
        caption = f"`{title}`\n{k} طول المقطع : {string_d}\n{k} المشاهدات : {views:,}\n{k} اللايكات : {likes:,}\n{k} الكومنت : {comments:,}\n{k} الاكسبلور : {reposts:,}\n\n~ @{channel}"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("RoBinSouRce", url="https://t.me/RobinSource")]]
        )
        
        # Try to get direct playable URL from formats
        direct_url = None
        formats = vid_data.get('formats', [])
        if formats:
            # Sort by quality and pick best mp4
            for fmt in sorted(formats, key=lambda x: x.get('height', 0) or 0, reverse=True):
                if fmt.get('url') and 'mp4' in fmt.get('ext', ''):
                    direct_url = fmt['url']
                    break
            # Fallback to any URL
            if not direct_url:
                for fmt in formats:
                    if fmt.get('url'):
                        direct_url = fmt['url']
                        break
        
        # Try sending via direct URL first (no download)
        if direct_url:
            try:
                m.reply_video(direct_url, caption=caption, reply_markup=reply_markup)
                loading.delete()
                return True
            except Exception as e:
                print(f"Direct URL failed: {e}")
        
        # Second try: download then upload
        download_opts = {**ydl_opts, 'download': True}
        with yt_dlp.YoutubeDL({**download_opts, 'cookiefile': 'cookies.txt'}) as ytdl:
            vid_data = ytdl.extract_info(query, download=True)
            file_name = ytdl.prepare_filename(vid_data)
        
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            m.reply_video(file_name, caption=caption, reply_markup=reply_markup)
            os.remove(file_name)
            loading.delete()
            return True
        else:
            loading.delete()
            return m.reply(f"{k} تم التحميل لكن الملف فاضي أو ما موجود.")
        
    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        print(f"TikTok download error: {error_msg}")
        loading.delete()
        if '429' in error_msg or 'Too Many Requests' in error_msg:
            return m.reply(f"{k} تم حظر التحميل مؤقتاً من TikTok (كثرة طلبات).\n{k} جرب بعد فترة أو استخدم رابط من تطبيق آخر.")
        elif '404' in error_msg or 'Not Found' in error_msg:
            return m.reply(f"{k} المقطع محذوف أو الرابط غلط.")
        elif 'Private' in error_msg or 'private' in error_msg:
            return m.reply(f"{k} المقطع خاص وما أقدر أحمله.")
        elif 'getaddrinfo' in error_msg or 'Failed to resolve' in error_msg or 'NameResolutionError' in error_msg:
            return m.reply(f"{k} عذراً، ما قدرت أوصل لسيرفر TikTok (مشكلة انترنت/DNS).\n{k} جرب بعد شوي أو شيك على اتصالك.")
        else:
            return m.reply(f"{k} عذراً، ما قدرت أحمل المقطع.\n{k} السبب: {error_msg[:100]}")
    except Exception as e:
        print(f"TikTok unexpected error: {e}")
        loading.delete()
        return m.reply(f"{k} صار خطأ غير متوقع أثناء التحميل، جرب مرة ثانية.")

   if text.endswith(' #AUDIO'):
    find = Find(text)
    if find:
     url = find[0]
     if 'soundcloud' in url:
       if r.get(f'{m.chat.id}:disableSound:{Dev_FLER}'):  return
       if r.get(f':disableYT:{Dev_FLER}'):  return
       id = url.split('soundcloud.com/')[1]
       if sounddb.get(f'{id}:sound'):
          return m.reply_audio(sounddb.get(f'{id}:sound'))
       # Removed cookies/oauth2 parameters
       with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt', 'extract_flat': False, 'n_threads': 8, 'concurrent_fragment_downloads': 8, 'fragment_retries': 10, 'retries': 10, 'ignoreerrors': True}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=False)
           if int(ytdl_dataa['duration']) > 155555555:
              return m.reply('مقطع اكثر من ٢٥ دقيقة مقدر انزله')
       # Removed cookies/oauth2 parameters
       with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt', 'extract_flat': False, 'n_threads': 8, 'concurrent_fragment_downloads': 8, 'fragment_retries': 10, 'retries': 10, 'ignoreerrors': True}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=True)
           file_name = ytdl.prepare_filename(ytdl_dataa)
       title = ytdl_dataa['title']
       a = m.reply_audio(file_name,title=title, performer=f'@{channel}', duration=int(ytdl_dataa['duration']))       
       sounddb.set(f'{id}:sound',a.audio.file_id)
       os.remove(file_name)
       return True
   
   if text.endswith(' #VOICE'):
    find = Find(text)
    if find:
     url = find[0]
     if 'soundcloud' in url:
       if r.get(f'{m.chat.id}:disableSound:{Dev_FLER}'):  return
       if r.get(f':disableYT:{Dev_FLER}'):  return
       idd = url.split('soundcloud.com/')[1]
       if sounddb.get(f'{idd}:soundVoice'):
          return m.reply_voice(sounddb.get(f'{idd}:soundVoice'))
       # Removed cookies/oauth2 parameters
       with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt', 'extract_flat': False, 'n_threads': 8, 'concurrent_fragment_downloads': 8, 'fragment_retries': 10, 'retries': 10, 'ignoreerrors': True}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=False)
           if int(ytdl_dataa['duration']) > 55555252:
              return m.reply('مقطع اكثر من ٢٥ دقيقة مقدر انزله')
       # Removed cookies/oauth2 parameters
       with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt', 'extract_flat': False, 'n_threads': 8, 'concurrent_fragment_downloads': 8, 'fragment_retries': 10, 'retries': 10, 'ignoreerrors': True}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=True)
           file_name = ytdl.prepare_filename(ytdl_dataa)
       id = random.randint(1,100)
       os.rename(file_name, f"zaid{id}.mp3")
       os.system(f'{FFMPEG_BIN} -i zaid{id}.mp3 -ac 1 -strict -2 -codec:a libopus -b:a 128k -vbr off -ar 24000 zaid{id}.ogg')
       a = m.reply_voice(f"zaid{id}.ogg")       
       sounddb.set(f'{idd}:soundVoice',a.voice.file_id)
       os.remove(f"zaid{id}.mp3")
       os.remove(f"zaid{id}.ogg")
       return True
   
   find = Find(text)
   if find:
     url = find[0]
     if 'soundcloud' in url:
       if r.get(f'{m.chat.id}:disableSound:{Dev_FLER}'):  return
       if r.get(f':disableYT:{Dev_FLER}'):  return
       id = url.split('soundcloud.com')[1]
       return m.reply(f"@{channel} - ☁️",reply_markup=InlineKeyboardMarkup ([
       [InlineKeyboardButton ("اضغط هنا لاختيار صيغة التحميل", switch_inline_query_current_chat=f'{id}#SOUND')],
       [InlineKeyboardButton ("☁️", url=f't.me/{channel}')],
       ]))
       
       
     
@Client.on_message(filters.regex("^شازام$") & filters.group)
async def shazamFunc(c,m):
   if r.get(f'{m.chat.id}:disableShazam:{Dev_FLER}'):  return False
   if m.reply_to_message and (m.reply_to_message.audio or m.reply_to_message.voice or m.reply_to_message.video):
     if m.reply_to_message.audio:
       duration=m.reply_to_message.audio.duration if m.reply_to_message.audio.duration else 301
       fileSize=m.reply_to_message.audio.file_size
     if m.reply_to_message.voice:
       duration=m.reply_to_message.voice.duration if m.reply_to_message.voice.duration else 301
       fileSize=m.reply_to_message.voice.file_size
     if m.reply_to_message.video:
       duration=m.reply_to_message.video.duration if m.reply_to_message.video.duration else 301
       fileSize=m.reply_to_message.video.file_size
     if duration > 300:
       return await m.reply("🧚‍♀️ مدة المقطع أكثر من 5 دقايق ..")
     if fileSize > 26214400:
       return await m.reply("🧚‍♀️ حجم المقطع أكثر من 25 ميجابايت ..")
     id = random.randint(1,1000)
     msg = await m.reply("جاري المعالجة ...")
     audio = await m.reply_to_message.download(f'./shazam{id}.ogg')
     out = await shazam.recognize_song(f'shazam{id}.ogg')
     os.remove(f'shazam{id}.ogg')
     await msg.delete()
     if not out["matches"]:
       return await m.reply("فشل بالتعرف على الصوت")
     else:
       title = out["track"]["title"]
       author = out["track"]["subtitle"]
       try:
         photo = out["track"]["images"]["background"]
       except:
         photo = "https://telegra.ph/file/49ace69e7c43c0041fb63.jpg"
       k = r.get(f'{Dev_FLER}:botkey')
       channel = r.get(f'{Dev_FLER}:BotChannel') if r.get(f'{Dev_FLER}:BotChannel') else (c.me.username or 'RobinSource')
       url = out["track"]["url"]
       TEXT = f"""
{k} اسم الصوت ( [{title}]({url}) )
{k} اسم الفنان : {author}
"""           
       key = InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️",url=f"t.me/{channel}")]])
       await m.reply_photo(
         photo,caption=TEXT,reply_markup=key)
       
@Client.on_message(filters.regex("^شازام ") & filters.group)
async def shazamLyrics(c,m):
   if r.get(f'{m.chat.id}:disableShazam:{Dev_FLER}'):  return False
   query = m.text.split(None,1)[1]
   out = await shazam.search_track(query=query, limit=1)
   if not out:
     return await m.reply("فشل العثور")
   else:
    try:
     key = int(out["tracks"]["hits"][0]["key"])
     title = out["tracks"]["hits"][0]["heading"]["title"][:35]
     author = out["tracks"]["hits"][0]["heading"]["subtitle"]
     url = out["tracks"]["hits"][0]["url"]
     track_id = key
     about_track = await shazam.track_about(track_id=track_id)
     text=about_track["sections"][1]["text"]
     lyrics=""
     for tt in text:
       lyrics+=tt+"\n"
     return await m.reply(lyrics[:4096],reply_markup=InlineKeyboardMarkup (
       [[InlineKeyboardButton (f"{title} - {author}",url=url)]]
     )
     )
    except:
     return await m.reply("فشل العثور")
     
@Client.on_inline_query(filters.regex("SOUND"))
async def SoundCloud(c, query):
  url = query.query.split("#SOUND")[0]
  channel = r.get(f'{Dev_FLER}:BotChannel') if r.get(f'{Dev_FLER}:BotChannel') else (c.me.username or 'RobinSource')
  if url.count('/') > 1:
    await query.answer(
        results=[           
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - صوت",
                thumb_url='https://t.me/D7BotResources/161',
                description='~ @RobinSource ',
                url=f'https://t.me/{channel}',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://soundcloud.com{url} #AUDIO',disable_web_page_preview=True)
            ),
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - بصمة",
                thumb_url='https://t.me/D7BotResources/163',
                description='~ @RobinSource ',
                url=f'https://t.me/{channel}',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://soundcloud.com{url} #VOICE',disable_web_page_preview=True)
            ),
        ],
        cache_time=1
        )
  else:
    await query.answer(
        results=[           
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - صوت",
                thumb_url='https://t.me/D7BotResources/161',
                description='~ @RobinSource ',
                url=f'https://t.me/{channel}',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://on.soundcloud.com{url} #AUDIO',disable_web_page_preview=True)
            ),
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - بصمة",
                thumb_url='https://t.me/D7BotResources/163',
                description='~ @RobinSource ',
                url=f'https://t.me/{channel}',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://on.soundcloud.com{url} #VOICE',disable_web_page_preview=True)
            ),
        ],
        cache_time=1
        )


    
@Client.on_callback_query(filters.regex("GET"))
def get_info(c,query):
    Thread(target=getInfo,args=(c,query)).start()

def getInfo(c, query):
    user_id = query.data.split("GET")[0]
    vid_id = query.data.split("GET")[1]
    if not query.from_user.id == int(user_id):
      return
    if not r.get(f'{query.message.id}:one_minute:{user_id}'):
      k = r.get(f'{Dev_FLER}:botkey')
      query.answer(f'{k} مر على البحث اكثر من دقيقة ابحث مرة ثانية',show_alert=True)
      return query.message.delete()
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_FLER}'):  return
    if r.get(f':disableYT:{Dev_FLER}'):  return
    query.message.delete()
    bot_username = c.me.username
    url = f'https://youtu.be/{vid_id}'
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'cookiefile': 'cookies.txt'}) as ydl:
            _info = ydl.extract_info(url, download=False)
        photo = _info.get('thumbnail', 'https://telegra.ph/file/49ace69e7c43c0041fb63.jpg')
    except:
        photo = 'https://telegra.ph/file/49ace69e7c43c0041fb63.jpg'
    reply_markup = InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton ("♫ ملف صوتي", callback_data=f'{user_id}AUDIO{vid_id}'),
          InlineKeyboardButton ("❖ فيديو", callback_data=f'{user_id}VIDEO{vid_id}'),
        ],
        [
          InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{bot_username}')
        ]
      ]
    )
    query.message.reply_to_message.reply_photo(
       photo,
       caption=f'@{bot_username} ~ {url}',
       reply_markup=reply_markup
    )
    

@Client.on_callback_query(filters.regex("AUDIO"))
async def get_audii(c, query):
    Thread(target=audio_down,args=(c,query)).start()


def audio_down(c, query):
    user_id = query.data.split("AUDIO")[0]
    vid_id = query.data.split("AUDIO")[1]
    if not query.from_user.id == int(user_id):
      return False
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_FLER}'):  return
    if r.get(f':disableYT:{Dev_FLER}'):  return
    bot_username = c.me.username
    rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{bot_username}')
     ]]
    )
    if ytdb.get(f'ytvideo{vid_id}'):
       aud = ytdb.get(f'ytvideo{vid_id}')
       query.edit_message_caption(f"@{bot_username} :)", reply_markup=rep)
       duration= aud["duration"]
       sec = time.strftime('%M:%S', time.gmtime(duration))
       return query.message.reply_audio(aud["audio"],caption=f'@{bot_username} ~ ⏳ {sec}')       
    url = f'https://youtu.be/{vid_id}'
    query.edit_message_caption("جاري التحميل ..", reply_markup=rep)
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'cookiefile': 'cookies.txt', 'format': 'best'}) as ydl:
            info = ydl.extract_info(url, download=False)
    except:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'cookiefile': 'cookies.txt'}) as ydl:
            info = ydl.extract_info(url, download=False)
    if int(info.get('duration', 0)) > 32700:
        return query.edit_message_caption("صوت اكثر من 545 دقيقة مقدر انزله", reply_markup=rep)
    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio",
        "outtmpl": f"yt_{vid_id}.%(ext)s",
        "quiet": True,
        "no_warnings": True,
        "no_mtime": True,
        "writethumbnail": True,
        "cookiefile": "cookies.txt",
        "ignoreerrors": True,
        "prefer_ffmpeg": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            dl_info = ydl.extract_info(url, download=True)
            if not dl_info:
                return query.edit_message_caption("فشل تحميل الفيديو، حاول مرة ثانية", reply_markup=rep)
            audio_file = ydl.prepare_filename(dl_info)
    except Exception as e:
        import glob
        found = glob.glob(f"yt_{vid_id}.*")
        audio_file = found[0] if found else None
        if not audio_file:
            return query.edit_message_caption(f"فشل التحميل: {str(e)}", reply_markup=rep)
    thumb = None
    try:
        thumb_file = f"yt_{vid_id}.jpg"
        if os.path.exists(thumb_file):
           thumb = thumb_file
    except:
        pass
    query.edit_message_caption("✈️✈️✈️✈️✈️", reply_markup=rep)
    duration = int(info['duration'])
    sec = time.strftime('%M:%S', time.gmtime(duration))
    a = query.message.reply_audio(
      audio_file,
      title=info['title'],
      thumb=thumb,
      duration=int(info['duration']),
      performer=info['channel'],
      caption=f'@{bot_username} ~ ⏳ {sec}',
    )
    query.edit_message_caption(f"@{bot_username} :)", reply_markup=rep)    
    if a and a.audio:
        ytdb.set(f'ytvideo{vid_id}',{"type":"audio","audio":a.audio.file_id,"duration":a.audio.duration})
    try: os.remove(audio_file)
    except: pass
    if thumb:
        try: os.remove(thumb)
        except: pass


@Client.on_callback_query(filters.regex("VIDEO"))
def get_video(c, query):
   Thread(target=video_down,args=(c,query)).start()

def video_down(c, query):
    user_id = query.data.split("VIDEO")[0]
    vid_id = query.data.split("VIDEO")[1]
    if not query.from_user.id == int(user_id):
      return False
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_FLER}'):  return
    if r.get(f':disableYT:{Dev_FLER}'):  return
    bot_username = c.me.username
    rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{bot_username}')
     ]]
    )
    if ytdb.get(f'ytvideoV{vid_id}'):
       vid = ytdb.get(f'ytvideoV{vid_id}')
       query.edit_message_caption(f"@{bot_username} :)", reply_markup=rep)
       duration=vid["duration"]
       sec = time.strftime('%M:%S', time.gmtime(duration))
       return query.message.reply_video(vid["video"],caption=f'@{bot_username} ~ ⏳ {sec}')
    url = f'https://youtu.be/{vid_id}'
    query.edit_message_caption("جاري التحميل ..", reply_markup=rep)
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'cookiefile': 'cookies.txt', 'format': 'best'}) as ydl:
            info = ydl.extract_info(url, download=False)
    except:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'cookiefile': 'cookies.txt'}) as ydl:
            info = ydl.extract_info(url, download=False)
    if int(info['duration']) > 1555555555:
      return query.edit_message_caption("فيديو اكثر من 25 دقيقة مقدر انزله",reply_markup=rep)
    # Removed cookies/oauth2 parameters
    ydl_opts = {
        "format": "bestvideo[ext=mp4][vcodec!=av01][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
        "cookiefile": "cookies.txt",
        "n_threads": 8,
        "concurrent_fragment_downloads": 8,
        "fragment_retries": 10,
        "retries": 10,
        "ignoreerrors": True,
    }
    with YoutubeDL({**ydl_opts, 'cookiefile': 'cookies.txt'}) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
        file_name = ytdl.prepare_filename(ytdl_data)
    query.edit_message_caption("✈️✈️✈️✈️✈️", reply_markup=rep)
    duration= int(info['duration'])
    sec = time.strftime('%M:%S', time.gmtime(duration))
    a = query.message.reply_video(
      file_name,
      duration=int(info['duration']),
      caption=f'@{channel} ~ ⏳ {sec}',
    )
    query.edit_message_caption(f"@{channel} :)", reply_markup=rep)    
    ytdb.set(f'ytvideoV{vid_id}',{"type":"video","video":a.video.file_id,"duration":a.video.duration})
    os.remove(file_name)