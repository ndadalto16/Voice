import speech_recognition as sr


r = sr.Recognizer()

WORDS = ["my name is", "What is your name I'm", "nice to meet you", "hi I'm", "What's your name", "please meet", ]

with sr.Microphone() as source:
    print('Speak Anything')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if any(word in WORDS for word in WORDS):
            print('PASS')
        print('You said : {}'.format(text))
    except:
        print("Sorry don't know what you said")

