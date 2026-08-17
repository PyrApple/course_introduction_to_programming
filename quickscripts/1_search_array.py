# %%

# import
import random

# init locals
num_elements = 10
max_value = 100
min_value = max_value + 1
min_id = -1

# generate list of random numbers
numbers = [random.randint(1, max_value) for x in range(num_elements)]

# loop over elements
for i_number in range(0, len(numbers)):

    # get current number
    x = numbers[i_number]

    # new smallest challenger
    if( x < min_value ):

        # update locals
        min_value = x
        min_id = i_number

# log
print(numbers)
print(f"smallest {min_value} at index {min_id}")

# %%
# implementation with built in functions

# get min value and id
min_value = min(numbers)
min_index = numbers.index(min_value)

# log
print(f"smallest {min_value} at index {min_id}")