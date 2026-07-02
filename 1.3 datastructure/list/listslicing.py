list1 = [10, 20, 30, 40, 50]
# list[start:end] syntax is used to slice a list. 
# It returns a new list containing the elements from the start index up to, but not including, the end index.
print(list1[1:4])  # Output: [20, 30, 40]
#Start from beginning 
print(list1[:3])  # Output: [10, 20, 30]
#Till end
print(list1[2:])  # Output: [30, 40, 50]
#Slicing with step 
print(list1[::2])  # Output: [10, 30, 50]
#Reverse List
print(list1[::-1])  # Output: [50, 40, 30, 20, 10]
#loop through a list using index numbers
for i in range(len(list1)):
    print(i,list1[i])