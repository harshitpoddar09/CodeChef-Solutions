# cook your dish here
n=int(input())
weapons=list(map(int,input().split()))
even=0
odd=0
for i in weapons:
    if i%2==0:
        even+=1
    else:
        odd+=1
if even>odd:
    print('READY FOR BATTLE')
else:
    print('NOT READY')