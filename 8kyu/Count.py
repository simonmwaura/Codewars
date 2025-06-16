# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]

#  """
#     Return a sequence of numbers counting by `x` `n` times.
#     """

def count_by(x, n):
    count_list = []
    for item in range(n):
       count_list.append( x * (item + 1))
    return count_list

print(count_by(2,5))
    