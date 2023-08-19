# (1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)

# Ex:

# Enter a sentence or phrase:
# The only thing we have to fear is fear itself.

# You entered: The only thing we have to fear is fear itself.
# (2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)

# (3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)

# (4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)

# Ex:

# Enter a sentence or phrase: 
# The only thing we have to fear is fear itself.

# You entered: The only thing we have to fear is fear itself.

# Number of characters: 46
# String with no whitespace: Theonlythingwehavetofearisfearitself.

def get_num_of_characters(inputStr):
    count = 0
    for i in range(len(inputStr)):
        count += 1
    return count

def output_without_whitespace(inputStr):
    inputStr = inputStr.replace(" ","")
    print("String with no whitespace: %s" %inputStr)

if __name__ == '__main__':
    inputStr = input("Enter a sentence or phrase:\n")
    print("")
    print("You entered: %s" %inputStr)
    print("")
    print("Number of characters: %s" %(get_num_of_characters(inputStr)))
    output_without_whitespace(inputStr)