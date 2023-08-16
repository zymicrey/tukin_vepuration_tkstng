#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("26376042", cast=int)
    API_HASH = config("1f5343b0646645ca1eaf7c4759fc248f")
    BOT_TOKEN = config("6491987934:AAFd5aEByfzMbUnpTgzezQNAq83D5kQY-Bg")
    DEV = 1664850827
    OWNER = config("2036803347")
    ffmpegcode = ["-preset faster -c:v libx264 -s 854x480 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Anime Sensei' -metadata:s:v title="Anime Sensei" -metadata:s:a title="Anime Sensei" -metadata:s:s title="Anime Sensei" -pix_fmt yuv420p -crf 27 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://te.legra.ph/file/86e958f9fc0d7cbdf1a28.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
