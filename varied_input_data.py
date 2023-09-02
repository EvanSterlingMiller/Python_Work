# Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

# Ex: If the input is:

# 15 20 0 5
# the output is:

# 10 20

user_input = input()

tokens = user_input.split() 

nums = []                    
for token in tokens:         
    nums.append(int(token))
avg = sum(nums) / len(nums) 
print(int(avg), max(nums))   