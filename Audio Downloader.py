import youtube_dl, os
SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')

options = {
    'format':'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [my_hook],
    'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s'
}

while 1:
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([input('Paste Youtube Link: ')])
        