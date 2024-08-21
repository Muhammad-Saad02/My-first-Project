def verify_card_number(card_number):
    sum_of_odd_digits = 0 
    reversed_card_number = card_number[::-1]
    odd_digits = card_number[::2] 
    for digits in odd_digits:
        sum_of_odd_digits += int(digits) 

    sum_of_even_digits = 0
    even_digits = reversed_card_number[1::2] 
    for digits in even_digits:
        number = int(digits)*2
    if number >= 10:
        number = (number//10) + (number % 10) 
    sum_of_even_digits += number 

    total = sum_of_odd_digits + sum_of_even_digits 
    print(total) 
    return total % 10

def main():
    card_number = '2223 0076 4872 6984'
    card_number_translation = str.maketrans({'-':'' , ' ':''}) 
    translated_card_number = card_number.translate(card_number_translation)
    print(translated_card_number) 
 
    if verify_card_number(translated_card_number):
        print('VALID!') 
    else:
        print('INVALID!')
main()
