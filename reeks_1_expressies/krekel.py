invoer = int(input())

temperatuur_fahrenheit = 50 + (invoer - 40) / 4
temperatuur_Celsius = 10 + (invoer - 40) / 7

if invoer < 0:
    print('geen geldig getal')
else:
    print(f'temperatuur (Fahrenheit): {temperatuur_fahrenheit}')
    print(f'temperatuur (Celsius): {temperatuur_Celsius}')