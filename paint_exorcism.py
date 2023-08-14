# As a young entrepreneur, you decide to start a house renovation business that combines two essential renovation tasks: house painting and exorcisms. Your task is to write a function that will compute the cost of painting and exorcism for your customers.

# For every 200 square feet, one gallon of paint and 10 hours of labor are required. Your company charges $40.00 per hour for labor and $100 per exorcism. Write a program that asks the user for the number of square feet to be painted, the price per gallon of paint, and the number of evil spirits that need to be exorcised. Then write a function that

# takes in these values from the user, (we give you code for this)
# calculates the number of gallons of paint required, the hours of labor required, the cost of paint, the labor charges, the exorcism charges, and the total cost of the job
# returns these 6 items (in order defined above) in a tuple (see 3.10 Multiple function outputs). Your program must then print out this tuple.



def house_renovation(exorcism):
    gallons_of_paint = sqft_painted / 200
    hours_labor = gallons_of_paint * 10
    cost_of_paint = ppg * gallons_of_paint
    labor_charges = hours_labor * 40
    exorcism_charges = demons * 100
    total = labor_charges + exorcism_charges + cost_of_paint
    cost = print(f"({gallons_of_paint}, {hours_labor}, {cost_of_paint}, {labor_charges}, {exorcism_charges}, {total})")
    return cost
# ask for input
sqft_painted=float(input("How many sqft is required to be painted?\n"))
ppg=float(input("What is the paint price per gallon?\n"))
demons=float(input("How many demons need to be exorcised?\n"))

house_renovation(exorcism)