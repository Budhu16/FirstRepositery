import speech_recognition as sr

R = sr.Recognizer()
print('Speak:')
with sr.Microphone() as source:
    audio = R.listen(source, phrase_time_limit = 5)

try:
    text = R.recognize_google(audio)
except:
    print('Some Error...')
else:
    print(text)
