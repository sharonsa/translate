from googletrans import Translator
import os
import sys
import glob
import shutil
import ntpath
import time


translator = Translator()
path = u'J:\\roms\\'


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
    

def walk_dirs(path):
    rename(path)
    for root, dirs, files in os.walk(path, topdown=True):
        for dir in dirs:
            dir_path=path+dir+"\\"
            print("Moving to dir " + dir_path)
            sys.stdout.flush()
            walk_dirs(dir_path)

 
def rename(path):
    files = glob.glob(path + "*")
    i = 0
    for file in files:
        if is_english(file):
            #new_name=file.replace("(146)\\FC Collection The Three Kingdoms (146)","(146)\\")
            #shutil.move(file, new_name)
            print(file)
        else:
            #try:
                i = i+1
                old_name = file
                try:
                    new_name = ntpath.dirname(file) + "\\"+translator.translate(ntpath.basename(file)).text.replace(":", "-")
                except:
                    print ("Translating error")
                    sys.stdout.flush()
                    i=i-1
                    pass
                    continue
                try:
                    print("renaming " + str(old_name) + " to " + str(new_name))
                    sys.stdout.flush()
                except:
                    try:
                        print("renaming XXX to "+ str(new_name))
                        sys.stdout.flush()
                    except:
                        print("renaming XXX to YYY")
                        sys.stdout.flush()
                        pass
                shutil.move(old_name, new_name)
                time.sleep(.300)
                
    print(str(i) + " files translated")        


walk_dirs(path)
