while True:
    height = int(input("Box height (3-9): "))
    width = int(input("Box width (must be greater than height and less than 20): "))
    if height < 3 or height > 9:
        print("Height must be between 3 and 9")
        continue
    elif width < height or width > 20:
        print("Width must be greater than height and less than 20")
        continue
    if 3 <= height <= 9 and height < width <= 20:
        break
    
total = 0
height2 = height
j = width-height
print(f"The integers from {height} to {width} are:")
for i in range(j):
    height2 = height2 + 1
    print(height2, end=" ")
    total = total + height2
average = total/j
print()
print(f"The average is {average}")

for i in range(width):
    print("*", end="")
print()
width2 = width-2
space = (" "*width2)
for i in range(height-2):
    print(f"*{space}*")
for i in range(width):
    print("*", end="")

print()
print()
first_row = "**"
factor = 1
for i in range(height):
    print(first_row*factor)
    factor = factor + 1
 