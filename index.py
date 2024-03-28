def luhn(number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    # Reverse the digits of the number
    reversed_digits = digits_of(number)[::-1]
    sum_of_digits = 0

    # Iterate over each digit in the reversed list
    for i, digit in enumerate(reversed_digits):
        # Check if the position is odd (every second digit in original number)
        if i % 2 != 0: # Double every second digit
            doubled = digit * 2
            if doubled > 9: # Sum digits if value is more than 9
                doubled = doubled // 10 + doubled % 10
            # Add modified digit to sum
            sum_of_digits += doubled
        else:
            sum_of_digits += digit # Add other digits as they are
    
    # return total sum of digits
    return sum_of_digits

# Testing function
number = 23544
sum_result = luhn(number)
print(f"Sum following Luhn's doubling rules: {sum_result}")