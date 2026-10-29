arr=[5,8,12,20,25,30,45,60,72,88]
print("Sorted list:",arr)

t=int(input("Enter number to search:"))
f=False 
for i in range(len(arr)):
    if arr[i]==t:
        print("Element found at index:",i)
        f=True
        break
if not f:
    print("Element not found!")