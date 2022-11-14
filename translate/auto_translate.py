import googletrans

translator = googletrans.Translator()

str1 = "나는 한국인 입니다."
str2 = "I like burger."
result1 = translator.translate(str1, dest='en')
result2 = translator.translate(str2, dest='ko')

print(f"나는 한국인 입니다. => {result1.text}")
print(f"I like burger. => {result2.text}")

import speech_recognition as sr

Recognizer = sr.Recognizer() #인스턴스 생성
mic = sr.Microphone()
with mic as source: #안녕~이라고 말하면
    audio = Recognizer.listen(source)
try:
    data = Recognizer.recognize_google(audio, language="ko")
except:
    print("이해하지 못했음")
    
print(data) #안녕 출력