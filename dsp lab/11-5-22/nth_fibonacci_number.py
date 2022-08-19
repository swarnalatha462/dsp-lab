def fib(n):
    if(n==0):
        print("0")
    elif(n==1):
        print("1")
    else:
        n1=0
        n2=1

    for i in range(2,n):
        n3=n1+n2
        n1,n2=n2,n3
        print(n3)
		
n=int(input())
print(fib(n))
