import os
import  sys

myfile= raw_input("Enter the filename to delete: ")

try:
    os.remove(myfile)
except OSError as e: # if failed, report it back to the user
    print("Error: %s - %s." % (e.filename, e.strerror))