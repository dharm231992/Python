"""
 Script: file_utilities.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

from datetime import datetime as dt
import sys, csv

def path_name():
    #OS dependent
    this_os=sys.platform
    
    if this_os=='win32':
        return './logfiles/'
    elif this_os=='linux':
        return '/home/pi/logfiles/'
    else:
        print(f"Unsupported OS {this_os}")
        exit(0)

"""
Create a file name in the logfiles directory, based on current data and time
Requires the computer to have an RTC or synched clock
"""

def log_file_name(extension):
    now=dt.now()
    file_name='%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    return file_name+extension

if(__name__=='__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    log_path=path_name()
    filename=log_file_name(".log")
    print(log_path+filename)
else:
    pass
