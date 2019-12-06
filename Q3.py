# 2019-12-06 - Patrick Moore - GMIT

def odds(array):
    returnArray = []
    if len(array) == 1:
        if (returnArray[0]%2 == 0):
            returnArray.append(returnArray[0])
    else:
        odds(array[1:])
    return returnArray  