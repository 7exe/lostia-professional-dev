from command import end, ask_for_password
from getpass import getpass
import sys
import os

def check_if_has_arguments():
  if(len(sys.argv)> 1):
    return True
  else:
    print("passwd: user")
    end(sys.argv)

def check_if_user_exists_and_save_new_data():
  
  users = open("LostiaFiles/keychain.keychain")
  loggedInAs = open("LostiaFiles/user.data")
  if(loggedInAs == "guest"):
    print("Permission Denied")
    end(sys.argv)
  newData = users.readlines()
  count = 0
  for user in newData:

    if(sys.argv[1] == user.split("/")[2]):
      password = user.split("/")[3]
      ignorePassword = 0
      if(loggedInAs == "systemadmin"):
        ignorePassword = 1
      if(ignorePassword == 0):
        ask_for_password("passwd",user.split("/")[1],3,password)
      newPassword = getpass("Enter new LOSTIA password: ")
      if(newPassword == "" or newPassword.split(" ")[0] == ""):
        print("New password cannot be empty")
        end(sys.argv)
      else:
        retype = getpass("Retype new LOSTIA password: ")
        if(newPassword == retype):
          newData[count] = newData[count].replace(password,newPassword,1)
          write = open("LostiaFiles/keychain.keychain","w")
          write.writelines(newData)
          write.close()
          print("passwd: password updated successfully")
          end(sys.argv)
        else:
          print("retyped password does not match")
          end(sys.argv)
    else:
      pass
    count+=1
  print("User not found")
    

check_if_has_arguments()
check_if_user_exists_and_save_new_data()