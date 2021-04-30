## CreaSubtitulos
Este programa extrae el sonido de un video y lo convierte en subtítulos en intervalos de 10 seg. No funciona para todos los videos, aun esta en desarollo.

Uso:
    python creaSubtitulos.py nombreVideo idioma
    
El formato del idioma tiene que ser: es-ES, ca-ES, en-GB, en-Us....
Necesita conexion a internet para funcionar (SpeechRecognition). Todos los idiomas que detecta y sus codigos aparecen en el siguiente enlace:
https://cloud.google.com/speech-to-text/docs/languages

Requiere tener instalados:
- Speech Recognition     `pip install SpeechRecognition`
- pydub                  `pip install pydub`
- moviepy                `pip install moviepy`

Tambien tendreis que tener en la misma carpeta los ficheros de [ffmpeg](https://www.ffmpeg.org/):
- ffmpeg.exe
- ffplay.exe
- ffprobe.exe








Projecto basado en [mp3totext.py](https://gist.github.com/nosemas/a7e01f629c0302539ae4ee0782e5a801) Creado por Joan Masdemont Fontas
