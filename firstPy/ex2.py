# Programming exercise of Python Programming, Udacity.com
#LESSION 2


def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


volume = cylinder_volume(10, 3)
print(volume)

#this will calculate the week
def readable_timeline(days):
    weeks = days // 7
    remainder = days % 7
    return "{} weeks and {} days." .format(weeks, remainder)
print(readable_timeline(15))


#this will calculate months
def year_timeline(days):
    month = days // 30
    day_calculator = days % 30
    return "{}month(s) and {}day(s)" .format(month, day_calculator)
print(year_timeline(121))


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, kushal Atreya
"""
print(snake_string * how_many_snakes)

phone_balance = 7
bank_balance = 180

