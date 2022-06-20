import numpy as np
from cryptography.fernet import Fernet
import secrets
import sys

PASSWORD_LENGTH = 13


# Generate random password
def generate_password():
    return secrets.token_urlsafe(PASSWORD_LENGTH)


# Save file
def save_file():
    with open('passwords.txt', 'w') as f:
        f.write('facebook: ' + generate_password())


def main(argv):
    save_file()


if __name__ == "__main__":
    main(sys.argv[1:])
