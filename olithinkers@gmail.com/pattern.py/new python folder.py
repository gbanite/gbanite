# Define the number of lines for the pattern
num_lines = 9

# Generate the pattern
for i in range(1, num_lines + 1):
    if i <= (num_lines // 2) + 1:
        print('*' * i)
    else:
        print('*' * (num_lines - i + 1))
