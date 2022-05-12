t= int(input()) #gets number of test cases 
for i in range(t):
	sum=0
	k=int(input())
	for j in range(1,k): #checking for multiples of 5 and 3 below 10
			if j%3==0 or j%5==0:
				sum=sum+j
				
	print(sum)
