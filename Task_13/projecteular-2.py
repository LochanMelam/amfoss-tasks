t=int(input()) #number of testcases given
a=0
b=1
c=0
d=0
for i in range(t):
	n=int(input()) #sum of even fibonacci number upto n
	while a<n:
		if  a%2==0:
			c=c+a
		a=b  #first term
		b=d  #second term
		d=a+b 
	print(c) 


