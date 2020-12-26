"""
Here I'm taking my pajamas on or off depending on the time of day and/or
if I'm sleepy or not.
"""
#Note to Self: When a specific condition occurs, a specific action takes place.

Time  = "Day"
Sleepy = False
Pajamas = "Unknown"
InBed = True
print(Pajamas)

# Function that checks if it's night time, if we're sleepy - then we put on pajamas.
if Time == "Night":
    Pajamas = "On"

elif Time == "Morning": #"elif" is short for "else if"
    Pajamas = "On"

else:
    Pajamas = "Off"
    print(Pajamas)