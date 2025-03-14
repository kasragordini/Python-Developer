def validate_name(name):
    """ Checks that the name is greater than two characters and is a string data type.

 Args:
    name (str): The inputted name from the user.

 Returns:
    bool: True if the name passes the check, False otherwise.
    """
    if type(name) != str:
        return False   
    elif len(name) <= 2: 
            return False
    else: 
        return True 

def validate_email(email):
    """ Checks that the email address is in a valid format, has a username greater than 1 character, an '@' symbol, and an allowed domain that is in the `top_level_domains` variable.

  Args:
    email (str): The inputted email from the user.

  Returns:
    bool: True if the email passes the checks, False otherwise.
    """
    valid_email = False
    username = email.split('@')[0] 
    if '@' not in email:
        return valid_email
    if len(username) < 1:
        return valid_email       
    for domain in top_level_domains:
        if domain in email:
            valid_email = True
    return valid_email


def validate_password(password):
    """ Checks that the password is strong enough. It should include a capital letter, a number between 0-9 and be greater than 8 characters.

  Args:
    password (str): The inputted password from the user.

  Returns:
    bool: True if the password passes the checks, False otherwise.
    """
    has_capital = False
    has_number = False 
    if len(password) < 8:
        return False 
    for char in password:
       if "A" <= char <= "Z":
           has_capital = True
       if "0" <= char <= "9":
           has_number = True
    if has_capital and has_number:
        return True
    else:
        return False


def validate_user(name, email, password):
    """Validate the user name, email and password.

    Args:
        name (string): Name that we're attempting to validate.
        email (string): Email address that we're attempting to validate.
        password (string): Password that we're attempting to validate.

    Returns:
        bool: Returns True if all validation checks pass.

    Raises:
        ValueError: If any validation check fails.
    """
    if validate_name(name) == False:
        raise ValueError("Please make sure your name is greater than 2 characters!")

    if validate_email(email) == False:
        raise ValueError("Your email address is in the incorrect format, please enter a valid email.")

    if validate_password(password) == False:
        raise ValueError("Your password is too weak, ensure that your password is greater than 8 characters, "
                         "contains a capital letter and a number.")

    return True

def register_user(name, email, password):
    """Attempt to register the user if they pass validation.

    Args:
        name (string): Name of the user.
        email (string): Email address of the user.
        password (string): Password of the user.

    Returns:
        dict or bool: Returns a dictionary with the user details if validation is successful,
        or False if the validation fails.
    """
    try:
        validate_user(name, email, password)
    except:
        return False

    user = {
        "name": name,
        "email": email,
        "password": password
    }

    return user
