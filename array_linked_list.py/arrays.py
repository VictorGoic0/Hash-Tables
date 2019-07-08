

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * self.capacity


# Double the size of the given array
def resize_array(array):
    new_capacity = array.capacity * 2
    new_elements = [None] * new_capacity

    for i in range(array.size):
        new_elements[i] = array.elements[i]

    array.capacity = new_capacity
    array.elements = new_elements


# Return an element of a given array at a given index
def array_read(array, index):
    if index < 0 or index >= array.size:
        print("Error out of bounds")
        return None
    else:
        return array[index]


# Insert an element in a given array at a given index
def array_insert(array, value, index):
    # Throw an error if array is out of the current count
    if index > array.size:
        print("Error out of bounds")
        return None

    # Resize the array if the number of elements is over capacity
    if array.capacity == array.size:
        resize_array(array)

    # Move the elements to create a space at 'index'
    # Think about where to start!
    for i in range(array.size, index, -1):
        if i > index:
            array.elements[i] = array.elements[i-1]
    array.elements[index] = value
    array.size += 1

# Add an element to the end of the given array
def array_append(array, value):
    array_insert(array, value, array.size)


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(array, value):
    removed = False
    for i in range(array.size):
        if removed:
            array.elements[i-1] = array.elements[i]
        elif array.elements[i] == value:
            removed = True
    if removed:
        array.size -= 1
        array.elements[array.size] = None
    else:
        print(f"Error, {value} not found")



# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop(array, index):
    if index >= array.size:
        print("Out of range")
        return None
    else:
        value = array.elements[index]
        for i in range(index, array.size-1):
            array.elements[i] = array.elements[i+1]
        array.size -= 1
        array.elements[array.size] = None
        return value


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.size):
        string += str(array.elements[i])
        if i < array.size - 1:
            string += ", "

    string += "]"
    print(string)


# Testing
arr = array(1)

array_insert(arr, "STRING1", 0)
array_print(arr)
array_pop(arr, 0)
array_print(arr)
array_insert(arr, "STRING1", 0)
array_append(arr, "STRING4")
array_insert(arr, "STRING2", 1)
array_insert(arr, "STRING3", 2)
array_print(arr)