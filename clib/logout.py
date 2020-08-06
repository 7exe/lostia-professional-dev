import sys
from command import *

currentdata = open("LostiaFiles/user.data").read()

if(currentdata != "guest"):
  changedata = open("LostiaFiles/user.data","w")
  changedata.write("guest")
  changedata.close()
  print("Successfully logged out!")
  isLoggedIn = False
  end(sys.argv)
else:
  print("Cannot logout from user 'guest'")
  end(sys.argv)
