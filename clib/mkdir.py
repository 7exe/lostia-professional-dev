from command import end
import sys
import os

currentDir = open("LostiaFiles/current.directory").read()
args = sys.argv

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("mkdir: directory")
    end(sys.argv)
check_if_has_arguments()
loggedInUser = open("LostiaFiles/user.data").read()
if(loggedInUser == "guest"):
  split = sys.argv[0].split("/")
  lenSplit = len(split)
  print(split[lenSplit-1].replace(".py","")+": PERMISSION DENIED.")
  end(sys.argv)

if(not os.path.exists(currentDir+args[1])):
  os.makedirs(currentDir+args[1])
  end(sys.argv)
else:
  print("Directory already exists!")
  end(sys.argv)