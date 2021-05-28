#! /bin/python3
# n = int(input())
# # dictionary={input():[int(y) for y in input().split()] for _ in range(n)}
# dic = {}
# for _ in range(int(input())):
#     x = input().split()
#     dic[x[0]] = x[1:]
#
#
# print("%.2f"%(float((sum(dictionary.get(input())))/n)))
# dic = {}
# for _ in range(int(input())):
#     x = input().split()
#     dic[x[0]] = x[1:]
# ask = list(map(int,dic[input()]))
# print(f'{sum(ask)/len(ask):.2f}')
# data = {}
# for i in range(int(input())):
#     dum = input().split()
#     data[dum[0]] = list(map(float,dum[1:]))
# name = input()
# print("{:.2f}".format(round(sum(data[name])/len(data[name]),2)))
# x =
# print(input().swapcase())

#
#
# import math
# import time
# def colored(r, g, b, text):
#     return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
# c='#'
# width = 40
# r =255
# for i in range(1,width//10+1):
#     time.sleep(1)
#     print (colored(255,20,147,(((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
#            (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)))
#
# for i in range((width//4-1),0,-1):
#     time.sleep(1)
#     r=r-25
#     print (colored(r,20,147,((c*i*4).center(width))))
# print(colored(r,20,147,((c*2).center(width))))


# str  = input()
# n = int(input())
# for  i in range(len(str)):
#     if i%n == 0 :
#         print("\n",end="")
#     print(str[i],end="")
# print("")



# x , y  = list(map(int,input().split()))
# c = "-"
# for i in range(x):
#     for j in range(y):
#         print("-",end="")
#         print ((c*j*4).center())
#     print("")
# massage = "kapil"
# print(massage.center(10,"*"))


# import math

# c='.|.'
# n,m =[int(x) for x in input().split()][:2]
# for i in range(1,n):
#     if(i%2 != 0):
#         print ((c*i).center(m,"-"))
# print("WELCOME".center(m,"-"))
# for i in reversed(range(1,n)):
#     if(i%2 != 0):
#         print ((c*i).center(m,"-"))



# print("{:^10}".format("sainihab"))




# n = int(input())
# width = len("{:b}".format(n))
# for num in range(1,n+1):
#     for base in 'dXob':
#          print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
#     print()




# n = int(raw_input())
# width = len("{0:b}".format(n))
# for i in range(1,n+1):
#     print("{0:{width}d} {0:{width}o} {0:{width}X}{0:{width}b}".format(i, width=width))


n = int(input())
for  i in reversed(range(98,n+97)):
    print("{:c}".format(i).center(4*n-2,"-"),end="")
    for  j in range(97,n+97):
    print("{:c}".format(i).center(4*n-2,"-"))
