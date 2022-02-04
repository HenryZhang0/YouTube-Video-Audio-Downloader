from threading import Thread
import youtube_dl
import os
import asyncio
SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Video_Downloads'

filename = SAVE_PATH+"/baz.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')


options = {
    'format': 'bestvideo',
    'progress_hooks': [my_hook],
    'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s'
}


def download(link):
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download(link)
        except:
            print("Invalid link.")
            print("Paste link:")


def main():
    link = input("Paste link: ").split(" ")
    t1 = Thread(target=download, args = [link])
    t2 = Thread(target=main)
    t1.start()
    t2.start()


if __name__ == "__main__":
    print("----YouTube Video Downloader----\n(paste links even during another download)")
    main()
