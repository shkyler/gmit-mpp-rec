# 2019-12-06 - Patrick Moore - GMIT

# - Replace a given character with ’*’
# Given  a  string,  and  a  character  to  replace, return a string where each 
# occurance of the character is replaced with ’*’

def starify(entry_string, char_to_change):
    # if the entered string is empty return and empty string (this is the base case)
    if entry_string == '':
        return ''
    # if the first item in the string is equal to the char we are going to change    
    if entry_string[0] == char_to_change:
        # return a star in the first position and then call the starify function on the rest of the entered string
        return '*' + starify(entry_string[1:], char_to_change)
    # if its not equal to the charachter to change return the string and call the funciton on the rest of the list    
    return entry_string[0] + starify(entry_string[1:], char_to_change)

# test the function
print(starify('I Love you!','o'))