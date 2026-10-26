def celsius_to_fahrenheit(celsius, round_to = 1):
    #Local statement
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

print("Convert temperature from C to F:")
for i in range(0, 101, 20):         #range(start, stop, step)
    print(i, celsius_to_fahrenheit(i), "F")

print("")
print(celsius_to_fahrenheit(27), "F")

def fahrenheit_to_celsius(fahrenheit, round_to=1):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

print("Convert temperture trom F to C:")
