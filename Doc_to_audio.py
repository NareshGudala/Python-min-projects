from gtts import gTTS
from playsound import playsound

#path to the text file
text_file = 'speech.txt'

# Read the content of the text file
with open(text_file, 'r') as file:
    text = file.read()

# set language and convert text to speech
language = 'te'
speech = gTTS(text = text, lang = 'te', slow = False)

#save the speech to an audio file
audio_file = 'speech.mp3'
speech.save(audio_file) 

# PLay the audio file
playsound(audio_file)
print("------------PLAY SOUND----------------")



'''
INPUT:

(Doc_to_audio.txt):
Python is a high-level, interpreted, object-oriented programming language known for its readability and versatility. 
It was created by Guido van Rossum and first released in 1991. The language is named after the British comedy group Monty Python.

'''
