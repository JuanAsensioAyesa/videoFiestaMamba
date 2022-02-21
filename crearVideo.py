import numpy
from moviepy.editor import *
import glob
import os
if __name__ == "__main__":
    imagenes = glob.glob("./videos/*.jpg")
    imagenes2 = glob.glob("./videos/*.jpg")
    for imagen in imagenes2:
        imagenes.append(imagen)
    i = 0
    
    print("Imagenes ",len(imagenes),i)  
    print("Creando clips de imagen")
    clips = [ImageClip(m).set_duration(0.1)
      for m in imagenes[:100]]
    print("Creados clip de imagen")
    print("Concatenando")
    concat_clip = concatenate_videoclips(clips, method="compose")
    print("Concatenado")
    print("Escribiendo")
    concat_clip.write_videofile("test.mp4", fps=24)
    print("Escrito")
    
    print("Hola mamba!")
