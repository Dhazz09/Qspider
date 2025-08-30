#  Digit Sum Calculator using While Loop


num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit = num % 10          
    digit_sum += digit        
    num = num // 10           

print(f" Sum of digits: {digit_sum}")