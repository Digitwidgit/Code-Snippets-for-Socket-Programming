
cmd = 'call function'
cmd2 = 'Test!'



if cmd.split(" ")[1] == "function":
        print(f"{cmd}")
        x = cmd.split(" ")[0]
        x2 = cmd.split(" ")[0] + " " + cmd.split(" ")[1]
        cmd = cmd.split(" ")[1]
        print(cmd) # split the cmd var and look and index 1, 'function'.
        print(x) # var x = the 0 index of the cmd var value, 'call'.
        print(x2) # var x2 = the value of both indexes in the cmd var. Index 0 and 1.

else:
    print("not working!")


def the_test():
    print("The function is working!!!!!!!!!!!!!")

print("Outside the function")


test = '123'
if test == '123':
    the_test()
