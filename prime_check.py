def primes(n):
    count=0
    for i in range (2,n):
        if n%i==0:
            count+=1
            break
    if count==0:
        print("prime")
    else:
        print("not prime")

            
n= int(input("enter a number :"))
       
primes(n)       
