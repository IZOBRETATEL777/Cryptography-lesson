# Iterative Function to calculate (x^y) in O(log y)
def power(x, y):
     
    # Initialize result
    res = 1   
  
    while (y > 0):
       
        # If y is odd, multiply x with result
        if ((y & 1) != 0):
            res = res * x
  
        # y must be even now
        y = y >> 1 # y = y/2
        x = x * x  # Change x to x^2
         
    return res


def findPower(a,x,n):
    for i in range(0,n):
        if (power(a,i)%n==x):
            return i
        
# Iterative Function to calculate
# (x^y)%p in O(log y)
def powerAndMod(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res
print(powerAndMod(2,5,13))













