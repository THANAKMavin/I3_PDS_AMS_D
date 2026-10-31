print("\nProblem3\n")

def celsius_to_fahrenheit(celsius, round_to = 1):
    #Local statement
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit, round_to=1):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# (a) Use a for loop
print("\nConvert temperature from °C to °F:")
print("°C   |   °F")
print("-----+-----")
for i in range(0, 101, 20):         #range(start, stop, step)
    print(f"{i:4} | {celsius_to_fahrenheit(i):5}")

print("\n")
# (b) Convert temperature from °F to °C

print("98.6°F","\t=>", fahrenheit_to_celsius(98.6), "°C")

# (c) Convert temperature from °C to °F
print("37 °C", "\t=>", celsius_to_fahrenheit(37), "°F")

# (d) Call one function with round_to = 3
print(celsius_to_fahrenheit(20, round_to=3))