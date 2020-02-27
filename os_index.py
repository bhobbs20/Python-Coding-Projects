import os
import time

path = "/Users/pigeon/Tech_Docs/"
files = os.listdir(path)

for file in files:
    if file.endswith('.txt'):
        mod_time = os.path.getmtime(path)
        local_time = time.ctime(mod_time)
        print("{} Last modification: {}".format(file, local_time))
    else:
        ("Sorry there are no txt files available")


