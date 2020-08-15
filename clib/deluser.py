import command
import sys
import shutil
import os

import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

currentUser = open("LostiaFiles/user.data").read()
keychain = open("LostiaFiles/keychain.keychain").readlines()

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("deluser: user")
    command.end(sys.argv)
  

if(currentUser == "systemadmin"):
  pass
else:
  print("deluser: Only root may remove a user from Ash ")
  command.end(sys.argv)

newKeychain = []

check_if_has_arguments()
if(sys.argv[1] == "systemadmin"):
  print("deluser: Cannot target this user")
  command.end(sys.argv)




def deluser():
  for user in keychain:
    foundUser = False
    userName = user.split("/")[2]
    if(sys.argv[1] == userName):
      foundUser = True
    else:
      newKeychain.append(user.replace("\n",""))
  if(foundUser == True):
    print("Looking for files to backup/remove ...")


    if(len(sys.argv)>=3 and "--backup-to" in sys.argv):
      index = 0
      for I in sys.argv:
        if(sys.argv[index] == "--backup-to"):
          break
        index+=1
      if(os.path.isdir(sys.argv[index+1])):
          print("Backing up files to be removed to "+sys.argv[index+1]+" ...")
          make_tarfile(sys.argv[index+1]+sys.argv[1]+".tar.gz","LostiaFiles/root/home/"+sys.argv[1])
          print("backup_name = "+sys.argv[index+1]+sys.argv[1]+".tar.gz")
      else:
        print("Backup directory does not exist")
        command.end(sys.argv)


    if(command.new_arg_parser("--remove-home")):
      print("Removing files ...")
      shutil.rmtree("LostiaFiles/root/home/"+sys.argv[1]+"/")

    print("Removing user `"+sys.argv[1]+"' ...")
    with open("LostiaFiles/keychain.keychain","w") as newData:
      newData.writelines(newKeychain)
      newData.close()
    print("Done.")
  else:
    print("User not found")



deluser()