'''
Name:
Date: 10/24/24
Description: For loops
'''
# this prints 0, 1, 2, 3, 4 each on their own line
#the numbre in range(stop) is how many nums are printed
# starts at 0 and ends at stop
for i in range(5):
    print(i,)

for i in range(5):
    print(i,end=",")

# For loop style 2 - for i in range(start, stop)
#this prints start, start+1, .... , stop-1
# loop runs stop start number of times
for num in range(2,6):
    print("*"*num)

for num in range(2,6):
    print(num,end=" ")
print()
print(f"----")
print(f"x | x^2")
for num_to_square in range(1,6):
    print(f"{num_to_square} | {num_to_square**2}")
print(f"---------")

# for loop style 3 - for i in range(start, stop, step
#this prints start, start+1 ...., stop-1 but counts by step
#loop runs ceiling((stop-start)/step) times
# ceiling means round up to nearest int
for number in range(10,40,4):
    print(number, end= " ")

#want: start at 12, count by 7s up to but not past 93
for number in range(12,93,7):
    print(number, end= " ")

# print the sum of the numbers 0 through n
user_num = int(input("Give me a number:"))
sum = 0 #initialize our sum to 0
for num in range(1,user_num+1):
    sum = sum + num
print(f"The sum is {sum}")

#1 ask the user for 5 numbers (use 5 variables and a loop)
num1 = int(input("Give me a number: "))
num2 = int(input("Give me a number: "))
num3 = int(input("Give me a number: "))
num4 = int(input("Give me a number: "))
num5 = int(input("Give me a number: "))


# find the average of those numbers (use a loop)
num6 = (num1 + num2 + num3 + num4 + num5)
average = num6/5
# print "The average of your numbers is ----"

print(average)
user_sum = 0
for i in range(5):
    user_num = int(input("Enter a number:"))
    user_sum = user_sum + user_num #updates user_sum with user_num values
average = user_sum/5
print(f"The average of your numbers is {average}")