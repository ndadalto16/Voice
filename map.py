import speech_recognition as sr


r = sr.Recognizer()
r.energy_threshold = 500

with sr.Microphone() as source:
    print('Speak Anything')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print("Sorry don't know what you said")
