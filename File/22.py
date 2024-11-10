# # Take input from the user for the number of rows
# n = int(input("Enter the number of rows: "))

# # Function to print the first column pattern (stars)
# def print_star_pattern(n):
#     for i in range(1, n+1):
#         print('*' * i)


# # Function to print the second column pattern (numbers increasing by rows)
# def print_increasing_number_pattern(n):
#     for i in range(1, n+1):
#         print(str(i) * i)


# # Function to print the third column pattern (numbers decreasing in rows)
# def print_decreasing_number_pattern(n):
#     for i in range(n, 0, -1):
#         print(str(n-i+1) * i)


# # Function to print the fourth column pattern (alphabet pattern)
# def print_alphabet_pattern(n):
#     for i in range(1, n+1):
#         print(''.join(chr(65 + j) for j in range(i)))


# # Print each pattern side by side
# print("\nPattern 1:")
# print_star_pattern(n)
# print("\nPattern 2:")
# print_increasing_number_pattern(n)
# print("\nPattern 3:")
# print_decreasing_number_pattern(n)
# print("\nPattern 4:")
# print_alphabet_pattern(n)




# ----------------------------------------------------------------

# Function to print the first column pattern (stars)
def print_star_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)


# Function to print the second column pattern (numbers increasing by rows)
def print_increasing_number_pattern(n):
    for i in range(1, n + 1):
        print(str(i) * i)


# Function to print the third column pattern (numbers decreasing in rows)
def print_decreasing_number_pattern(n):
    for i in range(n, 0, -1):
        print(str(n - i + 1) * i)


# Function to print the fourth column pattern (alphabet pattern)
def print_alphabet_pattern(n):
    for i in range(1, n + 1):
        print(''.join(chr(65 + j) for j in range(i)))


# Ask the user for the number of rows
n = int(input("Enter the number of rows for the patterns: "))

# Print each pattern one after the other
print("\nPattern 1 (Stars):")
print_star_pattern(n)
print("\nPattern 2 (Increasing Numbers):")
print_increasing_number_pattern(n)
print("\nPattern 3 (Decreasing Numbers):")
print_decreasing_number_pattern(n)
print("\nPattern 4 (Alphabets):")
print_alphabet_pattern(n)

