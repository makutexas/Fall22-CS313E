#  File: TopoSort.py
#  Description: TopoSort.py sorts a graph using topological sort
#  Student Name: Mark Chao
#  Student UT EID: mc72239
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 11/26/2022
#  Date Last Modified: 11/26/2022

import sys

# Add Your functions here

def max_profit(money, num_houses, prices, increase):

    net_profit = [0] + [(prices[i]*(increase[i] * 0.01)) for i in range(num_houses)]
    prices = [0] + prices

    dp = [[0 for i in range(money+1)] for j in range(num_houses + 1)]

    for item in range(1, num_houses + 1):
        for weight in range(money+1):
            if prices[item] <= weight:
                dp[item][weight] = max(dp[item-1][weight], net_profit[item] + dp[item-1][weight-prices[item]])
            else:
                dp[item][weight] = dp[item-1][weight]
    
    # for i in range(num_houses + 1):
    #     print(dp[i])

    return dp[num_houses][money]

# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])

# Add your implementation here .... 
    result =  max_profit(money, num_houses, prices, increase)

# Add your functions and call them to generate the result. 

    print("%.2f" % result)

    

    
main()
