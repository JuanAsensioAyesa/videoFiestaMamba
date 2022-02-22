import numpy
from moviepy.editor import *
import glob
import os

# pip install librosa
import librosa



def get_beat_times(audio_file):
  y, sr = librosa.load(audio_file) 

  # approach 1 - onset detection and dynamic programming
  tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
  # beats now contains the beat *frame positions*
  # convert to timestamps like this:
  beat_times = librosa.frames_to_time(beats, sr=sr)

  return beat_times

if __name__ == "__main__":
    #Mira a ver si ves una forma menos cutre de hacer esto
    imagenes = glob.glob("./videos/*.jpg")
    imagenes2 = glob.glob("./videos/*.jpeg")


    #Esta parte del codigo la he hecho para ver que proporciones hay en los distintos videos
    # y como se repiten por si hay que hacer preprocesado y luego usar el comando ffmpeg
    dict  =  {}
    for imagen in imagenes2:
        imagenes.append(imagen)
    
    i = 0
    for imagen in imagenes:
      print(i,len(imagenes))
      clip = ImageClip(imagen)
      w,h = clip.size
      if (w,h) in dict.keys():
        dict[(w,h)]+=1
      else:
        dict[(w,h)] = 1
      i+=1
    print(dict)
    dic_ratio = {}
    for key in dict.keys():
      w,h = key
      if(w > h):
        ratio = float(w)/float(h)
      else:
        ratio = float(h)/float(w)
      str_key = "{:.1f}".format(ratio)
      if str_key in dic_ratio.keys():
        dic_ratio[str_key]+=1
      else:
        dic_ratio[str_key] = 1

    print(dic_ratio)
    #Aqui se acaba la parte pensada para preProcesado

    #Esta parte seria lo ideal, ya que se la suda el tamanio de las disintas imagnes
    # (se podria escalar la que haga falta)
    # Lo malo es que a mi me usa muchiiiiiiisima RAM para la mierda que es realmente
    # Esto tambien nos permitiria customizar la duracion de cada imagen por si queremeos que alguna dure
    # mas cuando rompa la cancion y tal
    #Igual en lugar de crear todos los clips de imagen a las bravas conviene mas crear uno y meterlo en uno de video directamente y
    # liberar la memoria de ese clip de imagen
    
    print("Imagenes ",len(imagenes),i)  
    print("Creando clips de imagen")
    #Estaria guapo meterle a cada clip un texto encima con un id unico, asi si hay que escalar alguno o rotarlo es mas facil
    clips = []

    beat_times = get_beat_times('macklemore.wav')

    for i, m in enumerate(imagenes):
      c = ImageClip(m)
      w, h = c.size
      if(w > h):
        ratio = float(w)/float(h)
      else:
        ratio = float(h)/float(w)
      
      dur = 10 if i == len(imagenes) - 1 else beat_times[i+1] - beat_times[i]
      clips.append(c.set_duration(2*dur))


    #clips = [ImageClip(m).resize(0.5).set_duration(0.1) for m in imagenes] #Con las 20 primeras imagenes ya me va como una mierda y son 600 y pico
    print("Creados clip de imagen")
    print("Concatenando")
    #Esto estoy seguro que tiene opciones para que vata mas rapido
    concat_clip = concatenate_videoclips(clips, method="compose")

    audioclip = AudioFileClip("macklemore.wav")
    concat_clip = concat_clip.set_audio(audioclip)

    print("Concatenado")
    print("Escribiendo")
    #24 fps creo que son muchos para imagenes aunque hay que meter fragmentos de video tambien
    concat_clip.write_videofile("test.mp4", fps=24)
    print("Escrito")
    
    print("Hola mamba!")
    #Aqui se acaba la mejor opcion
    
    #Esto se supone que hace lo de arriba pero pide que ssean todas del mismo tamanio y tampoco nos deja customizar mucho
    clip = ImageSequenceClip("./videos/", fps=10)
    clip.write_videofile("result.mp4")
