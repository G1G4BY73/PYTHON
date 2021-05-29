#! /bin/python3

# for i in range(int(input())):print("*"*(i+1))

# n = int(input())
# for i in reversed(range(n)):print(" "*(i) + "*"*(n-i))

# n = int(input())
# for i in range(n):print(("* "*(i+1)).center((n*2)-1))


# for i in range(1,int(input())+1):
#     for  j in range(1,i+1):print(str(j)+ " ",end=" ")
#     print()


# k=1
# for i in range(1,(int(input())+1)):
#     for i in range(1,i+1):
#         print(k,end=" ");k=k+1
#     print()


# for _ in range (65,66+int(input())):print((chr(_)+" ")*(_-64))

# n=65
# for _ in range (1,int(input())+1):
#     for j in range(1,_+1):
#         print(chr(n),end=' ');n=n+1
#     print()


# n=int(input())
# for i in reversed(range(n)):print(("* "*(i+1)).center((n*2)-1))

# n = int(input())
# for i in range(n):print(("* "*(i+1)).center((n*2)-1))
# for i in reversed(range(n)):print(("* "*(i+1)).center((n*2)-1))


# for _ in reversed(range(int(input()))):print("* "*(_+1))

# n=int(input())
# for i in range(1,n+1):
#     print("* "*(n//2+1)) if n%2 == 0 else print("* "*(n//2+2)) if i == (n//2)+1 else print(("* "*(n//2)).center(n+2)) if i ==1 else print("*"+" "*(n-1)+"*") if n%2 == 0 else print(("* "*(n//2)).center(n+2)) if i ==1 else print("*"+" "*(n)+"*")


# n= int(input())
# for i in range(n):print("* "*n) if i == 0 or i == n-1  else print("*"+" "*(n*2-3)+"*")


# n = int(input())
# for i in range(n):
#     for j in range(n):print("* ",end="") if i==j or j==0 or i==n-1  else print("  ",end="")
#     print()
