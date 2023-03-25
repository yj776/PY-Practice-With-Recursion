# Write code for algorithm 5 below

# 5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def is_palindrome(n):
    if len(n) == 0 or len(n) == 1:
        return True
    else:
      return n[0] == n[-1] and is_palindrome(n[1:-1])
     
print(is_palindrome('apple'))
print(is_palindrome('tacocat'))