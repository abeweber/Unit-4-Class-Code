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
j = width-height
print(f"The integers from {height} to {width} are:")
for i in range(j):
    height = height + 1
    print(height, end=" ")
    total = total + height
average = total/j
print()
print(f"The average is {average}")