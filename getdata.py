
import os


file_name = "c://users//nater//downloads//Kibo_Code_Module_2.pdf"
file_size = os.path.getsize(file_name)


filedata = (f"download{file_name}@{file_size}")
print("File size was extracted:" + '[',file_size,']')

sliced = filedata[:8]
sliced2 = filedata[8:]
print("This is the comand to request the download: " + "[" + sliced + "]")
print("This is the filename and filesize in an fstring: " + "[" + sliced2 + "]")

file_name, file_size = sliced2.split('@')
print("")
print("This is the path: " + "[" + file_name + "]", '\n' "This is the filesize: " + "[",file_size,"]")


x = file_name.rfind('/') + 1
return_name = file_name[x::]
print("This is the filename: " + "[" + return_name + "]")

return_data = (f"download{return_name}@{file_size}")
sliced = return_data[:8]
print("This is the command: " + "[" + sliced + "]")
return_data = return_data[8:]
print("This is the filename and filesize together: " + "[" + return_data + "]")
return_name, filesize = return_data.split('@')
print("")
print("The returned file name is:" + "[" + return_name + "]" '\n' "The returned filesize is:" + "[",filesize,"]")

