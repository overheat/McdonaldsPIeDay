#!/usr/bin/env python3

def day(n):
    if n==1:
        return 6 
    return inc + day(n - 1)

def total(n):
    if n == 1:
        return day(1)
    return day(n) + total(n - 1)

n = int(input('Please input how many days: ')) 
inc = int(input('Please input how many increment: '))

#print(day(n))
print('XiaoMai will eat', total(n), 'pie in March!')