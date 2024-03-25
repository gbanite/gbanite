# Initialize variables to keep track of the sum and count of numbers entered
total = 0
count = 0

# Continuously ask the user to enter a number until they enter -1
while True:
    num = float(input("Enter a number (enter -1 to stop): "))
    if num == -1:
        break  # Break out of the loop if -1 is entered
    total += num
    count += 1

# Calculate the average of the numbers entered (excluding -1)
if count > 0:
    average = total / count
    print("Average of the numbers entered:", average)
else:
    print("No numbers entered.")
