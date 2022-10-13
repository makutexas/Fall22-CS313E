#  File: Josephus.py

#  Description: Josephus.py returns the ordre at which the soldiers are eliminated given starting conditions

#  Student Name: Mark Chao

#  Student UT EID: mc72239

#  Partner Name: Ben Ton-That

#  Partner UT EID: bbt426

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 10/7/2022

#  Date Last Modified: 10/9/2022

import sys

class Link(object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.last_link = None
  
  # Insert an element (value) in the list
  def insert ( self, data ):
    newLink = Link(data)
    if self.last_link == None: #Case of no links
      newLink.next = None
      self.last_link = newLink
    elif self.last_link.next == None: #Case of 1 link
      newLink.next = self.last_link
      self.last_link.next = newLink
      self.last_link = newLink
    else: #Adding subsequent links
      newLink.next = self.last_link.next
      self.last_link.next = newLink
      self.last_link = newLink

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    if self.last_link == None: #Empty list
      return None
    
    if self.last_link.next == None: #Case with 1 link
      if (self.last_link.data == data):
        return self.last_link
      else:
        return None
    
    currentLink = self.last_link #Case with 2+ links

    while currentLink.data != data: 
      currentLink = currentLink.next
      if currentLink == self.last_link: #If it loops back around and finds nothing
        return None
    
    return currentLink

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):

    foundLink = self.find(data)

    if foundLink == None: #If the link is not found
      return None
    elif (foundLink.next == None): #If the link is the only link AND data is found
      self.last_link = None
      return foundLink

    previousLink = self.last_link #2+ links in linked list
    
    while previousLink.next != foundLink: 
      previousLink = previousLink.next

    if foundLink == self.last_link: #Sets new self.last_link if that is the link deleted
      self.last_link = previousLink

    if foundLink.next != previousLink: 
      previousLink.next = foundLink.next #Pointers set
    else:
      previousLink.next = None #If 1 item will be left in linked list, set .next to None

    return foundLink
    
  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    currentLink = self.last_link
    startLink = self.find(start)
    if startLink == None: 
      return None, None
    elif startLink.next == None: 
      return currentLink, None
    
    while currentLink != startLink: #Iterates the current link position to the starting point.
      currentLink = currentLink.next
      
    for i in range(n-1): #Iterates to first number to delete n times.
      currentLink = currentLink.next
    self.delete(currentLink.data) 
    return currentLink, currentLink.next

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    print_list = []
    pointer = self.last_link

    if pointer == None: #Empty list
      return str(print_list)

    if pointer.next == None: #If list is exactly 1
      print_list.append(pointer.data)
      return str(print_list)

    while pointer.next != self.last_link: #Append all but last link
      pointer = pointer.next
      print_list.append(pointer.data)
    
    pointer = pointer.next #Append last link
    print_list.append(pointer.data)

    return str(print_list)

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  soldiers = CircularList()
  for i in range (1, num_soldiers + 1):
    soldiers.insert(i)
  
  while True:
    deleted_link, start_pointer = soldiers.delete_after(start_count, elim_num)
    if start_pointer == None:
      print(deleted_link.data)
      break
    start_count = start_pointer.data
    print(deleted_link.data)

if __name__ == "__main__":
  main()