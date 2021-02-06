import os
import time

path = 'c:\\users\\nater'

files = os.listdir(path)

for f in files:
    time.sleep(.10)
    print(f)
