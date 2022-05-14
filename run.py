# Imports

import re
import gspread
from google.oauth2.service_account import Credentials
from string import punctuation, whitespace, digits, ascii_uppercase, ascii_lowercase



# Constants
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPEAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPEAD_CLIENT.open('authentication')
REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Vars

# Googlesheet vars
users = SHEET.worksheet('Users')
user_data = users.get_all_values()

# Welcome message

def welcome_screen():
    """
    Description:
    This function handles the welcome screen for user when they first run program.
    It asks user whether they want to log in or register.
    
    """
    print('Welcome to the Twitter sentiment application')
    log_reg = input('Login or Register? : ')
    if log_reg == "Login":
        user_login_details()
    elif log_reg == 'Register':
        user_registration()
    else:
        print('pass')    

def user_login_details():
    """
    Description:

    This function handles colleciton of user log in.

    Params:
            none

    Returns:

            str - email
            str - password
    
    """
    email = input('Please enter your email: ')
    password = input('Please enter your password: ')
    return email, password

def user_registration():
    """
    Description:

    This function handles user registration.
    Calls on the user_login_detail

    Params:
            none

    Returns:
            str - Name
            str - Business
            str - email
            str - password
    
    """
    name = input('Please your name: ')
    business = input('Please enter institution you work for: ')
    print('Please enter your email and the password you would like.\n')
    print('Please note that your email must include @ symbol')
    print('Please your password must be at least 6 charecters long and must be alphanumeric')
    email, password = user_login_details()
    return name, business, email, password

# DATA VALIDATION

def psw_valid(data_to_val):
    """
    Description:

    This function handles validating of information.
 
    Params:
            data_to_val --> this is the data you want validated for 
                            uppercase, lowercase, digits & val

    Returns:

            Boolean - True --> if all conditions are met
            Boolean - False --> if any conditions are not met
    
    """
    data_to_val = data_to_val

    digit = has_digit(data_to_val)
    lowercase = has_lowercase(data_to_val)
    punc = has_punc(data_to_val)
    upper = has_uppercase(data_to_val)
    
    if digit and lowercase and punc and upper == True:
        print('Valid')
        return True
    else:
        print('Not valid')
        return False
        

def has_digit(data_to_val):
    # This will evaluate if there is a digit and will return true if present
    pw_has_digits = False
    data_to_val = data_to_val.strip()

    for i in data_to_val:
        if i in digits:
            pw_has_digits = True
            break

    if not pw_has_digits:
        return False

    return True

def has_uppercase(data_to_val):    
    # This will evaluate if there is uppercase and will return true if 
    # present
    pw_has_upper = False
    data_to_val = data_to_val.strip()

    for i in data_to_val:
        if i in ascii_uppercase:
            pw_has_upper = True
            break
        
    if not pw_has_upper:
        return False

    return True


def has_lowercase(data_to_val):
    # This will evaluate if password has uppercase and will return true if 
    # present
    pw_has_lower = False
    data_to_val = data_to_val.strip()

    for i in data_to_val:
        if i in ascii_lowercase:
            pw_has_lower = True
            break
        
    if not pw_has_lower:
        return False

    return True


def has_punc(data_to_val):
    # This will evaluate if password has uppercase and will return true if 
    # present
    pw_has_punc = False
    data_to_val = data_to_val.strip()

    for i in data_to_val:
        if i in punctuation:
            pw_has_punc = True
            break
        
    if not pw_has_punc:
        return False

    return True

def email_valid(email):
        """
    Description:

    This function handles email validating.
 
    Params:
            email --> use regualr expressions to check for email

    Returns:

            Boolean - True --> if all conditions are met
            Boolean - False --> if any conditions are not met
    
    """
    if re.fullmatch(REGEX, email):
        return True
    else:
        return False


name, business, email, password = user_registration()
psw_valid(password)
email_valid(email)



