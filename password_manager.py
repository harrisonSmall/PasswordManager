import numpy as np
from cryptography.fernet import Fernet
import secrets
import sys

PASSWORD_LENGTH = 13
FILE_PATH = 'passwords.txt'


# Generate random password
def generate_password():
    return secrets.token_urlsafe(PASSWORD_LENGTH)


# Save file
def save_file(key, password):
    with open(FILE_PATH, 'a') as f:
        f.write(key + ': ' + password + '\n')
        f.close()
    print('Password created/ saved for', key + ': ', password)


# Read and print file
def read_file():
    with open(FILE_PATH, 'r') as f:
        print(f.read())


def action(choice):
    if choice == '1':
        read_file()
    elif choice == '2':
        key = input('What is the password for: ')
        save_file(key, generate_password())
    elif choice == '3':
        key = input('What is the password for: ')
        password = input('What is the password: ')
        save_file(key, password)
    elif choice == '4':
        exit()


# Reprompt
def reprompt():
    print('1. Read passwords \n'
          '2. Generate a new password \n'
          '3. Save an existing password \n'
          '4. Exit')
    choice = input('Choice: ')
    action(choice)
    reprompt()


def main(argv):
    print('Welcome to Password Manager')
    print('Choose an option (1, 2, 3): \n'
          '1. Read passwords \n'
          '2. Generate a new password \n'
          '3. Save an existing password \n'
          '4. Exit')
    choice = input('Choice: ')
    action(choice)
    reprompt()


if __name__ == "__main__":
    main(sys.argv[1:])
