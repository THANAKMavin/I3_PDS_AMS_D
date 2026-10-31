print("\nProblem4\n")
print("Part A")
#   Part A
# "7" or '7'  :     String
# int("7")    ->    int 7
# float("7")   ->    float 7.0

print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10 / 2))

#   Part B
print("Part B")
def safe_int(text):
    text = text.strip()                     #   .strip()  : Delete space
    if text.lstrip("-").isdigit():          #   .isdigit(): Check it is a number -> True else False (Ex: text="1a3"->false)
                                            #   .lstrip("-") : Don't delete "-"
        return int(text)
    try:                                    #   (try:) : Check condition error or not
        return int(float(text))             #   return value to float and convert to int
    except ValueError:                      #   if error -> None
        return None

for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))         #   repr()  ->  ''

#   Part C
print("\nPart C")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

number1 = safe_int(num1)
number2 = safe_int(num2)

if number1 is None or number2 is None:
    print("Invalid input! Please enter valid numbers.")
else:
    total = number1 + number2
    print("Sum =", total)