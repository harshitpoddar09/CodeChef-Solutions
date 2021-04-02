# cook your dish here
def isPrime(n):
    if n<=1:
        return False
    for j in range(2,n):
        if n%j==0:
            return False
    return True
    
t=int(input())
for i in range(t):
    n=int(input())
    if isPrime(n):
        print('yes')
    else:
        print('no')