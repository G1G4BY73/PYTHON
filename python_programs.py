#! /bin/python3


#To check Number is even or odd

# print("even") if int(input()) %2 == 0 else print("odd")


#Factorail of a Number

# def factorial(n):
#     if (n < 0):
#         return "factorial of a negative number is not possible."
#     elif (n == 0):
#         return 1
#     else:
#         return n*factorial(n-1)
# result = factorial(int(input()))
# print(result)


# check weather a number is prime or not

# n = int(input())
# if(n==1 or n==2):
#     print("Prime Number")
# else:
#     for i in range(2,n):
#         if(n%i ==0):
#             print("Not a Prime Number")
#             break
#         else:
#             print("Prime Number")
#             break


# Largest among n digits

# n= int(input())
# list = [int(x) for x in input().split()][:n]
# list.sort(reverse=True)
# print(list[0])

#Swap two numbers without using third variable

# x,y =[int(x) for x in input().split()][:2]
# print(f"x is {x} and y is {y}")
# x,y=y,x
# print(f"after reverse \nx is {x} and y is {y}")


#Swap two numbers without using third variable non-pyhtonic way

# x,y = [int(x) for x in input().split()][:2]
# print(f"x is {x} and y is {y}")
# x = x+y
# y = x -y
# x =x-y
# print(f"After reverse \nx is {x} and y is {y}")


#Priniting fibonacci series till n'th term:

# n = int(input())
# t =[0,1]
# for i in range(3,n+1):
#     x = t[i-2]+t[i-3]
#     t.append(x)
# for i in t:
#     print(t[i],end=" ")
# print()

#check palindrome

# n = int(input())
# temp=n
# y=0
# while(n):
#     x=n%10
#     y=y*10 +x
#     n=n//10
# print("Palindrome") if y == temp else print("Not Palindrome")



#Pascal Triangle


n = int(input())
for i in range(n):
    for j in reversed(range(n)):
        print(" "*j +"1"  )
