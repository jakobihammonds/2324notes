s = 12
#hunter helped me

p = int(input("What is P: "))

def isEven(num):
    if num%2==0:
        return True
    else:
        return False

def isPrime(num):  
    if num > 1:
        # check factors
        for i in range(2,num):
            if (num%i) == 0:
                return False
        return True
# if input number is <_ 1 = not prime

def isLess(num,s):
    if num<s:
        return True
    else:
        return False

def isZero(s):
    if s == 0:
        return True
    else:
        return False


while True:
    if isEven(p):
        p+=1
        continue
    if not(isPrime(p)):
        p+=2
        continue
    if isLess(p,s):
        s-=p
        p+=2
        continue
    else:
        s-=1
        if s == 0:
            print(p)
            break
        else:
            p+=2
            continue