# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square
import math


def find_next_square(sq):
    num1= math.sqrt(sq)
    if (int(num1) * int(num1)) == sq:
        return int((num1 + 1)*(num1 + 1))
    else  :
        return -1
























    # if num1 * num1 != int(sq):
    #     
    # elif num1 * num1 == int(sq):
    #     r
    
    
    # if type(num1 - 0.000000) == int:
    #    return (num1 + 1)*(num1 + 1)
    # else:
    #     
print(find_next_square(151))