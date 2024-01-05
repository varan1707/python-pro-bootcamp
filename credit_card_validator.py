#Python Credit Card Validation program for Validating Credit Cards addded by users. The program uses the
# test-credit-card-validator file. However, you can enter any credit card number and check if the  number is correct
# or not

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Remove any e '-' or ' ' characters

card_number = input("Enter a credit card number: ")
card_number = card_number.replace('-','')
card_number = card_number[::-1]
#print(card_number)

# Add all the digits from left to right in the credit card number

for i in card_number[::2]:
    sum_odd_digits += int(i)

# Double every second digit from right to left in the credit card number and if the number is a two-digit number we add
# the digits and get a single digit number

for i in card_number[1::2]:
    i = int(i * 2);
    if i >= 10:
        sum_even_digits += (i % 10) + 1
    else:
        sum_even_digits += i


# sum the totals for the odd and the even digits from right to left in the credit card number
total = sum_odd_digits + sum_even_digits

# check if the credit card is valid as at this stage the number has to be checeked if the number is valid.
if total % 10 == 0:
    print("Congrats! It's a Valid Credit Card Number");
else:
    print("Sorry! The Credit Card Number is Invalid");


