#!/usr/bin/env python3

def print_fibonacci(length):
    fib_nums = []
    for n in range(length):
        if n == 0:
            fib_nums.append(0)
        elif n == 1:
            fib_nums.append(1)
        else:
            new_num = fib_nums[-1] + fib_nums[-2]
            fib_nums.append(new_num)
    
    print(fib_nums)