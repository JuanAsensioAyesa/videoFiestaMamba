import glob
import os 


if __name__ == "__main__":
    listTodas = glob.glob("./todas/*")
    listChill = glob.glob("./chill/*")
    for name in listChill:
        subs = name.split("/")
        print(subs[2])
        os.system("rm "+"./todas/"+"'"+subs[2]+"'")