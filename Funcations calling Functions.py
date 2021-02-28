
import time

def make_file():
    print("Wait one moment .....")
    x = input("Please write something >> ")
    f = open('myfile.txt','w')
    f.write(x)
    f.close()
    print('"' + x + '"' + " was written to file.")
    time.sleep(2)

    f = open('myfile.txt', 'r')
    x = (f.read())
    time.sleep(1)
    print('"' + x + '"' + " was read from the file!")
    
    
def function3():
    print("so great now")
    make_file()
    
def function2():
    print("were")
    function3()

def function1():
    print("okay!")
    function2()
    
test = '10'
if test == '10':
    function1()





