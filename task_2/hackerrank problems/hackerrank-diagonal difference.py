d=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
m=0
if d>3:
    l=list(map(int,input().split()))
    for i in range(0,1):
        k=a[i]+b[i+1]+c[i+2]+l[i+3]
        y=l[i]+c[i+1]+b[i+2]+a[i+3]
    m=k-y
    if m>=0:
        print(m)
    
    else:
        print(m*-1)
else:
    for j in range(0,1):
        k=a[j]+b[j+1]+c[j+2]
        y=c[j]+b[j+1]+a[j+2]
        m=k-y
    if m>=0:
        print(m)
    else:
        print(m*-1)
