# # 1. Write a Python program to sum all the items in a list.
# #     - The list should be generated using list comprehension
# #     - The size of the list should be from a user input
sum = 0
y = int(input("What is the size? "))
multiples = [2 * x for x in range(y)]

for multiple in multiples:
    sum = sum + multiple
print("The sum of the multiples is " +str(sum))

#2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`

my_list = ["man", "pop", "woman", "12211", "omo", "mum"]
count = 0
for x in my_list:
    if (len(x) >= 2 and x[0] == x[-1]):
        count += 1
print("The words in the category are " +str(count))

# 3. Write a Python program to remove duplicates from a list, given list
#     `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
Fruits = []
for fruit in fruits:
    if fruit not in Fruits:
        Fruits.append(fruit)
print(Fruits)

# #4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`

Colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Orange', 'Grey']
del Colors[0]
del Colors[4]
del Colors[5]
print(Colors)

#5. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

Square_numbers = [x * x for x in range(40) if x >= 1 and x <= 30]
print(Square_numbers)
    

    
        
