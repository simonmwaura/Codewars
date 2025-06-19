# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    odd_array =[]
    for item in range(len(source_array)):
        if source_array[item] %2 != 0 :odd_array.append(source_array[item])
    odd_array.sort()
    odd_index = 0
    new_array = []
    for item in source_array:
        if item % 2 != 0: 
            new_array.append(odd_array[odd_index])
            odd_index += 1
        else : new_array.append(item)
    return new_array
                

print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))