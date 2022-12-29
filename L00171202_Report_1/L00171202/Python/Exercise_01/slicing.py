#slicing a string
a = "wazir!"
print(a)

#printing first 3 letters
print("First 3 letters: "+ a[0:3:1])

#printing reverse string
print("Reverse string: "+ a[-1::-1])

#printing 4 letter
print("4th letter: "+ a[3])

#reassembling a string
b= "Antivirus"
first_letters=b[0:4:1]
last_letters=b[-1:-6:-1]
insert_letter='Y'
new_name=first_letters+insert_letter+last_letters
print("Old String: "+ b +", inserted letter: "+ insert_letter)
print("New String: "+ new_name)

#String Interpolation
name="Antivirus"
print("Old String: "+ name)
name = name[0:4:1] + "Y"  + name[4:]
print("New String: "+name)