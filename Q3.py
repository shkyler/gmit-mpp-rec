# 2019-12-06 - Patrick Moore - GMIT

# Q3 - Remove all odd numbers
# Given an array of numbers return an array with all the odd numbers removed.

def rem_odds(array):  
    # if the list is empty return an empty list  
    if not array:
        return []
    # if the element at position is even, return an array with this element in it and then check the remove the odds from the rest of the array 
    if array[0] % 2 == 0:
        return [array[0]] + rem_odds(array[1:])
    # if its not even - check the next element in the array    
    return rem_odds(array[1:])


 # Define a list of numbers to test
a = [1,2,3,4,5,6,7,8,9,10]
# Print the evens from the array
print(rem_odds(a))  


