def binary_search (list, n):
  #Generate sorted list
  binary_list = list

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
  return index

print(binary_search([0,1,2,3,4,5],))