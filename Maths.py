import math
#Python includes the following function that perform mathametical calculations.
#1. abs(x) It returns absolute value of x- the (positive) distance between x and zero.
print("The Absolute values are\n:",abs(-45))
print(abs(119.4))

#2. max(x,y,z,....) max() returns the largest of its arguments the value closest to positive infinetly.
print("Maximum Values are\n ",max(10,20,30,10,50,50,800))
print(max(-10,20,50,80,46,2,56))

#3.min(x,y,z,....) It returns the smallest of its arguments the value closest to negitve infinetly.
print("Minimum values are:",min(10,20,30,10,50,50,800))
print(min(-10,20,50,80.,46,2,56))

#4.math.pow(x,y[,z]) It returns x to the power of y .if the third argument (z) is given it returns x to the power of y modulus z, i.e pow(x,y)%z. Note to use pow function we have to import math module
print("The power Values Are:",math.pow(100,2))
print(math.pow(3,0))

#5. round(x,n) It returns x roundes to n digits from the decimal point.
print("Round offed number is",round(80.234345,2))
print(round(1083.90757567,2))

#6. math.sqrt(x) It returns the square root of x for x>0 NOte: we have to import Math module
print("The Square root of the number are:",math.sqrt(100))
print(math.sqrt(8))


