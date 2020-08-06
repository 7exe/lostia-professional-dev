import time
import os
import datetime
import ctypes
import sys
from command import end


list = [
'''
 $$$$$$\\
$$$ __$$\\
$$$$\ $$ |
$$\$$\$$ |
$$ \$$$$ |
$$ |\$$$ |
\$$$$$$  /
 \______/''',
'''
  $$\\
$$$$ |
\_$$ |
  $$ |
  $$ |
  $$ |
$$$$$$\\
\______|''',

 '''
  $$$$$$\\
$$  __$$\\
\__/  $$ |
 $$$$$$  |
$$  ____/
$$ |
$$$$$$$$\\
\________|''',
'''
 $$$$$$\\
$$ ___$$\\
\_/   $$ |
  $$$$$ /
  \___$$\\
$$\   $$ |
\$$$$$$  |
 \______/''',
 '''
$$\   $$\\
$$ |  $$ |
$$ |  $$ |
$$$$$$$$ |
\_____$$ |
      $$ |
      $$ |
      \__|''',
'''
$$$$$$$\\
$$  ____|
$$ |
$$$$$$$\\
\_____$$\\
$$\   $$ |
\$$$$$$  |
 \______/ ''',
 '''
 $$$$$$\\
$$  __$$\\
$$ /  \__|
$$$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
 \______/ ''',
'''
$$$$$$$$\\
\____$$  |
    $$  /
   $$  /
  $$  /
 $$  /
$$  /
\__/''',
'''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
$$  __$$<
$$ /  $$ |
\$$$$$$  |
 \______/ ''',
 '''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
\$$$$$$$ |
 \____$$ |
$$\   $$ |
\$$$$$$  |
 \______/ '''
]
colon = '''
$$\\
\__|
$$\\
\__|'''




ti = str(datetime.datetime.now())
ti = ti[11:19]

lines = ["","","","","","","","",""]
line = 0

numbers = [[],[],[],[],[],[],[],[]]
for x in range(8):
    if ti[x].isdigit():
        #print list[x]
        numbers[x] = list[int(ti[x])].splitlines()
    elif ti[x] == ":":
        numbers[x] = colon.splitlines()

for x in range(9):
    temp = ""
    for i in range(9):
        #print x,i
        try:
            if i != 8:
                temp += str(numbers[i][line]).ljust(10)
            else:
                temp += str(numbers[i][line])
        except:
            temp += "          "
    lines[x] += temp
    line += 1

    #print lines

for x in range(9):
    print(lines[x])

#done = False

print()

end(sys.argv)