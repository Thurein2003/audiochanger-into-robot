import speech_recognition as sr
from gtts import gTTS
import os

voice = ""''
while True :
    e =sr.Recognizer( )
    with sr.Microphone ( ) as source :
        try:
            audio = e.listen(source)
            text = e.recognize_google( audio )
            print(text)
            if text == "stop" :
                break
            text = e.recognize_google( audio )
            voice=voice+str(text)

        except:
            print("say something" )
we-gTTs( text=voice, lang= 'en', slow=False)
we.save("A. wav")
