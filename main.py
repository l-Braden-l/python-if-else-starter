#Braden Leach
#Oct 1 2024
#If else statements



#task 1 
#i read it
#task 2 
    #is green
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points for shooting the alien')
else:
    print('You earned  points for shooting the alien')
    # is not green 
alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points for shooting the alien')
else:
    print('You earned  points for shooting the alien')
#task 3 
name = input('write your first name:\n')
if len(name) <= 5:
    print('your name is too short')
else:
    print('You have a long name')
#task 4 
vowels = ['a','e','i','o','u']
letter = input('Please enter a letter of the alphabet:\n').lower()
if letter in vowels:
    print('your letter is a vowel')
else:
    print('your letter is a consonant')
#task 5 
number_2 = float(input('enter a number again:\n'))
number_1 = float(input('enter a number:\n'))

if number_1 % number_2 == 0:
    print('the first number is divisible by the second number!')
else:
    print('the first number is not divisible by the second number')