n=7
if n<=0:
    print("not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
        else:
            print("prime number")
            break

print("github test")