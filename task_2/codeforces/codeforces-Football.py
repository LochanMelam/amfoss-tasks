n=input()
c=0
for i in range(0,len(n)):
    if i<len(n)-1:
        if n[i]==n[i+1]:
            c=c+1
        else:
            c=c+0
    else:
        c=c+0
c+=1
if c<=6:
    print("No")
else:
    print("Yes")
