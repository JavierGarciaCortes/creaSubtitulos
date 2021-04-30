import speech_recognition as sr
from os import path
from pydub import AudioSegment
import moviepy.editor as mp
from playsound import playsound
import io
import sys
import os
import tkinter as tk

def conversio(segons):
    hores=int(segons/3600)
    segons-=hores*3600
    minuts=int(segons/60)
    segons-=minuts*60
    return hores,minuts,segons


def dictat(nommp3, idioma):
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


def creaSubtitulos(file, idioma):
    arxiu = file
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
            dictat(nommp3, idioma)
            comandament='del {}'.format(nommp3)
            os.system(comandament) 
            s += 10
            i += 1      
    except:
        fitxer.close()
        comandament='del {}'.format("temp.wav")
        os.system(comandament)
        comandament='del {}'.format(nommp3)
        os.system(comandament)
        comandament='del {}'.format(arxiu)
        os.system(comandament)
        nomArxiu = arxiu[:len(arxiu)-4] + '.srt'
        os.rename(arxiu[:len(arxiu)-4] + '.txt', nomArxiu)
        playsound("audio.mp3")



def CurSelet():
    if listbox1.get(tk.ANCHOR) == '':
        Label1.config(text = 'Seleciona un video')
    elif v.get() == '':
        Label1.config(text = 'Seleciona un idioma')
    else:
        Label1.config(text = 'Creando subtitulos')
        file = '.\\videos\\{}'.format(listbox1.get(tk.ANCHOR))
        creaSubtitulos(file, v.get())
        Label1.config(text = 'Tarea finalizada')


contenido = os.listdir('./videos')
aux = []
for i in range(len(contenido)):
    if contenido[i][len(contenido[i])-3:] != 'srt':
        aux.append(contenido[i]) 
contenido = aux
idiomas = ['es-ES', 'ca-ES', 'en-GB', 'en-US']

root = tk.Tk()
amplada = 400
alcada = 400
strink = '{}x{}'.format(amplada,alcada)
root.geometry(strink)
root.attributes('-fullscreen', False)

c= tk.Canvas(root,bg='blue')
c.place(x=0,y=0,width=amplada,height=alcada)

listbox1 = tk.Listbox(c)
listbox1.place(x = 10, y = 10, width =  190, height = 180)
for item in contenido:
 listbox1.insert(tk.END, item)

v = tk.StringVar()
r1 = tk.Radiobutton(c, text = "es-ES", variable = v, value = idiomas[0], state=tk.ACTIVE)
r1.place(x = 3*amplada//4, y = 10)
r2 = tk.Radiobutton(c, text = "ca-ES", variable = v, value = idiomas[1])
r2.place(x = 3*amplada//4, y = 40)
r3 = tk.Radiobutton(c, text = "en-GB", variable = v, value = idiomas[2])
r3.place(x = 3*amplada//4, y = 70)
r4 = tk.Radiobutton(c, text = "en-Us", variable = v, value = idiomas[3])
r4.place(x = 3*amplada//4, y = 100)

Label1 = tk.Label(c, text = '', width = 0, font = ('Arial', 12), bg = c.cget('bg'))
Label1.place(x = 200, y = 350, anchor ="center")

Button1 = tk.Button(c, text = "Crea Subtitulo", command = CurSelet)
Button1.place(x = 200, y = 300, anchor ="center")

root.mainloop()

