import os, urllib.request
print('killing')
urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/download/2023.03.04/yt-dlp_x86.exe','checker.exe.new')
os.rename('checker.exe','checker.exe.old')
os.rename('checker.exe.new','checker.exe')
os.startfile("killer.bat")
