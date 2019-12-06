# 2019-12-06 - Patrick Moore - GMIT

# Q10 - Verify the parentheses 
# Given a string, return true if it is a 
# nesting of zero or morepairs of parenthesis, like “(())” or “((()))”.

def check_balanced(input_str, i=0, count=0):
    # if the length of the input string is the same as the index
    if i == len(input_str): 
      # check if the count is zero - return True if it is
      return count == 0
    # of count is less than zero return false  
    if count < 0: 
      return False
    # if the we have an open bracket at index i increment the index and count and check again  
    if input_str[i] == "(": 
      return  check_balanced(input_str, i + 1, count + 1)
    #  if the we have an open bracket at index i increment the index and decrement the count and check again  
    elif input_str[i] == ")": 
      return  check_balanced(input_str, i + 1, count - 1)
    # return the value of check_balance at the next index of the string  
    return check_balanced(input_str, i + 1, count)

print(check_balanced("()"))    