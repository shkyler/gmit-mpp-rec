# 2019-12-06 - Patrick Moore - GMIT

# Q9 - Find the minimum element in an array of integers.
# You can carry some extrainformation through method arguments such as
# minimum value

def find_min(array):
# if the array only has one element in it return that element
  if len(array) == 1:
     return array[0]
# otherwise return the lower of the values between the current value and the rest of the array
  else:
     return min(array[0], find_min(array[1:]))

# test the function
test = [10,-50,60,70,80,90,-2]
print(find_min(test))