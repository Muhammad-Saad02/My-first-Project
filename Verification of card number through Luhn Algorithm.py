def verify_card_number(card_number):
    # Initialize the sum of odd digits (digits in odd positions from the right)
    sum_of_odd_digits = 0
    
    # Reverse the card number to make the index manipulation easier
    reversed_card_number = card_number[::-1]

    # Extract the odd-positioned digits from the original card number (not reversed)
    odd_digits = card_number[::2]

    # Calculate the sum of the odd digits
    for digits in odd_digits:
        sum_of_odd_digits += int(digits)

    # Initialize the sum of even digits (digits in even positions from the right)
    sum_of_even_digits = 0
    
    # Extract the even-positioned digits from the reversed card number
    even_digits = reversed_card_number[1::2]

    # Process each even-positioned digit
    for digits in even_digits:
        # Multiply the digit by 2
        number = int(digits) * 2
        
        # If the result is a two-digit number, sum its digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        # Add the processed even digit to the sum of even digits
        sum_of_even_digits += number

    # Calculate the total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    
    # Return whether the total sum modulo 10 is zero (indicating a valid card number)
    return total % 10 == 0

def main():
    card_number = '2223 0076 4872 6984'
    
    # Define a translation table to remove spaces and hyphens from the card number
    card_number_translation = str.maketrans({'-': '', ' ': ''})
    
    translated_card_number = card_number.translate(card_number_translation)
    print(translated_card_number)
    
    # Verify the card number using the Luhn algorithm
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')
main()
