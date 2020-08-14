import command
import sys
count = 0
newEnvVarName = []
newEnvVarValue = []
for I in command.env_var_name:
  newEnvVarName.append(I.replace("\n",""))
for I in command.env_var_value:
  newEnvVarValue.append(I.replace("\n",""))
endPrint = False
for I in command.env_var_name:
    if(command.new_arg_parser("-0") or command.new_arg_parser("--null")):
      print(str(I).replace("\n","")+"="+str(command.env_var_value[count]).replace("\n",""),end=" ")
      endPrint = True
    else:
      count3=0
      for D in sys.argv:
        if(len(sys.argv)!=1):
          if(D not in newEnvVarName and count3!=0):
            print(str(I).replace("\n","")+"="+str(command.env_var_value[count]).replace("\n",""))
            break
        else:
          print(str(I).replace("\n","")+"="+str(command.env_var_value[count]).replace("\n",""))
          break
        count3+=1
    count+=1

if(endPrint == True):
  print()

if(len(sys.argv)!=1):
  for I in sys.argv:
    if(I in newEnvVarName):
      newCount = 0
      for O in newEnvVarName:
        if(I == O):
          print(newEnvVarValue[newCount])
        newCount+=1
