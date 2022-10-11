#  File: Cipher.py

#  Description: Cipher.py encrypts and decrypts strings according to a rotated table method

#  Student Name: Mark Chao

#  Student UT EID: mc72239

#  Partner Name: Benjamin Ton-That

#  Partner UT EID:bbt426

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 9/4/2022

#  Date Last Modified: 9/10/2022

import math
import sys

def blankTwoDList(n):
  #Initialize list
  twod_list = []
  for i in range (n):
      twod_list.append([""] * n)
  return twod_list

def fillTable(strng, decrypt = False):
  dimension = math.ceil(math.sqrt(len(strng)))
  table = blankTwoDList(dimension)
  index = 0

  # Adds astericks to the table to make the encrypted message
  # the appropriate size so that it's read correctly
  if (decrypt == True): 
    count = 0
    for col in range(dimension):
      for row in range(dimension - 1, -1, -1):
        if count < ((dimension ** 2) - len(strng)):
          table[row][col] = "*"
          count += 1

  #Fill row + col with string letters, otherwise *
  for row in range(dimension):
    for col in range(dimension):
      if (index < len(strng)) and (table[row][col] != "*"):
        table[row][col] = strng[index]
        index+=1
      else:
        table[row][col] = "*"
  return table

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns  an encrypted string 
def encrypt (strng):
  en_str = ""
  unen_table = fillTable(strng)
  # Read through table to encrypt the string
  for col in range(0, len(unen_table)):
    for row in range((len(unen_table)-1),-1,-1):
      if (unen_table[row][col] != "*"):
        en_str = en_str + unen_table[row][col]

  return en_str
      

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt (strng):
    decry_str = ""
    encry_table = fillTable(strng, True)
    for col in range ((len(encry_table)-1),-1,-1):
      for row in range(len(encry_table)):
        if (encry_table[row][col] != "*"):
          decry_str = decry_str + encry_table[row][col]
    return decry_str

def main():
  # read the strings P and Q from standard input
  data = sys.stdin.read()
  data_str = data.split("\n")
  P = data_str[0]
  Q = data_str[1]         
  # encrypt the string P
  print(encrypt(P))
  # decrypt the string Q
  print(decrypt(Q))
  # print the encrypted string of P
  # and the dkecrypted string of Q
  pass

if __name__ == "__main__":
  main()
  