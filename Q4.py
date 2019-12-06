# 2019-12-06 - Patrick Moore - GMIT

# Q4 - Remove all even numbers
# Given an array of numbers return an array with all the even numbers removed.

def rem_evens(array):  
    # if the list is empty return an empty list - this will act as the base case
    if not array:
        return []
    # if the element at position is odd, return an array with this element in it and then check the remove the evens from the rest of the array 
    if array[0] % 2 == 1:
        return [array[0]] + rem_evens(array[1:])
    # if its not odd - check the next element in the array    
    return rem_evens(array[1:])


 # Define a list of numbers to test
a = [1,2,3,4,5,6,7,8,9,10]
# Print the sum of the array
print(rem_evens(a)) 