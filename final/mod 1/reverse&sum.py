num = int(input("Enter a number: "))

# Reversing the number
reversed_num = int(str(num)[::-1])

# Finding the sum of digits
digit_sum = sum(int(digit) for digit in str(num))

print("Reversed number:", reversed_num)
print("Sum of digits:", digit_sum)
