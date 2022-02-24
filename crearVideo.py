import random
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


def crear_video(videos, outfile):
    print("Creando clips de imagen")
    #Estaria guapo meterle a cada clip un texto encima con un id unico, asi si hay que escalar alguno o rotarlo es mas facil
    clips = []

    # Obtener timestamps de los beats de la canción
    beat_times = get_beat_times('overture.wav')
    # Obtener la duración media entre beats
    mean_dur = numpy.mean(numpy.gradient(beat_times))

    for i, v in enumerate(videos):
      filename = os.path.basename(v).split('.')[0]
      aux = filename.split('_')
      start = int(aux[1])
      dur = 1.5*mean_dur if len(aux) == 2 else 2*mean_dur

      v = VideoFileClip(v)
      if i == len(videos) - 1:
        dur = 6
      clips.append(v.resize( height=1080 ).subclip(start).set_duration(dur))

    #clips = [ImageClip(m).resize(0.5).set_duration(0.1) for m in imagenes] #Con las 20 primeras imagenes ya me va como una mierda y son 600 y pico
    print("Creados clip de imagen")
    print("Concatenando")
    #Esto estoy seguro que tiene opciones para que vata mas rapido
    concat_clip = concatenate_videoclips(clips, method="compose")

    audioclip = AudioFileClip("overture.wav")
    concat_clip = concat_clip.set_audio(audioclip)

    print("Concatenado")
    print("Escribiendo")
    #24 fps creo que son muchos para imagenes aunque hay que meter fragmentos de video tambien
    concat_clip.write_videofile(outfile, fps=24)
    print("Escrito")
    
    print("Hola mamba!")
    #Aqui se acaba la mejor opcion


def crear_video_imagenes(imagenes, audio, outfile, chill=False):
    print("Creando clips de imagen")
    #Estaria guapo meterle a cada clip un texto encima con un id unico, asi si hay que escalar alguno o rotarlo es mas facil
    clips = []

    # Obtener timestamps de los beats de la canción
    beat_times = get_beat_times(audio)
    # Obtener la duración media entre beats
    mean_dur = numpy.mean(numpy.gradient(beat_times))

    if chill:
      mean_dur *= 4
    
    for i, m in enumerate(imagenes):
      c = ImageClip(m)

      dur = 10 if i == len(imagenes) - 1 else beat_times[i+1] - beat_times[i]

      dur = mean_dur if chill else dur

      clips.append(c.resize( height=1080 ).set_duration(dur))
    

    #clips = [ImageClip(m).resize(0.5).set_duration(0.1) for m in imagenes] #Con las 20 primeras imagenes ya me va como una mierda y son 600 y pico
    print("Creados clip de imagen")
    print("Concatenando")
    #Esto estoy seguro que tiene opciones para que vata mas rapido
    concat_clip = concatenate_videoclips(clips, method="compose")

    audioclip = AudioFileClip(audio)
    concat_clip = concat_clip.set_audio(audioclip)

    print("Concatenado")
    print("Escribiendo")
    #24 fps creo que son muchos para imagenes aunque hay que meter fragmentos de video tambien
    concat_clip.write_videofile(outfile, fps=24)
    print("Escrito")
    
    print("Hola mamba!")
    #Aqui se acaba la mejor opcion

if __name__ == "__main__":
    #Mira a ver si ves una forma menos cutre de hacer esto
    noChill = glob.glob("./videos/noChill/*.*")
    
    chill = glob.glob("./videos/chill/*.*")
    random.seed(0)
    random.shuffle(noChill)

    videos = glob.glob("./videos/noChill/videos/*")

    #crear_video(videos, 'video_no_chill.mp4')

    #crear_video_imagenes(chill, 'amanecer.wav', 'video_chill.mp4', True)
    crear_video_imagenes(noChill, 'projectx.wav', 'video_no_chill_fotos.mp4')
    