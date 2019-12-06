# 2019-12-06 - Patrick Moore - GMIT

# Q2 - Product of an array
# Given an array of numbers return it’s product (all the numbers multiplied together).

def prod(array):
    # define the lenght of the array of 1 to be the base case
    if len(array) == 1:
         # when the lenght of the array is 1 return the value at index zero (the only value in the array)
        return array[0]
        # if its longer than 1, multiply the the value at index 0 to the product of the rest of the list
    else:
        return array[0] * prod(array[1:])   

# Define a list of numbers to test
a = [1,2,3,4,5,6,7,8,9,10]
# Print the product of the array
print(prod(a))  