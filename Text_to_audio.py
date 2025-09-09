# pip install gtts
# pip install playsound
# language (en = english)

from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = 'en'
# sp = gTTS(text="Hi Naresh and Welcome To Hyderabad",lang=language,slow=True)

sp = gTTS(text="Hai Naresh Welcome to Hyderabad",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("-----------PLAY MUSIC-----------")


"""

Available Languages 
You can check the available languages using the gtts.lang.tts_langs function:

# from gtts.lang import tts_langs

# # Get a dictionary of supported languages
# languages = tts_langs()
# print(languages)

"""

