from command import end
import sys
import os

currentDir = open("LostiaFiles/current.directory").read()
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
    print("touch: filename")
    end(sys.argv)

def check_if_file_exists_and_write():
  if(os.path.isfile(currentDir+sys.argv[1])):
    print("This file already exists!")
    end(sys.argv)
  else:
    open(currentDir+sys.argv[1],"w").close()
    end(sys.argv)

check_if_has_arguments()
check_if_file_exists_and_write()