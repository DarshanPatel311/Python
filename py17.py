arr = []  
temp = 0;    
a=int(input('Enter Array Size:')) 
for k in range(a):
    l=int(input('Enter Array:'))
    arr.append(l)
print('Elements of array: ');    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
  
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     

    
print('Sort an array in ascending order.');    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    