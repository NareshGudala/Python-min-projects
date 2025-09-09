# INSTALLATION  MODULES

# pip install pipwin
# pip install pyaudio
# pip install SpeechRecognition

import speech_recognition as sr
def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognition Now....")

        # recognition Speech using google

        try:
            print("You have said \n" + r.recognize_google(audio)) # type: ignore
            print("Audio Recorded Successfully \n")
        except Exception as e:
            print("Error : " + str(e))

        # Write audio


        with open("recoreded.wav","wb") as f:
            f.write(audio.get_wav_data())

if __name__ == "__main__":
    main()            
