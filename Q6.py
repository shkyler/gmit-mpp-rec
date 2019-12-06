# 2019-12-06 - Patrick Moore - GMIT

# Q6 - Find index in array for item.  
# Given an array, and an element to search for return the index of the element 
# in the array or -1 if the element is not present in the array.


def index(array, value_to_check):
    # if the entered value is not in the list return -1
    if value_to_check not in array:
      return -1
    # if the item is the first item in the list, return 0
    if array[0] == value_to_check:
      return 0  
    # otherwise return 1 plus the value of the array on the next slide of the array  
    else:
      return 1 + index(array[1:], value_to_check)


a= [1,1,2,3,4,5]
print(index(a,3))    