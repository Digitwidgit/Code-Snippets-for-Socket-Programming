import os

#get the current working directory.
my_directory = os.getcwd()

#Find the drive leter (c:, d:, e:..) by slicing the string.
#There are 3 positions. Start:Stop:Step. First number tells starting position -
#So the 0 would start with the first character. The second number tells it where -
#to stop. So here it is stopping on the 2. Remember, it always starts with 0, no 1.
#Last is telling it how many to step. We stated 1, so it will could over only by ones.
#So looking at the string -> c:\myfolder\mynextfolder... We can determine that -
#0 position is starting with the first character which is 'c'. The 2 would be counting-
#until "\". However, it will always subtract left one character. So instead of printing-
#c:\, it will step back one and only print c:.
find_drive_letter = my_directory[0:2:1]

#This tellis it to start on character 2, which would be the "\" from c:\. and because-
#we put ":", that tells it to count all the way to the end of the string. Hence, we get-
#everything to the right of c:. --> \directroy\nextdirectroy\...
my_path = my_directory[2:]



#Printing the results of the drive letter.
print("This is my drive letter: " + "[" + find_drive_letter + "]")

#Printing the results of the path.
print("This is the path after the drive letter: " + '"' + my_path + '"')

#Combining both the drive letter and the path. The "|" character allows it too all be on-
#the same line.
print("Combining both the drive letter and the path --> " + find_drive_letter + my_path, end="|")
print("All on the same line", end="|")
print("Even thought its on a new line within the code")
