import random
num = [1]
lo,hi = 933,1866
mid = int((hi+lo)/2)
ave=sum(num)/len(num)
while(not(ave>(mid*.95) and ave<(mid*1.05))):
    num=[]
    for i in range(10):
        num.append(random.randint(lo,hi))
    ave=sum(num)/len(num)
    print(ave)
print(num)
