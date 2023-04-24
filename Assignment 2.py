n = int(input("Enter number of elements : "))
 
a = list(map(int,
    input("\nEnter the numbers : ").strip().split()))[:n]

print("The original list is : " + str(a))
res = 0
for i in a:
    from math import pow
    res += pow(i, 2)
res = int(res)
print("The sum of squares of list is : " + str(res))
