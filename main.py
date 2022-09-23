#Arquivo principal
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Cria uma voz de resposta
def voz_ia (audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/hello.mp3')
    print("Estou aprendendo")
    playsound('audios/hello.mp3')

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

frase = ouvir_mic()
voz_ia(frase)