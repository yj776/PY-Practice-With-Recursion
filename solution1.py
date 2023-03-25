# Write code for algorithm 1 below

# 1.  Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def count_down(n):
    if n == 0: 
        return
    else: 
        print(n)
        count_down(n-1)

n = 8 
count_down(n)