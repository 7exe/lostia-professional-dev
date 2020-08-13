import command

count = 0
for I in command.env_var_name:
  print(str(I).replace("\n","")+"="+str(command.env_var_value[count]).replace("\n",""))
  count+=1