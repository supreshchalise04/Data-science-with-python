#A list is a built-in Python data structure used to store multiple values in a single variable. 
# Lists are ordered, mutable (changeable), and allow duplicate values.
numbers = [10, 20, 30, 40]
names = ["Ram", "Sita", "Hari"]
mixed = [10, "Python", 5.5, True] 
#Lists use index numbers. to access an item in a list, you can use its index number. 
# The index starts at 0 for the first item, 1 for the second item, and so on. 
# You can also use negative indexing to access items from the end of the list,
# where -1 refers to the last item, -2 to the second last item, and so on.
print(numbers[0])  # Output: 10
print(names[1])    # Output: Sita
print(mixed[-1])   # Output: True
# Changing List Values (Mutable)
numbers[0]=15
print(numbers)  # Output: [15, 20, 30, 40] 
#Length of List -> Use len()
print(len(numbers))  # Output: 4
#adding two lists together
list1 = [1, 2, 3]
# adding two lists together
list = list1 + numbers  
print (list)
#Repeating Lists 
list1 = list1 * 2
print(list1)  # Output: [1, 2, 3, 1
# checking if an item exists in a list
print(20 in numbers)  # Output: True