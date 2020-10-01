a=list(map(int,input().split()))
b=list(map(int,input().split()))
ap=0
bp=0
for i in range (0,len(a)):
    if a[i]>b[i]:
        ap=ap+1
    elif b[i]>a[i]:
        bp=bp+1
    else:
        ap+=0
        bp+=0
print(ap)
print(bp)
