import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from hanspell import spell_checker
import googletrans
import asyncio

# Create TK
#root = tk.Tk()

# Create sr instance
Recognizer = sr.Recognizer()
mic = sr.Microphone()

# Translator
translator = googletrans.Translator()

# GUI
#root.mainloop()

async def print_data(data: str) -> None:
    correct = spell_checker.check(data).as_dict()['checked']
    print(correct)
    print(translator.translate(correct, dest='zh-cn').text)
    

while True:
    with mic as source: #안녕~이라고 말하면
        audio = Recognizer.listen(source, phrase_time_limit=5)
    try:
        data = Recognizer.recognize_google(audio, language="ko")
        asyncio.run(print_data(data))
    except:
        #print("?")
        continue
    
    #lb = tk.Label(root, text=data)
    #lb.pack()