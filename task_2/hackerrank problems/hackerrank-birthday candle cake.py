b = int(input())
a=list(map(int,input().split()))
m=a[0]
c=0
for i in range(0,len(a)):
    if m<a[i]:
        m=a[i]
for j in range(0,len(a)):
    if a[j]==m:
       c=c+1
    else:
        c=c+0
print(c)
        
