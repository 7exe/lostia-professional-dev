import command


currentVersion = "1.4.1"
Name = "Adaptable Shell"
Access = "Early Alpha"
Calced1 = 26-len(Name)
Empty1 = " "*Calced1 
Calced2 = 26-len(currentVersion)
Empty2 = " "*Calced2
Calced3 = 26-len(Access)
Empty3 = " "*Calced3
EnabledModules = str(len(open("LostiaMain/ModuleConf.config").readlines()))
Calced4 = 26-len(EnabledModules)
Empty4 = " "*Calced4
Users = str(len(open("LostiaFiles/keychain.keychain").readlines())-1)
Calced5 = 26-len(Users)
Empty5 = " "*Calced5


print("\x1b[6;30;47m┌────────────────┤        \x1b[6;31;47mAsh Shell\x1b[6;30;47m       ├────────────────┐")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│ \x1b[6;34;47mName\x1b[6;30;47m                          \x1b[6;107;44m"+Name+Empty1+"\x1b[6;30;47m │\x1b[0m")
print("\x1b[6;30;47m│ \x1b[6;34;47mVersion\x1b[6;30;47m                       \x1b[6;107;44m"+currentVersion+Empty2+"\x1b[6;30;47m │\x1b[0m")
print("\x1b[6;30;47m│ \x1b[6;34;47mDev Ver\x1b[6;30;47m                       \x1b[6;107;44m"+Access+Empty3+"\x1b[6;30;47m │\x1b[0m")
print("\x1b[6;30;47m│ \x1b[6;34;47mEnabled Modules\x1b[6;30;47m               \x1b[6;107;44m"+EnabledModules+Empty4+"\x1b[6;30;47m │\x1b[0m")
print("\x1b[6;30;47m│ \x1b[6;34;47mUsers added to shell\x1b[6;30;47m          \x1b[6;107;44m"+Users+Empty5+"\x1b[6;30;47m │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m│                                                          │\x1b[0m")
print("\x1b[6;30;47m└──────────────────────────────────────────────────────────┘\x1b[0m")
