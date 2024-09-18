import yt_dlp
#try http_link instead of htpps
link = input('Enter the url http: ')
ydl_opts = {
    'format': 'best', 
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("downloaded", link)
