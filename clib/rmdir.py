from command import end
import sys
import os
import shutil

loggedInUser = open("LostiaFiles/user.data").read()
if(loggedInUser == "guest"):
  split = sys.argv[0].split("/")
  lenSplit = len(split)
  print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
  end(sys.argv)

def getListOfFiles(dirName):
  listOfFile = os.listdir(dirName)
  allFiles = list()
  for entry in listOfFile:
      fullPath = os.path.join(dirName, entry)
      allFiles.append(fullPath)
  return allFiles

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("rmdir: directory")
    end(sys.argv)

currentDir = open("LostiaFiles/current.directory").read()

check_if_has_arguments()
if(os.path.isdir(currentDir+sys.argv[1])):
  pass
else:
  print("Directory not found.")
  end(sys.argv)

if(len(getListOfFiles(currentDir+sys.argv[1]))>0):
  print("rmdir: failed to remove '"+sys.argv[1]+"': Directory not empty")
  end(sys.argv)
else:
  shutil.rmtree(currentDir+sys.argv[1])
  end(sys.argv)




