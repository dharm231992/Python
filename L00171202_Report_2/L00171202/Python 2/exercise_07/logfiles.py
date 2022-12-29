"""
 Script: logfiles.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

filename="logfile.txt"

try:
    with open(filename, "w") as file_handle:
        print(f"Writing a test line to {filename}")
        file_handle.write("writing a log line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
finally:
    print("Finishing up!")
    #close not needed when using with statement
    #file_handle.close()
