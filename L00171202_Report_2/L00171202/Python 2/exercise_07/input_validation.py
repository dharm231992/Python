"""
 Script: validation_and_raising.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

def validate_integer():
    #Loop forever
    while True:
        try:
            user_input = int(input("Enter an integer value: "))
        except:
            #Bad value
            print("Error")
            continue
        else:
            print("Valid input")
            #exit loop
            break
        finally:
            #only runs after except, continue
            print("Try again - enter an integer value only!")

validate_integer()

#take input as string and convert to integer
value=int(input("Enter an integer greater than 10: "))

if value<=10:
    raise Exception("Vaue must be > 10")
else:
    print("Validation checks passed!")