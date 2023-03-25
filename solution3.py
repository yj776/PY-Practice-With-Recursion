# Write code for algorithm 3 below

# 3. Write a function that returns the first n elements in the Fibonacci Sequence.

def fibonacci_sequence(n):
    if n <= 0:
        print('Incorrect Input')
    elif n == 1:
        return(0)
    elif n == 2:
        return(1)
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

print(fibonacci_sequence(8))