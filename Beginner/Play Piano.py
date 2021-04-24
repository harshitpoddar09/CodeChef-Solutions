# cook your dish here
def piano(s):
    j=0
    while j<len(s):
        if s[j]==s[j+1]:
            return 'no'
        else:
            j+=2
    return 'yes'
t=int(input())
for i in range(t):
    s=str(input())
    print(piano(s))