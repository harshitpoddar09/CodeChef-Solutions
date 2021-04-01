# cook your dish here
t=int(input())
notes=[100,50,10,5,2,1]
for i in range(t):
    n=int(input())
    j=0
    ans=0
    while j<6:
        ans+=n//notes[j]
        n=n%notes[j]
        if n==0:
            break
        j+=1
    print(ans)