import os
import glob

file1 = glob.glob("C:/Users/robert.flores/Downloads/*.csv", recursive=True)

for file in file1:
    try:
        os.remove(file)
    except OSError as e:
        print("Error: %s : %s" % (file1, e.strerror))

file2 = glob.glob("C:/Users/robert.flores/Downloads/Vulnerabilit*.*", recursive=True)

for file in file2:
    try:
        os.remove(file)
    except OSError as e:
        print("Error: %s : %s" % (file2, e.strerror))