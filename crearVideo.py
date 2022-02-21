import numpy
from moviepy.editor import *
import glob
import os
if __name__ == "__main__":
    imagenes = glob.glob("./videos/*.jpg")
    imagenes2 = glob.glob("./videos/*.jpg")
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
    # print("Imagenes ",len(imagenes),i)  
    # print("Creando clips de imagen")
    # clips = [ImageClip(m).set_duration(0.1)
    #   for m in imagenes[:20]]
    # print("Creados clip de imagen")
    # print("Concatenando")
    # concat_clip = concatenate_videoclips(clips, method="compose")
    # print("Concatenado")
    # print("Escribiendo")
    # concat_clip.write_videofile("test.mp4", fps=24)
    # print("Escrito")
    
    # print("Hola mamba!")

    # clip = ImageSequenceClip("./videos/", fps=10)
    # clip.write_videofile("result.mp4")
