a=[]
x=0
n=int(input("Enter th lenth:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)
for j in range(len(a)):
    x=x+a[j]
print(x)