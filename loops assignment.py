# Loops Assignment
# 1. Print First 10 natural numbers using while loop.
counter = 1
while counter <= 10:
	print(counter)
	counter = counter + 1

#2. Calculate the sum of all numbers from 1 to a given number.
sum = 0
count = 1
num = int(input("What is your limit? "))
while count <= num:
	sum = sum + count
	count = count + 1
print("Sum is " +str(sum))

#3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...
counter2 = 1
num = int(input("What number's multiples do you need? "))
limit = int(input("How many multiples? "))
while counter2 <= limit:
	m = counter2 * num
	print(m)
	counter2 = counter2 + 1

# 4. Write a program to display only those numbers from a list that satisfy the following condition
#- The number must be divisible by five
#- If the number is greater than 150, then skip it and move to the next number
#- If the number is greater than 500, then stop the loop
# given `numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
	if number%5 == 0:
		if number > 150:
			continue
		elif number > 500:
			break
		print(number)

#5. Write a program to count the total number of digits in a number using a while loop. given number `4673453` 
count = 0
num = 4673453
while num > 0:
	count = count + 1
	num = num//10
print(count)

#6. Display numbers from -10 to -1 using while loop
	
num = -10
while(num <= -1):
    print(num)
    num += 1


