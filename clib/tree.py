import os
from os import listdir, sep
from os.path import abspath, basename, isdir
from command import end
import sys
totalfiles = -1



def tree(dir, padding, print_files=True):
    global totalfiles
    print(""+padding[:-1] + '├─── \033[34m' + basename(abspath(dir)) + '\033[39m')
    padding = padding + '   '
    files = []
    if print_files:
        files = listdir(dir)
    else:
        files = [x for x in os.listdir(dir) if os.path.isdir(dir + sep + x)]
    count = 0
    for file in files:
        count += 1
        totalfiles = totalfiles + 1
        
        path = dir + sep + file
        if isdir(path):
            if count == len(files):
                tree(path, padding + ' ', print_files)
            else:
                tree(path, padding + '│', print_files)
        else:
            if(count==len(files)):
              print(padding + '└─── ' + file)
            else:
              print(padding + '├─── ' + file)
    

try:
  if(len(sys.argv) > 1):
        if(os.path.isdir(sys.argv[1])):
            tree(sys.argv[1]," ")
            dirs = 0
            files = 0
            for _, dirnames, filenames in os.walk(sys.argv[1]):
              files += len(filenames)
              dirs += len(dirnames)
            print("\n"+str(dirs+1)+" directories, "+str(files)+" files")
            end(sys.argv)
        else:
            print("Directory not found")
            end(sys.argv)
  else:
        tree("./"," ")
        dirs = 0
        files = 0
        for _, dirnames, filenames in os.walk("./"):
          files += len(filenames)
          dirs += len(dirnames)
        print("\n"+str(dirs+1)+" directories, "+str(files)+" files")
        end(sys.argv)
except:
    print("Failed to display Directory")
    end(sys.argv)
