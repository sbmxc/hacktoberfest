# function to implement linear search algorithm in python
# takes a number list and search key
# returns the index of the key in list
def linear_search(array, key):

  end = len(array)

  for index in range(end):

    if array[index] == key:
      return index
  
  return -1   # if key wasn't found


# main code
array = [9, 2, 4, 3, 6, 5, 7, 8, 1]
key = 8

print(f'initial array: {array}')

print(f'search element: {key}')
index = linear_search(array, key)

if (index < 0):
  print(f'{key} not found in array')

else:
  print(f'{key} found at index {index}')
