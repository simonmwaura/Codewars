# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

def get_middle(s):
    if len(s)%2 == 0:
        num_1 = (len(s) / 2 )- 1
        num_2 = (len(s) / 2)
        return f"{s[int(num_1)]}{s[int(num_2)]}"    
    elif len(s)%2 !=0:
        num_3 = (len(s)) / 2
        return s[int(num_3)]
    
print(get_middle("middle"))