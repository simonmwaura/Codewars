# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    new_list = text.split(' ')
    reverse_list = []
    for i in range(len(new_list)):
        new_value = new_list[i][::-1]
        reverse_list.append(new_value)
    return " ".join(reverse_list)
    
   
print(reverse_words("This is an example!"))