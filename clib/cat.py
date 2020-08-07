import sys
import os
from command import end

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("cat: file")
    end(sys.argv)

currentDir = open("LostiaFiles/current.directory").read()

def cat():
  if(os.path.exists(currentDir+sys.argv[1])):
      catFile = open(currentDir+sys.argv[1]).read()
      print(catFile)
      end(sys.argv)
  else:
    print("Directory does not exist")
    end(sys.argv)

check_if_has_arguments()
cat()