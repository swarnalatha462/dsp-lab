n=int(input("Enter a number: "))
n1,n2=0,1
print(n1,end=" ")
print(n2,end=" ")
n3=n1+n2
while(n3<n):
	print(n3,end=" ")
	n1,n2=n2,n3
	n3=n1+n2
