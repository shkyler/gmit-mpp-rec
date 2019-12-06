# 2019-12-06 - Patrick Moore - GMIT

# Q8 - Print an array
# Given an array of integers prints all the elements one per line.  
# This is a little bit different as there is no need for a ’return’ statement 
# just to print and recurse.

def print_array(array):
  # if the lenght of the array is not 0 print the first value and call the function
  # on the rest of the array
  if len(array) != 0:
    print(array[0])
    print_array(array[1:])

# Define a list of numbers to test
a = [1,2,3,4,5,6,7,10,10,10]
# Print the values in the array
print_array(a)    