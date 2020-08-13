import command
import sys

def echo():
  sysArr = sys.argv
  sysArr.pop(0)
  seperator = " "
  count=0
  count2=0
  hasFound = 0
  newEnvVarName = []
  newEnvVarValue = []
  for I in command.env_var_name:
    newEnvVarName.append(I.replace("\n",""))
  for I in command.env_var_value:
    newEnvVarValue.append(I.replace("\n",""))
  def update():
    for I in sysArr:
      if(I.replace("%","") in newEnvVarName):
        Index = newEnvVarName.index(I.replace("%",""))
        SysIndex = sysArr.index(I)
        sysArr[SysIndex] = str(newEnvVarValue[Index])
      else:
        if(I.startswith("%")):
          Index2 = sysArr.index(I)
          sysArr[Index2] = "null"

  update()

        
  print(seperator.join(sysArr))
  command.end(sys.argv)

echo()