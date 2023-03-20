import os
import openai
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from termcolor import colored

LANGUAGE = "es"  # define audio language
ENGINE_IA = "text-davinci-003"
AUDIO_FILE = "response.mp3"
openai.api_key = ""  # your api-key here

def voice():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Eva: En que te puedo ayudar?")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-AR")
            print('神: ', text)
            new_question(LANGUAGE, ENGINE_IA, AUDIO_FILE, text)
        except:
            print("Eva: lo siento, no he comprendido")

def new_question(LANGUAGE, ENGINE_IA, AUDIO_FILE, text):
    try:
        # print("Eva:[...]")
        response = openai.Completion.create(
            engine=ENGINE_IA,
            prompt=text,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.7,
        )

        response_text = response.choices[0].text.strip()
        print('Eva: ', response_text)

        tts = gTTS(response_text, lang=LANGUAGE, slow=False)
        tts.save(AUDIO_FILE)
        playsound(AUDIO_FILE)
        os.remove(AUDIO_FILE)
        print("Presione enter para continuar...")
        input()  # Espera hasta que se presione Enter

    except Exception as e:
        print(colored("lo lamento, error:", "red"))
        print(colored(str(e), "red"))

    print()


if __name__ == "__main__":
    while True:
        voice()
