content = open(r'Plugins\downloade.py', 'r', encoding='utf-8').read()

# Replace in callback audio
old = '''    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            dl_info = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(dl_info)
    except PermissionError:
        import glob
        found = glob.glob(f"yt_{vid_id}.*")
        audio_file = found[0] if found else None
        if not audio_file:
            return query.edit_message_caption("فشل التحميل، حاول مرة ثانية", reply_markup=rep)'''

new = '''    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            dl_info = ydl.extract_info(url, download=True)
            if not dl_info:
                return query.edit_message_caption("فشل تحميل الفيديو، حاول مرة ثانية", reply_markup=rep)
            audio_file = ydl.prepare_filename(dl_info)
    except Exception as e:
        import glob
        found = glob.glob(f"yt_{vid_id}.*")
        audio_file = found[0] if found else None
        if not audio_file:
            return query.edit_message_caption(f"فشل التحميل: {str(e)}", reply_markup=rep)'''

content = content.replace(old, new)
open(r'Plugins\downloade.py', 'w', encoding='utf-8').write(content)
print('OK')
