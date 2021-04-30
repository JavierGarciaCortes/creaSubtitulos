import speech_recognition as sr
from os import path
from pydub import AudioSegment
import moviepy.editor as mp
from playsound import playsound
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
    # convert mp3 file to wav                                         
    sound = AudioSegment.from_mp3(nommp3)
    sound.export("temp.wav", format="wav")

    # transcribe audio file                                                         
    AUDIO_FILE = "temp.wav"

    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  
        sortida = r.recognize_google(audio,language=sys.argv[2]) 
        fitxer.write(sortida + "\n")


arxiu = sys.argv[1]
s = 0
i = 0

# Extract the audio of the video
clip = mp.VideoFileClip(arxiu)
arxiu = arxiu[:len(arxiu)-4] + '.mp3'
clip.audio.write_audiofile(arxiu[:len(arxiu)-4] + '.mp3')

# File where we save the transcription
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
    playsound("audio.mp3")
