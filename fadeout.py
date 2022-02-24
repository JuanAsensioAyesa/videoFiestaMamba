from moviepy.editor import *
from moviepy.audio.fx.audio_fadeout import audio_fadeout

v = VideoFileClip('./video_no_chill_fotos_Trim.mp4')
v = audio_fadeout(v.fadeout(5), 5)

#clips = [ImageClip(m).resize(0.5).set_duration(0.1) for m in imagenes] #Con las 20 primeras imagenes ya me va como una mierda y son 600 y pico
print("Creados clip de imagen")
print("Concatenando")
#Esto estoy seguro que tiene opciones para que vata mas rapido

print("Concatenado")
print("Escribiendo")
#24 fps creo que son muchos para imagenes aunque hay que meter fragmentos de video tambien
v.write_videofile('out.mp4', fps=24)