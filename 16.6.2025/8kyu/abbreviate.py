# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name):
    new_list = name.split(' ')
    abbrev_list= []
    for i in new_list :
        new_value = i[0]
        abbrev_list.append(new_value)
    abbrev_string = " ".join(abbrev_list)
    return f"{abbrev_string[0].capitalize()}.{abbrev_string[len(abbrev_list)].capitalize()}"
print(abbrev_name("patrick feenan"))
