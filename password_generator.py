import string
import random
import os
import time
os.system('clear')

settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
}

PASSWORD_MIN_LENGTH = 4   #agar ba harf bozorg bashe yani ghasd taghir nadarim
PASSWORD_MAX_LENGTH = 30


def change_length_of_pass(option, default, pass_mi_length=PASSWORD_MIN_LENGTH, pass_max_length=PASSWORD_MAX_LENGTH):
    '''return int user input for length of password'''
    while True:
        user_input = input(f'pass {option} is {default} Enter length of pass(only number): ')
        
        if user_input == '':
            return default

        if user_input.isdigit():   #vaghty harf vared mikonim shart aval ke False mishe badi ro nmire
            password_int = int(user_input)
            if pass_mi_length <= password_int <= pass_max_length:
                return int(user_input)
            print(f'Enter length between {pass_mi_length}-{pass_max_length}')
        else:
            print(f'!wrong! pleas enter a num you enter a {type(user_input)}')
        print('Please try again')


def check_user_input(option, default):
    '''check user input in range (y,n,enter)'''
    while True:
        user_input = input(f'include {option}? (default is {default}) (y: yes , n: no): ')
        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'

        print('invaled input. Try again')


def get_setting_from_user(settings):
    '''Get setting and return changed item'''
    for option, default in settings.items():
        if option != 'length':
            user_choice = check_user_input(option, default)
            settings[option] = user_choice
        else:
            user_pass_length = change_length_of_pass(option, default)
            settings[option] = user_pass_length


def get_random_symbol():
    '''Return random symbol'''
    return random.choice('!@#$%^&*()_+±>.,<?/|}{[]:;')


def generate_random_char(choices):
    '''Generat a random char for creat a password'''
    choice = random.choice(choices)

    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    
    elif choice == 'lower':
        return random.choice(string.ascii_lowercase)
    
    elif choice == 'symbol':
        return get_random_symbol()
    
    elif choice == 'number':
        return random.choice('123456789')

    elif choice == 'space':
        return ' '


def password_generator(settings):
    '''Return a final password'''
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda key: settings[key] == True, ['upper', 'lower', 'symbol', 'number', 'space']))

    for i in range(password_length):
        final_password += generate_random_char(choices)

    return final_password


def ask_to_change_setting(settings):
    '''Ask user to change password or not'''
    while True:
        user_choice = input('do you like change default setting? ')
        if user_choice in ['y', 'n', '']:
            if user_choice in ['y', '']:
                print('-'*5, 'change setting', '-'*5, sep='')
                get_setting_from_user(settings)
            break
        print('please enter between (y , n , enter)')


def generate_another_password(settings):
    '''Ask a user to regenerat
    and return a True or False'''
    while True:
        print('-' * 20)
        print(f'Generated password: {password_generator(settings)}')
        while True:
            user_input = input('Do you want another password? (y:yes , n:no , enter:yes)')
            if user_input in ['y', 'n', '']:
                if user_input == 'n':
                    return
                break
            else:
                print('please enter between (y , n , enter)')
                print('please try againe')


def run():
    # get_setting_from_user(settings)
    # print('-' * 20)
    # print(f'Generated password: {password_generator(settings)}')
    print('arian')
    time.sleep(2)
    ask_to_change_setting(settings)
    generate_another_password(settings)


run()
