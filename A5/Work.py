#  File: Work.py

#  Description: Work.py determines the amount of initial lines of code for Chris to write n lines

#  Student Name: Mark Chao

#  Student UT EID: mc72239

#  Partner Name: 

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 10/1/2022

#  Date Last Modified: 10/3/2022

import sys
import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series

def sum_series (v, k):
  total = 0
  p = 0
  while (v // (k ** p)) > 0:
    total += (v // (k ** p))
    p += 1
  return total

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  lines = 0
  while sum_series(lines,k) < n:
    lines += 1
  return lines

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  #Generate sorted list
  binary_list = [sum_series(i,k) for i in range(n)]
  print(binary_list)

  top = len(binary_list)
  top = len(binary_list) - 1
  bot = 0
  index = -1
  while bot <= top:
    mid = (top + bot) // 2
    if n > binary_list[mid]:
      bot = mid + 1
    else: 
      index = mid
      top = mid - 1
  if index == -1:
    return len(binary_list)
  return index

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
