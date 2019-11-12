n,m,a=map(int,input().split())
if m%a==0:
    f=m//a
else:
    f=m//a+1
if n%a==0:
    d=n//a
else:
    d=n//a+1
print(f*d)
