import speech_recognition as sr
import spacy

nlp = spacy.load('en_core_web_sm')
r = sr.Recognizer()

MeetPerson = False
Name = ""
WORDS = ["my name is", "What is your name I'm", "nice to meet you", "hi I'm", "What's your name", "please meet", ]

with sr.Microphone() as source:
    print('Speak Anything')
    # audio = r.listen(source)

    try:
        # Text is a string
        text = "Nathan DaDalto and Emily went to the park. my name is Nathan and"
        # text = r.recognize_google(audio)
        nameVars = nlp(text)

        # Find to see if Meeting phrase is in conversation
        i = 0
        for i in range(len(WORDS)):
            if WORDS[i] in text:
                MeetPerson = True

        # Saves New Name
        if MeetPerson is True:
            for i in range(len(WORDS)):
                if WORDS[i] in text:
                    Name = text.split(WORDS[i], maxsplit=1)[-1]\
                            .split(maxsplit=1)[0]
                    print("New Person name is: " + Name)

        # Checks for Names
        for noun in nameVars.ents:
            print(noun.text, noun.start_char, noun.end_char, noun.label_)

        print('You said : {}'.format(text))
    except:
        print("Sorry don't know what you said")

# Help Links https://www.geeksforgeeks.org/python-named-entity-recognition-ner-using-spacy/

"""
How to get the Index of Greeting Phrase
sChar = text.index(WORDS[i])
eChar = text.index(WORDS[i]) + len(WORDS[i])
print("Index of Phrase is:" + str(sChar) + " " + str(eChar))
"""