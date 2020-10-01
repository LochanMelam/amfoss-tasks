n=int(input("enter number of expressions "))
lis=[]
c=0
for i in range(0,n):
    expression=input("enter variable in capital letter ")
    lis.append(expression) 
for j in range(0,len(lis)):
    if lis[j]=="++X" or lis[j]=="X++":
        c+=1
    else:
        c-=1
print(c)
