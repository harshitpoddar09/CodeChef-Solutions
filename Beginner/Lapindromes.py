# cook your dish here
def lapindrome(s):
    if len(s)%2==0:
        a=s[:len(s)//2]
        b=s[len(s)//2:]
    else:
        a=s[:len(s)//2]
        b=s[(len(s)//2)+1:]
    for i in set(a):
        if a.count(i)!=b.count(i):
            return 'NO'
    return 'YES'
    
t=int(input())
for i in range(t):
    s=str(input())
    print(lapindrome(s))