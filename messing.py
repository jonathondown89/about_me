name = "Jonathon Down"
age = 35
height = 74 #inches
weight = 180 #pounds
weight_in_kilo = weight * 0.453592 #lbs into kilo (1)
height_in_cm = height * 2.54 #inches into cm (1)
meter = height / 39.3701 #inches in meter (1)
height_in_meters = height_in_cm / 100 #cm into meter (100)



print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")

total = age + height + weight
print("He weighs", weight, "in lbs, which is", round(weight_in_kilo), "in Kilo")
print("His is", height, "in inches, which is", round(height_in_cm), "in CM")
print(height_in_cm , "Centimeters is", meter, "Meters")
print("Or", height_in_meters, "Meters")


