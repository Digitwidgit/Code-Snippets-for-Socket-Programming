import os
import time

path = 'c:\\'

files = os.listdir(path)

#Time was set to 1/10th of a second. 
for f in files:
    time.sleep(.10)
    print(f)
