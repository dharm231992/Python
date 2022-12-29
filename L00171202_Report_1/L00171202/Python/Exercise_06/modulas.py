#

"""this function takes two integer values and returns true if the first number is divisible by second and false if the first number is not divisible by second"""

def divisible(numerator: int, denominator: int)->bool:
 return numerator % denominator == 0
print(divisible(30,4))
print(divisible(4,2))#prints true as 4 is divisible by 2



