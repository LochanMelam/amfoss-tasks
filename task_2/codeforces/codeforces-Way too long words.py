n=int(input())
lis=[]
for i in range(0,n):
    word=input()
    lis.append(word)
for j in range(0,len(lis)):
    if len(lis[j])>10:
        c=0
        m=0
        d=str(lis[j])
        c=str(d[0])
        m=str(d[-1])
        l=str(len(lis[j])-2)
        print(c+l+m)
    else:
        print(lis[j])
