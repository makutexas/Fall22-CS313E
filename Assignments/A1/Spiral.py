#  File: Spiral.py

#  Description: Spiral.py creates a spiral pattern of numbers, and given some integers, will find the sum of the numbers around that integer

#  Student Name: Mark Chao

#  Student UT EID: mc72239

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 8/30/2022

#  Date Last Modified: 8/30/2022

import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def print_spiral(spiral):
    for i in range (len(spiral)):
        print(spiral[i])

def create_spiral(n):
    #Initialize numbers
    if (n % 2 == 0):
        n += 1
    number = 1
    step = 1

    #Initialize list
    spiral = []
    for i in range (n):
        spiral.append([""] * n)

    #Initalize pointer, origin is 0,0
    row = int((n-1)/2)
    col = int((n-1)/2) 

    spiral[row][col] = 1

    #Fills all but the last row
    for recurrences in range (0,int((n-1)/2)):
        for i in range (0,step):
            col += 1
            number += 1
            spiral[row][col] = number
        for j in range (0,step):
            row += 1
            number += 1
            spiral[row][col] = number
        step += 1
        for i in range (0,step):
            col -= 1
            number += 1
            spiral[row][col] = number
        for j in range (0,step):
            row -= 1
            number += 1
            spiral[row][col] = number
        step += 1
    
    #Fills the last row on top
    for i in range (0,step-1):
            col += 1
            number += 1
            spiral[row][col] = number
    
    return spiral
     
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    #Find the number and save the row and col
    numberFound = False
    for row in range(len(spiral)):
        for col in range(len(spiral[row])):
            if spiral[row][col] == n:
                origin_row = row-1
                origin_col = col-1
                numberFound = True
    
    #Find the numbers around it
    
    adjacent_num = []

    if numberFound:
        for i in range(3):
            if (origin_row + i < 0 or origin_row + i >= len(spiral[0])): #Good row coordinate
                continue
            for j in range(3):
                if (origin_col + j < 0 or origin_col + j >= len(spiral[0])): #Good col coordinate
                    continue
                if (spiral[origin_row + i][origin_col + j] != n):
                    adjacent_num.append(spiral[origin_row + i][origin_col + j])
    
    return sum(adjacent_num)


def main():
    data = sys.stdin.read()
    list_str = data.split("\n")
    list_int = [int(item) for item in list_str if item != ""]


    spiral = create_spiral(list_int[0])

    for i in range(1,len(list_int)):
        print(sum_adjacent_numbers(spiral,list_int[i]))

# read the input file

# create the spiral

# add the adjacent numbers

# print the result

if __name__ == "__main__":
    main()
    pass