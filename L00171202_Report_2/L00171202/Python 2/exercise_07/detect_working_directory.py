"""
 Script: detect_working_directory.py
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

if(__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    
    #get OS in lower case
    myos=detect_os()
    myos=myos.lower()
    
    #check for only windows or linux OS
    if myos == "windows":
        print("This system is Windows")
    elif myos == "linux":
        print("This system is Linux")
    else:
        print(f"Cannot continue, unidentified system: {myos}")
        sys.exit()
    
    #get cwd
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")
    
else:
    print(f"This module is called {__name__} and is being called by another script")