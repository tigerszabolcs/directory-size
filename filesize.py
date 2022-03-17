import os
from tkinter import N

class bigFiles:
    def __init__(self, fName, fSize) -> None:
        self.fName = fName
        self.fSize = fSize
        pass

class dirSizes:
    def __init__(self, dirPath, dirSize, lFile) -> None:
        self.dirPath = dirPath
        self.dirSize = dirSize
        self.lFile = lFile
        pass

def ConvertSize(size,measure):
    if measure == "MB":
        return size / (1024*1024)
    elif measure == "GB":
        return size/ (1024*1024*1024)
    else:
        return size



def calculateSizeOfDir(rootDir):
    rootdir = rootDir
    max = 0
    totalSize = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fpath = os.path.join(subdir, file)
            cFileSize = os.path.getsize(fpath)
            if cFileSize > max:
                max = cFileSize
            if not os.path.islink(fpath):
                totalSize += cFileSize
            continue
    # print("Legnagyobb file: ", maxfile, " " , "mérete: " , maxsize )
    # for x in history:
    #    print(x.fSize, x.fName)
    print("size in MB: ", int(ConvertSize(totalSize,"MB")), "|| size in GB: ", int(ConvertSize(totalSize,"GB")), sep=' ') 
    currentDir = dirSizes()
    currentDir.dirPath = rootDir
    currentDir.dirSize = totalSize
    currentDir.lFile = max
    return currentDir

def main():
    allDir = []
    allDir.append(calculateSizeOfDir("C:\Games"))

if __name__ =="__main__":
    main()
