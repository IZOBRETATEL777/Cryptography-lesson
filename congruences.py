while True:
    a='no'
    try:
        a,b=map(int,input("Enter two integers: ").split())
        c=int(input("Enter the divisor: "))
        f=int(input("Enter integer to check whether prime or not: "))
        break
    except ValueError:
        print("Input numbers correctly!!!")
    except KeyboardInterrupt:
        print("If you want to exit just type 'yes'!!!\n")
        a=input("Here: ").lower()
    if a=='yes':
        print("Exiting...")
        break
try:
    def isCongruence(a,b):
        if a%c==b%c: return True
        return False

    def isPrime(a):
        for i in range(2,int(a**0.5)+1):
            if a%2==0: return False
        return True

    if (isCongruence(a,b)):k=' '
    else:k=" not "
    print("{0} and {1} are{3}congruence when divided by {2}".format(a,b,c,k))

    if(isPrime(f)):k=' '
    else:k=" not "
    print("{0} is{1}prime number".format(f,k))
except:
    pass
