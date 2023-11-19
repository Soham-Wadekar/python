# 3. Create a program that prints a pattern of numbers in the form of a right-angled triangle.

num = 10

for i in range(1,num):
    for j in range(1,i+1):
        print(j,end=" ")
    print()