import command

from shutil import copyfile
import sys
from sys import exit
import os


def has_arguments():
  if(len(sys.argv)>2):
    pass
  else:
    print("cp: source, target")
    command.end(sys.argv)

has_arguments()
source = sys.argv[1]
target = sys.argv[2]

if(os.path.exists(command.CURDIR+sys.argv[1])):
  pass
else:
  print("Source file does not exist!")

if(os.path.exists(command.CURDIR+sys.argv[2])):
  print("Target already exists!")
  

def read_and_write_from_source():
  sourceData = open(command.CURDIR+source).read()
  
  with open(command.CURDIR+target,"w") as newFile:
    newFile.write(sourceData)
    newFile.close()
  command.end(sys.argv)


try:
    read_and_write_from_source()
except IOError as e:
    #print("Unable to copy file. %s" % e)
    command.end(sys.argv)
except:
    #print("Unexpected error:", sys.exc_info())
    command.end(sys.argv)