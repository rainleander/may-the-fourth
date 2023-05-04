import random

# Generate a sequence of 10 random numbers between 1 and 10
sequence = [random.randint(1, 10) for _ in range(10)]

# Print the initial sequence
print(sequence) 

# Apply transformations using the Force (code)
for i, number in enumerate(sequence):
    if number % 2 == 0:
        # Multiply even numbers by 2
        sequence[i] = number * 2
    else:
        # Add 5 to odd numbers
        sequence[i] = number + 5

    # Replace any number greater than 10 with 1
    if sequence[i] > 10:
        sequence[i] = 1

# Print the final sequence
print(sequence)
