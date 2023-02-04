__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, glob
from os import path
import shutil
import pathlib
from zipfile import ZipFile

#print(os.getcwd())

directory = "cache"
parent_dir = os.getcwd() + "/files"
new_path = os.path.join(parent_dir, directory)

def clean_cache():
    directory = "cache"
    
    new_path = os.path.join(parent_dir, directory)
    #print(new_path)
    if path.exists(new_path) == True:
        shutil.rmtree(new_path)
        os.mkdir(new_path)
    else:
        os.mkdir(new_path)

#clean_cache()

zip_file = glob.glob(os.getcwd()+"/files/*.zip")

#print(zip_file[0])
#print(new_path)
def cache_zip(zip_file_path, cache_dir_path):
    x = ZipFile(zip_file_path)
    x.extractall(path = cache_dir_path)

#cache_zip(zip_file[0],new_path)

def cached_files():
    x = []
    for filepath in pathlib.Path(new_path).glob("**/*"): 
        #print(os.path.abspath(filepath))
        x.append(os.path.abspath(filepath))
        
    return x

#print(cached_files())
#x = os.path.abspath(new_path)
#print(x)
#plek = new_path +"/601.txt"
#print(plek)

def find_password(lijst):
    word = "password: "
    #plek = new_path +"/601.txt"
    for i in lijst:
       # print(i)
        
        with open(i, "r") as file:
            content = file.read()
            content2 = file.readlines()
            if word in content:
                
                y = content.index(word)
                #print(y)
                q = len(word)
                z = (content.find("\n",(y+q)))
                r = content[(y+q):z]
                
                return r
            
        #print(content)


final = find_password(cached_files())
print(final)