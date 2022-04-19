# Python 3 implementation of fermat's factorization
 
from math import ceil, sqrt
 
#This function finds the value of a and b
#and  returns a+b and a-b
def FermatFactors(n):
 
   # since fermat's factorization applicable
   # for odd positive integers only
    if(n<= 0):
        return [n] 
 
    # check if n is a even number
    if(n & 1) == 0: 
        return [n / 2, 2]
         
    a = ceil(sqrt(n))
 
    #if n is a perfect root,
    #then both its square roots are its factors
    if(a * a == n):
        return [a, a]
 
    while(True):
        b1 = a * a - n
        b = int(sqrt(b1))
        if(b * b == b1):
            break
        else:
            a += 1
    return [a-b, a + b]
     
# Driver Code
print(FermatFactors(int(input("Enter the number: "))))
