import re

row_column = [int(i) for i in input().split(" ")]
matrix = []
code = ""

for i in range(row_column[0]):
    matrix.append(list(input()))  # Store the values of the row as a list inside a bigger list
    while len(matrix[i]) != row_column[1]:
        matrix[i].append(" ")  # If the user entered fewer values than required in the row, fill the rest with spaces

for i in range(row_column[1]):
    for j in range(len(matrix)):
        code += matrix[j][i]

# This function performs a replace operation I found it after doing some research
# it takes (pattern, replacement, string), (?<=\w)[^A-Za-z0-9]+(?=\w) determine the
# range of work after the first character and before the last character
decoded = re.sub(r'(?<=\w)[^A-Za-z0-9]+(?=\w)', ' ', code)
print(decoded)
