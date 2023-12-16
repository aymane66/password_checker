print("------------------ Password Checker ------------------")


def has_upper_case(password):
    # Check if the password has at least one uppercase character
    for char in password:
        if char.isupper():
            return True
    return False


def has_lower_case(password):
    # Check if the password has at least one lowercase character
    for char in password:
        if char.islower():
            return True
    return False


def has_digits(password):
    # Check if the password has at least one digit
    for char in password:
        if char.isdigit():
            return True
    return False


def is_long(password):
    # Check if the password is longer than 9 characters
    return len(password) > 9


def has_special_characters(password):
    # Check if the password has at least one special character
    special_characters = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"
    for char in password:
        if char in special_characters:
            return True
    return False


def conditions(password):
    if len(password) == 0:
        print("Please insert a password! ")
    else:
        error_occurred = False

        if not has_upper_case(password):
            print("- Your password lacks uppercase characters.")
            error_occurred = True
        if not has_lower_case(password):
            print("- Your password lacks lowercase characters.")
            error_occurred = True
        if not has_digits(password):
            print("- Your password lacks digits.")
            error_occurred = True
        if not is_long(password):
            print("- Your password is too short.")
            error_occurred = True
        if not has_special_characters(password):
            print("- Your password lacks special characters.")
            error_occurred = True

        if not error_occurred:
            print("Your password is strong! ")


try:
    password = input("Insert a password (> 9 characters): ")
    conditions(password)
except ValueError:
    print("Error! ")