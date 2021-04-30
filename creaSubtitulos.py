import speech_recognition as sr
from os import path
from pydub import AudioSegment
import moviepy.editor as mp
import io
import sys
import os

def conversio(segons):
    hores=int(segons/3600)
    segons-=hores*3600
    minuts=int(segons/60)
    segons-=minuts*60
    return hores,minuts,segons
 


def dictat(nommp3):
    # converteix arxiu donada com argument de mp3 a wav                                         
    sound = AudioSegment.from_mp3(nommp3)
    sound.export("sortida.wav", format="wav")

    # transcriure arxiu de audio                                                         
    AUDIO_FILE = "sortida.wav"

    # utilitzar arxiu de audio com font de so                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  
        sortida = r.recognize_google(audio,language=sys.argv[2]) 
        fitxer.write(sortida + "\n")


#Partim mp3 de minut en minut la primera hora
arxiu = sys.argv[1]
s = 0
i = 0


clip = mp.VideoFileClip(arxiu)
arxiu = arxiu[:len(arxiu)-4] + '.mp3'
clip.audio.write_audiofile(arxiu[:len(arxiu)-4] + '.mp3')

#Arxiu on es guarda el resultat
fitxer=io.open(arxiu[:len(arxiu)-4] + '.txt','a')

try:
    while True:
        hores,minuts,segons=conversio(s)
        print(hores,minuts,segons)
        comandament ="ffmpeg -i {} -acodec copy -t 00:00:10 -ss {}:{}:{} {}.mp3".format(arxiu,hores,minuts,segons,i)
        os.system(comandament)
        nommp3=str(i)+".mp3"
        s2=3600*hores+minuts*60+segons+10
        hores2,minuts2,segons2=conversio(s2)
        fitxer.write("\n\n"+str(i)+"\n"+"{}:{}:{},000 --> {}:{}:{},000".format(hores,minuts,segons,hores2,minuts2,segons2)+'\n')
        dictat(nommp3)
        comandament='del {}'.format(nommp3)
        os.system(comandament) 
        s += 10
        i += 1      
except:
    fitxer.close()
    comandament='del {}'.format("sortida.wav")
    os.system(comandament)
    comandament='del {}'.format(nommp3)
    os.system(comandament)
    comandament='del {}'.format(arxiu)
    os.system(comandament)
    nomArxiu = arxiu[:len(arxiu)-4] + '.srt'
    os.rename(arxiu[:len(arxiu)-4] + '.txt', nomArxiu)


# codi clau extret de https://pythonbasics.org/transcribe-audio/
# modificat per joan masdemont fontas
# 2º modificació per Javier García Cortés
# us ----python creaSubtitulos.py nomVideo   idioma ------ on idioma pot ser es-ES , fr-FR.....

