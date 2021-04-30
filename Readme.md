CreaSubtitulos
Este programa extrae el sonido de un video y lo convierte en subtitulos en intervalos de 10seg.

Uso:
    python creaSubtitulos.py nombreVideo idioma
    
El formato del idioma tiene que ser: es-ES, ca-ES, en-GB, en-Us....
Necesita conexion a internet para funcionar (SpeechRecognition). Todos los idiomas que detecta y sus codigos aparecen en el siguiente enlace:
https://cloud.google.com/speech-to-text/docs/languages

Requiere:
Speech Recognition  - pip install SpeechRecognition
pydub               - pip install pydub
moviepy             - pip install moviepy
ffmpeg-python       - pip install ffmpeg-python















# codi clau extret de https://pythonbasics.org/transcribe-audio/
# Codigo modificado de mp3totext.py  https://gist.github.com/nosemas/a7e01f629c0302539ae4ee0782e5a801
# Creado por Joan Masdemont Fontas