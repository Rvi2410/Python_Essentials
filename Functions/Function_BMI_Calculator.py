"""
BMI : Body Mash Index

BMI = (Weight in KG) / height in meters square

"""

def bmi(weight, height):
    return weight / (height ** 2)


print(bmi(52.5, 1.65))  # (kg, meter)

##########################################

def bmi(weight, height):
    if  height < 1 or height > 2.5 \
            or weight < 20 or weight > 200:
        return None
    return weight / (height**2)

print(bmi(80,1.5))
print(bmi(210,3))

# Second, take a look at the way the backslash (\) symbol is used. If you use it in Python code and end a line with it,
# it will tell Python to continue the line of code in the next line of code.

##############################################
"""
Convert Imperial Unit to metric ones
1 lb = 0.45 kg
"""

# function for covert ld to kg

def lb_to_kg(lb):
    return lb * 0.45

print(lb_to_kg(10),"kg")

####################################
"""
convert ft to m, cm , inch
1 ft = 0.3048 m = 12 inch
1 ft = 30 cm
1 m = 100 cm
1 in = 2.54 cm
1 in = 0.0254 m
"""
# function for ft to inch to m

def ft_to_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_to_inch_to_m(1, 1))
print(ft_to_inch_to_m(10, 1))

###################################

# BMI for person 5'7" tall and weight of 176 lbs
def ft_to_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_to_inch_to_m(5,7))

def lb_to_kg(lb):
    return lb * 0.45

print(lb_to_kg(176))
weight= lb_to_kg(176)
print(weight)


def bmi(weight, height):
    if height < 1 or height > 2.5 \
            or weight < 20 or weight > 200:
        return None
    return weight / (height ** 2)

print(bmi(weight= lb_to_kg(176), height=ft_to_inch_to_m(5, 7)))
