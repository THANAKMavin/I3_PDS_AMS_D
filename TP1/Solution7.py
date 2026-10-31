print("\nProblem7")
# a Make 3 functions
def digit_sum(n):
    total = 0
    while n > 0:
        total +=  n % 10
        n = n // 10
    return total

def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

def is_palindrome(n):
    return n == reverse_number(n)

print("2026: digit sum=", digit_sum(2026), "| reverse=", reverse_number(2026), "| palindrome=", is_palindrome(2026))
print("12321: digit sum=", digit_sum(12321), "| reverse=", reverse_number(12321), "| palindrome=", is_palindrome(12321))
print("9875: digit sum=", digit_sum(9875), "| reverse=", reverse_number(9875), "| palindrome=", is_palindrome(9875))


# b Count how many palindrome there are from 10 to 999
count = 0
for n in range(10, 999):
    palindrome = is_palindrome(n)
    if palindrome:
        count+=1
print("Palindomes from 10 to 999:", count) 
print("")
