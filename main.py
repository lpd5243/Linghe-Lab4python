# Author: Linghe Du lpd5243@psu.edu
# Collaborator :
# Collaborator :
# Collaborator :
# Section : 4
# Breakout : 
def num_of_divisors(n):
  ans = 1
  x = 2
  while x * x <= n:
    u = 1
    while n % x == 0:
      u += 1
      n /= x
    ans *= u
    x += 1
  return ans * (1 + (n > 1))
  return 0

"""
given a positive int n, return number of divisors for n between 1-n inclusive
You must use a while cond: style loop for this function.
"""

def num_of_primes(n):
  m = 0
  for p in range (n+1):
    if (num_of_divisors(p)==2):
      m +=1
  return m
  return 0
"""
given a positive int n, return number of primes that is <= n.
You must use num_of_divisors() function to help determine if a number is prime:
a number is a prime if its number of divisors is 2.
You must use a for... in range(...): style loop for this function.
"""

def sum_n(n):
  if n==0:
    return n
  else:
    return n+sum_n(n-1) 
  return 0
"""
given a non-negative int n, return the sum 0+1+2+...+n
You must use a while cond: style loop for this function.
"""


def print_n(s, n):
  for i in range(n):
    if n == 0: 
      return
    else:
      print(s)
  return   
"""
given a string s and a non-negative int n, print s n times
you must use for ... in range(...): style loop for this function
"""

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  print(f"{num} has {num_of_divisors(num)} divisors.")
  print(f"There are {num_of_primes(num)} primes <= {num}.")
  line = input("Enter a string: ")
  print_n(line, num)

if __name__ == "__main__":
  run()