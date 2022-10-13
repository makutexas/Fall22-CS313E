#  File: DNA.py

#  Description:

#  Student Name: Mark Chao

#  Student UT EID: mc72239

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 8/27/2022

#  Date Last Modified: 8/27/2022

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

import sys

def generate_subsequences(str):
  subsequence = []
  for i in range(0,len(str)):
    for j in range (i+1,len(str)+1):
      if (str[i:j] != "") and (len(str[i:j]) != 1):
        subsequence.append(str[i:j])
  subsequence.sort()
  return subsequence

def longest_subsequence (s1, s2):
  s1_subsequence = generate_subsequences(s1)
  s2_subsequence = generate_subsequences(s2)
  subsequence_list = []
  for s1_item in s1_subsequence:
    for s2_item in s2_subsequence:
      if (s1_item != s2_item):
        continue
      else:
        if (len(subsequence_list) == 0): #Case where list is currently empty
          subsequence_list.append(s1_item)
        elif (len(s1_item) == len(subsequence_list[0])): #Case where subsequence lengths are the same
          repeat = False
          for item in subsequence_list:
            if item == s1_item:
              repeat = True
              break
          if repeat == False:
            subsequence_list.append(s1_item)
        elif (len(s1_item) > len(subsequence_list[0])): #Case where subsequence length is longer than those currently stored
          subsequence_list = []
          subsequence_list.append(s1_item)
  subsequence_list.sort()
  return subsequence_list
  pass 

def main():
  # read the data
  data = sys.stdin.read()
  data_list = data.split("\n")  
  index = 1
  for i in range (0,int(data_list[0])):
    ss = longest_subsequence(data_list[index],data_list[index+1])
    if ss == []:
      print("No Common Sequence Found")
    else:
      for item in ss:
        print(item)
    print()
    index+=2

      

    
  # for each pair
  # call longest_subsequence
  # write out result(s)

  # insert blank line
  pass

if __name__ == "__main__":
  main()