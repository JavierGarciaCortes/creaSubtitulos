import os
import tkinter as tk

def CurSelet():
    if listbox1.get(tk.ANCHOR) == '':
        Label1.config(text = 'Seleciona un video')
    elif v.get() == '':
        Label1.config(text = 'Seleciona un idioma')
    else:
        comandament='py .\creaSubtitulos.py .\\videos\\{} {}'.format(listbox1.get(tk.ANCHOR), v.get())
        os.system(comandament)
        Label1.config(text = 'Creando Subtitulos')


contenido = os.listdir('./videos')
aux = []
for i in range(len(contenido)):
    if contenido[i][len(contenido[i])-3:] != 'srt':
        aux.append(contenido[i]) 
contenido = aux
idiomas = ['es-ES', 'ca-ES', 'en-GB', 'en-Us']


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

