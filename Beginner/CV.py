# cook your dish here
def cv(n,s):
    vowels=['a','e','i','o','u']
    i=0
    count=0
    while i<n-1:
        if s[i] not in vowels and s[i+1] in vowels:
            count+=1
            i+=2
        else:
            i+=1
    return count
t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    print(cv(n,s))