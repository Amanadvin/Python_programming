"""
a = open("aman.txt","w")
a.write("hello I am Romeo advin .")
a.close()
"""

"""
a=open("aman.txt","r")
print(a.read())
"""

"""
a=open("aman.txt","a")
a.write("I am append")
a.close()
"""

#************************************************************** HOW TO CREATE DIFFERENT FILE **********************************************************************

#open("advin.pdf","w")
#open("advin.mp4","w")
#open("advin.xlsx","w")
#************************************************************   IMPORTANT LIBRARIES  ****************************************************************************

import os
#os.rename("aman.txt","advin.txt")
#os.remove("advin.xlsx")
#os.mkdir("hello123")
#os.rmdir("hello123")

#************************************************************   IMPORTANT LIBRARIES ("COPY AND MOVE THE FILES ") **************************************************


import shutil

#shutil.copy("advin.pdf","C:\\Users\\ak682\\Desktop\\AMAN SCH")

#shutil.move("advin.xlsx","C:\\Users\\ak682\\Desktop\\AMAN SCH")

#************************************************************   IMPORTANT LIBRARIES ("SEARCHING THE FILE AND FOLDER  ") *****************************************************


import os.path

#print(os.path.isfile("C:\\Users\\ak682\\Desktop\\AMAN SCH"))

#if(os.path.isfile(r"C:\Users\ak682\Desktop\Project_quizgame.py")):
 #   print("file found")
#else:
 #   print("file not found ")



import os.path

#print(os.path.isfile("C:\\Users\\ak682\\Desktop\\AMAN SCH"))

#if(os.path.isdir(r"C:\Users\ak682\Desktop\BAJRANGI")):
 #   print("file found")
#else:
#    print("file not found ")

#************************************************************   IMPORTANT LIBRARIES ("SEARCHING THE FILE AND FOLDER  ") *****************************************************

import zipfile

#x = zipfile.ZipFile("myzipfile.zip","w")
#x.write("advin.pdf")
#x.write("advin.mp4")
#x.close()

#x = zipfile.ZipFile("myzipfile.zip")
#x.extractall(r"C:\Users\ak682\Desktop\data file")


"""
a1 = [1,2,3,4,5]
a2 = [6,7,8,9,10]

z = list(zip(a1,a2))
print(z)

for i,j in z:
    print(i+j)

"""

