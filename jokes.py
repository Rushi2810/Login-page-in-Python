import requests
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def take_input():
 with mic as source:
 	r.adjust_for_ambient_noise(source)
 	audio = r.listen(source)
 	speech = r.recognize_google(audio)
 	return speech

def text_to_speech(text):
	engine.say(text)
	engine.runAndWait()
	engine.stop()

print("Wating for input:")
input = take_input()
print(input+"\n")

while True:
	if"joke" in input or "funny" in input:
		response = requests.get("https://icanhazdadjoke.com", headers
                ={"Accept":"application/json"})
		joke = response.json()["joke"]
		print(joke)
		text_to_speech(joke)
		exit()		

	if "close" in input or "quit" in input:
		engine.stop()
		exit()
	engine.stop()
