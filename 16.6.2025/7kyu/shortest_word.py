# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def myFunc(e):
  return len(e)

def find_short(s):
    new_list = s.split(" ")
    new_list.sort(key=myFunc)
    return len(new_list[0])
 
print(find_short("bitcoin take over the world maybe who knows perhaps"))