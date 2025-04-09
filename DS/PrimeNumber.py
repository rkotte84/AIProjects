
a = 2
n = input("Enter a number: ")
n = int(n)
while a <= n-1:
    if n % a == 0:
        print(n, "is not a prime number")
        break
    else:
      a += 1
else:
     print(n, "is a prime number")

