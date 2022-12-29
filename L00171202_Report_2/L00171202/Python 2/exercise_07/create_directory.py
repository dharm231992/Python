"""
 Script: create_directory.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

import os, platform

#global variable for current directory
current_working_directory = None

def detect_os() -> str:
    #return the OS in use
    return platform.system()

def detect_working_directory() -> str:
    #return directory name the script was run from
    return os.getcwd()

def create_directory(dirname:str) -> int:
    #check if directory already exist
    if os.path.isdir(dirname):
        #dir exists
        return 2
    else:
        #Use try/except to catch errors
        try:
            #create dir
            os.mkdir(dirname)
            #if this worked, return true
            return 0
        except:
            #give explicit error message
            print(f"Error creating directory {dirname}")
            #if this did not work, return false
            return 1

if(__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    
    #get OS in lower case
    myos=detect_os()
    myos=myos.lower()
    
    #check for only windows or linux OS
    if myos == 'windows':
        print("This system is Windows")
    elif myos == 'linux':
        print("This system is Linux")
    else:
        print(f"Cannot continue, unidentified system: {os}")
        sys.exit()
    
    #get cwd
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")
    
    #create directory
    if create_directory("SG")==0:
        print("Creating a directory worked.")
        #do other stuff
    elif create_directory("SG")==1:
        print("Directory could not be created.")
        #Do other stuff
    elif create_directory("SG")==2:
        print("Directory already exists.")
        #Do other stuff

else:
    print(f"This module is called {__name__} and is being called by another script")