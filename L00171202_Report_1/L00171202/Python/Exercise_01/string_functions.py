#string functions
a="we had great time"
print(a)

#length
print("String length = ", len(a))

#type
print(type(a),"\n")

#splitting string
print("splitting string:", a.split())

#join
print("Joining string:", ''.join([a.split()[0],a.split()[3]]))
print("Joining string:", '@'.join(a.split()))

#range
print(list(range(0,15,5)))

#lower
print("string in lowercase:", a.lower())

#islower
print("Is string in lowercase?\t", a.islower())
print(a.split()[3] + " - islower?\t", a.split()[3].islower())

#upper
print("string in uppercase:", a.upper())

#isupper
print("is string in uppercase?\t", a.isupper())

#index
print("Indexing: ", a.index("gre"))

#find
print("Is 'great' in string? ","great" in a)

#isalnum
print("Is string alphanumeric?\t", a.isalnum())

#isalpha
print("Is string alphabetic?\t", a.isalpha())

#title
print("Title case a string:\t", a.title())

#istitle
print("Is string titlecases?\t", a.istitle())

#swapcase
print("Swapping:\t", a.swapcase())

#removeprefix
print("Remove prefix 'we had':", a.removeprefix('we had'))

#removesuffix
print("Remove suffix 'great time':", a.removesuffix('great time'))
