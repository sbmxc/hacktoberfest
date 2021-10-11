def locate_minimum_value(array):
    """
    This function identifies the minimum value in an array and returns its index and value.
    
    Args:
    	:param list array: a list of integers
    
    Returns: tuple[int] 
    """
    minimum_value = float('inf')
    loc = -1
    for index, value in enumerate(array):
        if value < minimum_value:
            minimum_value = value
            loc = index
    return loc, minimum_value


def selection_sort(array):
    """
    This function sorts an input array in ascending order of integer values using the selection sort algorithm.
    
    Args:
    	:param list array: a list of integers
    
    Returns: list[int]
    """
    for i in range(len(array)):
        loc, minimum_value = locate_minimum_value(array[i:])
        array[i+loc] = array[i]
        array[i] = minimum_value
    return array

if __name__ == "__main__":
	print("Try out the Selection Sort Algorithm")
	array_length = int(input("Enter the length of the array you wish to sort: "))
	array = []
	for i in range(array_length):
		element = int(input(f"Enter element {i+1} of the array: "))
		array.append(element)
		
	print(selection_sort(array))