""" 
In python an array only stores the pointers to the values that are in the array
an array also only keeps track of the first element in the array since the items in an array are stored in
a contiguous location hence to access the items in an array we use the index system
"""

new_list = [1, 2, 3]

# accessing an item in an array => O(1)
new_list[2]

# searching for a value in an array => O(n)
for item in new_list:
    if item == 2:
        print("Item found")
        break

# inserting values in an array at any position=> O(n)
# appending -> inserting values at the end of an array=> O(1)
# deleting a value at any  specific place=> O(n)
# deleting an item at the end of the list=> O(1)

numbers = [54, 62, 93, 17, 77, 31, 44, 55, 20]

mid = len(numbers) // 2
first_half = numbers[:mid]
second_half = numbers[mid:]
print(f"First Half: {first_half}, Second Half: {second_half}")
