# Q1

def sum(array):
    # define the lenght of the array of 1 to be the base case
    if len(array) == 1:
        # when the lenght of the array is 1 return the value at index zero (the only value in the array)
        return array[0]
        # if its longer than 1, add the the value at index 0 to the sum of the rest of the list
    else:
        return array[0] + sum(array[1:])

# Define a list of numbers to test
a = [1,2,3,4,5,6,7,8,9,10]
# Print the sum of the array
print(sum(a))

