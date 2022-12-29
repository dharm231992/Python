"""
 Script: main.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load
from time import sleep

#Check OS, log file name and path
this_os=detect_os()
log_path=path_name()
filename=log_file_name(".csv")

while True:
    #sleep for 1 second
    sleep(1)
    
    # Get a time stamp for this line
    timestamp=log_file_name("")
    # Get cpu information
    information=cpu_load()
    # Create a line for the logfile, convert the integer values to string
    logline=timestamp+":"+str(information[0])+","+str(information[1])+"\n"
    
    #write to logfile
    try:
        with open(filename, "a") as file_handle:
            print(f"logging to {filename}")
            file_handle.write(logline)
    except IOError as err:
        print("IOError was {err}")
    except EOFError as err:
        print("EOFError was {err}")
    except OSError:
        print("OSError")
    except:
        print("General Error")
