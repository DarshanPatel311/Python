arr=[]
n=int(input('Enter Array lenth:'))
max = 0
for j in range(n):
    z=int(input())
    arr.append(z)

for i in range(len(arr)):
    if(arr[i]>max):
        max=arr[i]
    
print(max,'Maximum in array')