# Write code for algorithm 2 below

# 2. Write a function that prints the natural numbers from 1 to n.

def natural_numbers(x,i = 1):
    if i > x:
        return
    else:
        print(x)
        natural_numbers(x-1)

natural_numbers(5)