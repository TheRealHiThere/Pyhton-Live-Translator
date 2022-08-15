import speech_recognition as SR
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

r = SR.Recognizer()
translator = google_translator()

running = True

while running:
    with SR.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Translating...")
            text = r.recognize_google(audio)
            print(text)

            if text == "exit":
                running = False
                break
            else:
                running = True

        except SR.UnknownValueError:
            print("Could not understand audio")
        except SR.RequestError:
            print("Could not request audio from google")


        tr_text = translator.translate(text, lang_tgt='es')
        print(f"The Translated Text is: {tr_text}")

        voice = gTTS(tr_text, lang='es')
        voice.save("translated.mp3")
        playsound("translated.mp3")
        os.remove("translated.mp3")
