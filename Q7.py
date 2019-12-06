# 2019-12-06 - Patrick Moore - GMIT

# Q3 - Sum of Digits
# Given a whole, number such as 23, return the sum of the digits in the number 
# i.e.  2 + 3 = 5.  
# For this would be useful to convert the number to a string
# then break it apart into digits.

def sum_num(number):
    # convert the number to a string
    str_num = str(number)
    # define the lenght of the string of 1 to be the base case
    if len(str_num) == 1:
        # when the lenght of the is 1 return the first and only digit -converted back to an integer
        return int(str_num[0])
        # if its longer than 1, add value of the first digit to the sum of the rest of the string
    else:
        return int(str_num[0]) + sum_num(str_num[1:])

# Print the sum of the integer
test = 125
print(sum_num(test))