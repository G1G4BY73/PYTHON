#! /bin/python3

# for i in range(int(input())):print("*"*(i+1))

# n = int(input())
# for i in reversed(range(n)):print(" "*(i) + "*"*(n-i))

# n = int(input())
# for i in range(n):print(("* "*(i+1)).center((n*2)-1))


n =int(input())
for i in range(1,n+1):
    for  j in range(1,i+1):print(str(j)+ " ",end=" ")
    print()
