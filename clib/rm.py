from command import end
import sys
import os

def getListOfFiles(dirName):
  listOfFile = os.listdir(dirName)
  allFiles = list()
  for entry in listOfFile:
      fullPath = os.path.join(dirName, entry)
      allFiles.append(fullPath)
  return allFiles

loggedInUser = open("LostiaFiles/user.data").read()
if(loggedInUser == "guest"):
  split = sys.argv[0].split("/")
  lenSplit = len(split)
  print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
  end(sys.argv)

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("rm: filename")
    end(sys.argv)

currentDir = open("LostiaFiles/current.directory").read()

check_if_has_arguments()
if("^" not in sys.argv):
  if(os.path.isfile(currentDir+sys.argv[1])):
    os.remove(currentDir+sys.argv[1])
    end(sys.argv)
  else:
    print("Target file does not exist")
    end(sys.argv)
else:
  Files = getListOfFiles(currentDir)
  for i in Files:
    if("-v" in sys.argv):
      print("removed '"+i.replace(currentDir,"")+"'")
    os.remove(i)