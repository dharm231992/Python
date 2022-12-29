"""This function will take a list of integers and an integer to be searched in the passed list. If found returns True else None"""
def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)
"""We are getting None because number 9 is not present in the search list passed to the find_num function"""
#lets add 9 to the search list so that we can get a true in return
result = find_num([1,2,3,4,5,6,7,8,9], 9)
print(result)

"""Updated code to return False if number not found in the search list"""

def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
    return False
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

"""This function will take a list of integers. It will return True if an even number is found in the list else False"""
def find_even_num(number_list: list)->bool:
    for iterate_number in number_list:
        if iterate_number % 2 ==0:
            return True
    return False
result = find_even_num([1,2,3,4,5,6,7,8])
print(result)

"""lambda function to find the volume of a cylinder. takes radius(r) and height(h) as arguments 
and returns volume of the cylinder calculated using the standard formula"""
cyl_vol = lambda r,h : 3.14*r*r*h
print(cyl_vol(2,3))