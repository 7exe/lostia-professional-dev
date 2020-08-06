from command import end
import sys
import os

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
if(os.path.isfile(currentDir+sys.argv[1])):
  os.remove(currentDir+sys.argv[1])
  end(sys.argv)
else:
  print("Target file does not exist")
  end(sys.argv)