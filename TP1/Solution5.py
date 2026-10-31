print("\nProblem5\n")
# a Test the function and print the result
def letter_grade(score):

    if score > 100 or score < 0:
        return "is invalid score."
    else:
        if score >= 97:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

for sc in [99, 90, 85.5, 5, 72, 60, 59.9, 9, -5, 101]:
    print(sc, "->", letter_grade(sc))

print("")

# b Answer the question
print("Question:")
print("Why must the test for A+ come before the test for A? What happend if swap them?")
print("Answer:")
print("#The test for A+ come before the test for A because the grade A+ need the score bigger than grade A, so we must write the condition A+ before the A to get logic result.")
print("#If we swap them, we can not get the logic result. When we talk A before A+, the user input the score more then 90 or more then 97, the score will check by the first condition, so it always true in the first condition and end the code(no continue to the next condition).")
print("")