# 判断一个数是不是质数
def exercise1():
    num = int(input("please input a number which to be tested:"))
    isPrime = True
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

# 把exercise1()写为函数
def is_prime(num:int) -> bool:
    '''判断一个数是否是质数'''
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

#升级: 如果不是质数,输出所有因子
def exercise2():
    num = int(input("please input a number which to be tested:"))
    is_prime = True
    element=[]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            element.append(i)

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number,and it have {int(len(element))*2} elements(without 1 and itself):")
        for i in element:
            print(f"{num}={i}x{int(num/i)}",end='\t')
        print()

#把exercise2()写为函数
def show_elements(num:int)->list:
    is_prime = True
    element = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            element.append(i)
    if is_prime:
        for i in element:
            element.append(int(num/i))
    return element

#再升级,给出指定范围内的所有质数
def exercise3():
    num_min = int(input("please input a lowered number:"))
    num_max = int(input("please input a highered number:"))
    element=[]
    for i in range(num_min, num_max + 1):
       if is_prime(i):
           element.append(i)
    print(element)

#把exercise3()写为函数
def show_prime_elements(num_min:int,num_max:int)->list:
    element = []
    for i in range(num_min, num_max + 1):
        if is_prime(i):
            element.append(i)
    return element

""""
输出指定范围的数的质数解析, 质数标记,如果不是质数则写出因子
"""

import os
import platform

def clear_terminal():
    """跨平台清空终端屏幕"""
    # 判断操作系统类型
    if platform.system() == "Windows":
        # Windows 系统清屏指令：cls
        os.system("cls")
    else:
        # macOS/Linux 系统清屏指令：clear
        os.system("clear")


def exercise4():
    num_min = int(input("please input a lowered number:"))
    num_max = int(input("please input a highered number:"))
    element = []
    for i in range(num_min, num_max + 1):
        if not is_prime(i):
            for j in show_elements(i):
                print(f"{i}={j}x{int(i/j)}",end='\t')
            print()
        else:
            print(f"{i} is a prime number")
#实现一个小的质数游戏机

def game_prime_number():
    '''实现以上全部功能'''
    while True:
        numbers=int(input("Please select an option:\n"
                      "\t1.\tDetermine if a number is prime; if not, output its factor.\n"
                      "\t2.\tOutput prime numbers within the specified range\n"
                      "\t3.\tOutput prime number analysis for all numbers within a specified range\n"))
        match numbers:
            case 1: exercise2()
            case 2: exercise3()
            case 3: exercise4()
        input("Press any key to return to the homepage.")
        clear_terminal()

if __name__ == '__main__':
    #exercise1()
    #exercise2()
    #exercise3()
    game_prime_number()