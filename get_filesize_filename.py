import os

file_path = "c://users//nater//documents//6.zip"
file_size = os.path.getsize(file_path)
print(file_size)

x = file_path.rfind('/') + 1

file_name = file_path[x::] 
print(file_name)

#file_size = str(file_size)
the_data = (f"{file_size}@{file_name}")
print(the_data)

filesize, filename = the_data.split('@')
print("This is the file size:" + filesize, '\n' "This is the filename:" + filename)

