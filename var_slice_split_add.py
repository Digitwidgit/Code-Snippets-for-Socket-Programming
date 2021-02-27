
send_data = "ok@"
send_data += "LIST: all files from the server.\n"
send_data += "UPLOAD <path>: Upload a file to the server.\n"
send_data += "DELETE <filename>: Delete a file from the server.\n"
send_data += "LOGOUT: Disconnect from the server.\n"
send_data += "HELP: List all commands."

cmd, msg = send_data.split('@')
if cmd == "ok":
    print(f"{msg}")
else:
    print("Missing ok!")

file_size = 1024
file_path = "c://users//someone//downloads//beautiful_girl.jpg"
x = file_path.rfind('/') + 1
file_name = file_path[x::]
cmd = "download"
print("")

data = (f"{cmd}@{file_path}@{file_name}@{file_size}")
a, b, c, d = data.split('@')

print("The command is: [" + a + ']' + '\n' + "The file path is: [" +  b + ']' + '\n' + "The file name is: [" + c + ']' + '\n' + "The file size is:(",d,'kb)')
print("")

x = (a, b, c, d)
for i in x:
    print(i)




