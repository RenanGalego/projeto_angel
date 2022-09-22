#Arquivo principal
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Cria um reconhecedor
def ouvir_mic():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Estou ouvindo")
        audio = mic.listen(source)

    try:
        frase = mic.recognize_google(audio, language='pt-BR')
        print(f'Você disse: {frase}')
    except sr.UnknownValueError:
        print("Entendi não")
        return frase

ouvir_mic()