from command import *
import sys
force_run_command("login systemadmin -k")
print("Current User:")
user = open("LostiaFiles/user.data").read()
print(user)

end(sys.argv)