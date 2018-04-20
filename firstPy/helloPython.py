# Programming exercise of Python Programming, Udacity.com
#LESSION 1

print("Hello World!")
# This is the comments

name = "Kushal"
print(name)
print("\n") # new line

print(3//2) # double // will round off the value

manila_pop = 1780148
manila_area = 16.56
manila_pop_density = manila_pop//manila_area # this will show the round figure, put / to get exact value.
print("Population density is " , manila_pop_density)

manila_pop = manila_pop + 1675 - 250
print("Exact Population is " , manila_pop) # This will update the value

manila_pop += 1675 # increase the value of manila_pop by 1675
manila_pop -= 250 # decrease the value of manila_pop by 250
manila_pop *= 0.9 # decrease the value of manila_pop by 10%
manila_pop /=  2 # approximate the female population of Manila
print("Female Population is " , manila_pop)

salary, savings = 2200, 25000
print(salary)
print("\n")

# lession 1.7
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area
# Write code that prints True if San Francisco is denser than Rio, and False otherwise

print(san_francisco_pop_density > rio_de_janeiro_pop_density)

# concatenate strings.

instructor_1 = "Philip"
instructor_2 = "Charlie"
print(instructor_1 + instructor_2)
print("\n")

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"
full_name = (given_name +" "+ middle_names +" "+ family_name)
print(full_name)
name_length = len(full_name)
print(name_length)
print("\n")

"""
int (integer, for whole numbers)
float (for numbers that aren’t necessarily whole numbers)
bool (boolean, for True and False values)
str (string, for text)

"""
print(type(633))
print(type("633"))
print(type(633.0))
print("\n")

print("hippo" *12)

mon_sales = float("121")
tues_sales = float("105")
wed_sales = float("110")
thurs_sales = float("98")
fri_sales = float("95")

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write several lines of code before the print statement.
total_sale = (mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales   )
print(total_sale)
total_sales = "This week's total sales: " + str(total_sale)
print(total_sales)