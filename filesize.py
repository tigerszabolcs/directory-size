import os
from tkinter import N

class bigFiles:
    def __init__(self, fName, fSize) -> None:
        self.fName = fName
        self.fSize = fSize
        pass

def ConvertSize(size,measure):
    if measure == "MB":
        return size / (1024*1024)
    elif measure == "GB":
        return size/ (1024*1024*1024)
    else:
        return size

def calculateSizeOfDir(rootDir):
    rootdir = 'C:/Games/'
    filesize = 0
    maxsize = 0
    maxfile = ""
    history = []
    totalSize = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fpath = os.path.join(subdir, file)
            filesize = os.path.getsize(fpath)
            if not os.path.islink(fpath):
                totalSize += os.path.getsize(fpath)
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
    print("size in MB: ", int(ConvertSize(totalSize,"MB")), "|| size in GB: ", int(ConvertSize(totalSize,"GB")), sep=' ') 
    return totalSize()
