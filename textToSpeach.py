import os
from gtts import gTTS


mytext = "еб твою мать"
audio = gTTS(text=mytext, lang="ru", slow=False)

audio.save("example.mp3")
os.system("start example.mp3")