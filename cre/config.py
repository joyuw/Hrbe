
from redis_client import r
import imageio_ffmpeg, pydub
FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
pydub.AudioSegment.converter = FFMPEG_BIN
pydub.AudioSegment.ffmpeg = FFMPEG_BIN

token = '8374906362:AAE4kFWIXQ5RjrG9xpC6hbAjdP-4PbB7QVI'
Dev_FLER = token.split(':')[0]
sudo_id = 7182427468
botUsername = 'X_B6bot'
from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')