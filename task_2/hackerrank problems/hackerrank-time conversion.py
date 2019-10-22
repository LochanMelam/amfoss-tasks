n=list(map(str,input("enter time and specify am or pm").split(":")))
k=n[1]
j=n[2]
if n[2]=="AM":
    m=12-n[0]    
    print(m+":"+n[1]+":"+n[2])
else:
    print(n[0]+":"+n[1]+":"+n[2])
    
