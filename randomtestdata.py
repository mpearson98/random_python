import random

# Generate 200 random numbers
numbers = [random.randint(1, 1000) for _ in range(200)]

# Convert the list of numbers to a string, separated by commas
numbers_str = ','.join(map(str, numbers))

# Write the string to a file
with open('data.csv', 'w') as f:
    f.write(numbers_str)