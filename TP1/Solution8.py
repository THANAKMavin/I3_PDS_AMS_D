print("\nProblem8\n")

# a
def describe(*numbers, decimals = 2, label = "Data"):
    if len(numbers) == 0:                   #len()  :  count the number
        print(label + ": No values")
        return None

    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers)/count

    print(f"{label}: n={count} min={minimum} max={maximum} mean={round(mean, decimals)}")

    return count, minimum, maximum, round(mean, decimals)

# b
def make_tag(text, **style):
    attribute = ""

    for key, value in style.items():
        attribute += f' {key}="{value}"'
        return f"<span{attribute}>{text}</span"
    
# c
square = lambda x: x ** 2
is_adult = lambda age: age >= 18

print(describe(12, 7, 30, 4))
print(describe(3.14159, 2.71828, decimals=3, label="Constants"))
print(describe())
print(make_tag("Hello", color="red", size=14))
print(square(9), is_adult(17), is_adult(21))