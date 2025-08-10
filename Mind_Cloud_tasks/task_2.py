"""
first we will getting the K,M from the user and turn it into list using .split()
then we in for loop we will take the values of the rows from the user and turn it
into list, but we will reject first item because it is the number of elements and
append this list to a bigger list then we will use function from itertools library
this function take the bugger list and make list of tuples with all possible combination
"""

from itertools import product

k_m = [int(a) for a in input().split(" ")]
lists = []
m = k_m[1]
max_value = 0
for i in range(k_m[0]):
    data = [int(a) for a in input().split(" ")]
    lists.append(data[1:])
for combo in product(*lists):
    value = sum(x**2 for x in combo) % m #loop through each tuple and apply the function to it
    if value > max_value: #compare the new value with old value
        max_value = value

print(max_value)

