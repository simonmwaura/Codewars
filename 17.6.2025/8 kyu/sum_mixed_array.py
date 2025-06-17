# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    total = 0
    for i in arr: total += int(i)
    return total
print(sum_mix([9, 3, '7', '3']))