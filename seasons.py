# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

# Ex: If the input is:

# April
# 11
# the output is:

# Spring
# In addition, check if the string and int are valid (an actual month and day).

# Ex: If the input is:

# Blue
# 65
# the output is:

# Invalid 
# The dates for each season in the northern hemisphere are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19


input_month = input()
input_day = int(input())

months= ('January', 'February','March', 'April' , 'May' , 'June' , 'July' , 
'August' , 'September' , "October" , "November" , "December")

if not(input_month in months):
    print("Invalid")

elif input_month == 'March':
    if not(1<=input_day<=31):
        print ("Invalid")
    elif input_day<=19:
        print("Winter")
    else:
        print ("Spring")
elif input_month == 'April' :
    if not(1<=input_day<=30):
        print("Invalid")
    else:
        print("Spring")
elif input_month == 'May':
    if not(1<=input_day<=31):
        print("Invalid")
    else:
        print("Spring")
elif input_month == 'June':
    if not(1<=input_day<=30):
        print("Invalid")
    elif input_day<=20:
        print ("Spring")
    else:
        print("Summer")
elif input_month == 'July' or input_month == 'August':
    if not(1<=input_day<=31):
        print("Invalid")
    else: 
        print("Summer")
elif input_month == 'September':
    if not(1<=input_day<=30):
        print("Invalid")
    elif input_day<=21:
        print ("Summer")
    else:
        print ("Autumn")
elif input_month == "October":
    if not(1<=input_day<=31):
        print("Invalid")
    else:
        print("Autumn")
elif input_month == "November":
    if not(1<=input_day<=30):
        print("Invalid")
    else:
        print ("Autumn")
elif input_month == "December":
    if not(1<=input_day<=31):
        print("Invalid")
    elif input_day <=20:
        print ("Autumn")
    else:
        print ("Winter")
elif input_month == 'January':
    if not(1<=input_day<=31):
        print("Invalid")
    else:
        print("Winter")
elif input_month == "February":
    if not(1<=input_day<=29):
        print("Invalid")
    else:
        print ("Winter")