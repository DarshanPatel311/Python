

x = int(input("Enter lenth "))


n1, n2 = 0, 1
count = 0


if x <= 0:
   print("Please enter a positive integer")

elif x == 1:
   print("Fibonacci sequence upto",x,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < x:
       print(n1)
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1

