"""
Script: lists.py
By: L00171202
Purpose: Working on Lists
"""

#creating list
my_list1=["a", "b", "c", 1, 3, 5]
print("1st list\t\t=", my_list1)

#no of elements in list
print("no of elements\t\t=", len(my_list1))

#getting an element
print("4th element of list\t=", my_list1[3])

#concatenate list
my_list2=[5,"r","n",8,5,"hello","letterkenny"]
print("2nd list\t\t=",my_list2)

#count
print("Repetition of '5'\t=", my_list2.count(5))

print("Concate both list\t=", my_list1+my_list2)

#remove
my_list2.remove("hello")
print("Removing 'hello'\t=", my_list2)

#changing element
my_list2[5]="welcome"
print("changed second list\t=", my_list2)

#append
my_list2.append("good bye")
print("Appended list\t\t=", my_list2)

#insert
my_list2.insert(5,"olla")
print("Insert to second list\t=", my_list2)

#extend
my_list1.extend([23,43,"w"])
print("Extend first list\t\t=", my_list1)

#reverse
my_list1.reverse()
print("Reversed first list\t=", my_list1)

#pop
print("Pop \t\t=", my_list2.pop(),"\n\tsecond list\t=",my_list2)

#listoflist
print("Nested list=", [my_list1,my_list2])




