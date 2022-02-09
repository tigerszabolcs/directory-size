import os
from tkinter import N
rootdir = 'C:/Games/'
filesize = 0
maxsize = 0
accuraccy = 10000000
maxfile = ""
history = []
class bigFiles:
    def __init__(self, fName, fSize) -> None:
        self.fName = fName
        self.fSize = fSize
        pass

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fpath = os.path.join(subdir, file)
        filesize = os.path.getsize(fpath)
        if not os.path.islink(file_path):
            total_size += os.path.getsize(file_path)
        #if (filesize > maxsize) and (filesize > 10000000):
        #   maxsize = filesize            
        #  maxfile = fpath
        # n = bigFiles(maxfile,maxsize)
        # history.append(n)
        # print(maxfile,maxfile, sep=' ')
        # continue
        #print(os.path.join(subdir, file))
        continue
# print("Legnagyobb file: ", maxfile, " " , "mérete: " , maxsize )
# for x in history:
#    print(x.fSize, x.fName)
