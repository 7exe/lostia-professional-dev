import os
import sys
from command import end, check_for_permission
from datetime import datetime
from getpass import getpass
import shutil

users = open("LostiaFiles/keychain.keychain").readlines()

permissions = ["sysadmin", "user", "admin"]


check_for_permission()
if(len(sys.argv)<2):
  print("adduser: user, permission [Optional]")
  end(sys.argv)

def check_if_user_exists():
  for user in users:
    if(sys.argv[1] == user.split("/")[2]):
      print("This user already exists!")
      end(sys.argv)
    else:
      pass

def validate_permission():
  if(len(sys.argv)==3):
    if(sys.argv[2] in permissions and sys.argv[2] != "sysadmin" and len(sys.argv)==3):
      return True
    else:
      print(sys.argv[2]+" is not a valid permission.")
      end(sys.argv)
  else:
    return None

def create_new_home_directory(name):
  print("Creating home directory `/home/"+name+"' ...")
  os.mkdir("LostiaFiles/root/home/"+name+"/")

def copy_files_default_files(name):
  print("Copying files from `/etc/skel'")
  listDir = os.listdir("LostiaFiles/root/etc/skel/")
  for dir in listDir:
    os.mkdir("LostiaFiles/root/home/"+name+"/"+dir+"/")


def remove_created_home_directory(name):
  shutil.rmtree("LostiaFiles/root/home/"+name+"/")


def write_new_data():
  if(sys.argv[1].isupper()):
    print("User name cannot be uppercase, full name can be")
    end(sys.argv)
  print("Adding user "+sys.argv[1]+" ...")
  create_new_home_directory(sys.argv[1])
  copy_files_default_files(sys.argv[1])
  password = getpass("\033[39mEnter new LOSTIA password: ")
  if("/" in password):
    print("/ is not a valid symbol")
    remove_created_home_directory(sys.argv[1])

    end(sys.argv)
  else:
    retype = getpass("\033[39mRetype new LOSTIA password: ")
    if(retype != password):
      print("retyped password does not match")
      remove_created_home_directory(sys.argv[1])
      end(sys.argv)
    else:
      fullName = input("\033[39mFull Name: ")
      if(fullName != "" or fullName.split(" ")[0]!=""):
        if(len(sys.argv)==2):
          with open("LostiaFiles/keychain.keychain","a") as newuser:
            newuser.write("\n/"+fullName+"/"+sys.argv[1]+"/"+password+"/user/visable/"+str(datetime.now())+"/")
            newuser.close()
          print("Added new user")
          end(sys.argv)
        else:
          with open("LostiaFiles/keychain.keychain","a") as newuser:
            newuser.write("\n/"+fullName+"/"+sys.argv[1]+"/"+password+"/"+sys.argv[2]+"/visable/"+str(datetime.now())+"/")
            newuser.close()
          print("Added new user")
          end(sys.argv)
      else:
        print("Full name cannot be empty")
        remove_created_home_directory(sys.argv[1])
        end(sys.argv)

validate_permission()
check_if_user_exists()
write_new_data()