
import os

#file path with the file name.
file_name = "c://users//username//downloads//somefile.pdf"
#use os to get the file size of the file name.
file_size = os.path.getsize(file_name)

#create a variable wand put the command "download" to request. Put the file name and file size as well.
filedata = (f"download{file_name}@{file_size}")
print("File size was extracted:" + '[',file_size,']')

#check for the command "download" at [:8] 0-8.
sliced = filedata[:8]
#check for everything after 8. Which is the file name and file size.
sliced2 = filedata[8:]
print("This is the comand to request the download: " + "[" + sliced + "]")
print("This is the filename and filesize in an fstring: " + "[" + sliced2 + "]")

#create 2 variable and split the data into the appropriate var. File name data into file_name and file size data into file_size.
file_name, file_size = sliced2.split('@')
print("")
print("This is the path: " + "[" + file_name + "]", '\n' "This is the filesize: " + "[",file_size,"]")

# x is just the starting position of the file name by using the most right '/' of the path.
x = file_name.rfind('/') + 1
#extracting the name by statring with position x and got to the end of the line.
return_name = file_name[x::]
print("This is the filename: " + "[" + return_name + "]")

#returning to the data to the other computer (if used in sockets). Put the command "download" the file name  and file size separated by @.
return_data = (f"download{return_name}@{file_size}")
#This is the "download" command.
sliced = return_data[:8]
print("This is the command: " + "[" + sliced + "]")
#This is everthing after the "download" command.
return_data = return_data[8:]
print("This is the filename and filesize together: " + "[" + return_data + "]")
#puth the file name into the var returh_name and the file size into file_size. Split by using @.
return_name, filesize = return_data.split('@')
print("")
print("The returned file name is:" + "[" + return_name + "]" '\n' "The returned filesize is:" + "[",filesize,"]")

