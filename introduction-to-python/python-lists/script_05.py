# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[areas.index("kitchen")+1] + areas[areas.index("bedroom")+1]

# Print the variable eat_sleep_area
print(eat_sleep_area)
