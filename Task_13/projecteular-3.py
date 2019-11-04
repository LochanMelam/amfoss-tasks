t=int(input()) #number of test cases
for i in range(t):
	n=int(input()) #input
	a=[] #for every test case the list becomes empty
	for j in range (2,n+1):
		c=0 
		for k in range(2,j+1):
			if j%k==0:
				c=c+1
		if c<2:
			a.append(j) #appends all the prime numbers upto input in the list a
		lis=[]
	for b in range(len(a)):
		if n%a[b]==0:
			lis.append(a[b]) #here b list is appended with list of all prime numbers which exactly divides input
	print(max(lis))
			
			

