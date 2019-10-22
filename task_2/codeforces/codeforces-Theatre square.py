n=list(map(int,input().split()))
m=n[0]
for i in range(0,len(n)):
    if m>n[i]:
        m=n[i]
print(m)
