# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

# If they are, change the array value to a string of that vowel.

# input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.
# a = 97
# e = 101
# i = 105
# o = 111
# u = 117

def is_vow(inp):
    new_list = []
    for i in range(len(inp)):  
        if inp[i] == 97:new_list.append("a")
        elif inp[i] == 101:new_list.append("e")
        elif inp[i] == 105:new_list.append("i")
        elif inp[i] == 111:new_list.append("o")
        elif inp[i] == 117:new_list.append("u")
        elif inp[i] != 97 or inp[i] != 101 or inp[i] != 105 or inp[i] != 111 or inp[i] != 117:
            new_list.append(inp[i])
    return new_list
        
        

print(is_vow([100,100,116,105,117,121]))