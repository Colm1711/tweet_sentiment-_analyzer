# Imports

import gspread
from google.oauth2.service_account import Credentials
from getpass import getpass
from validation import Validation



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


# Vars

# Googlesheet vars
users = SHEET.worksheet('Users')
user_data = users.get_all_values()

# Welcome message

def welcome_screen():
    """
    Description:

    This function handles the welcome screen for user when they first run
    program.

    Queries user whether they want to log in or register.
    
    """
    print('\nWelcome to the Twitter sentiment application. This is designed to retrieve twitter information and add sentimant scores to data.\n')
    print('If you are returning user please Login. Dont have an account or first time vistor please select the Register option. \n' )
    log_reg = input('Login(L) or Register(R)? : ')
    if log_reg.lower() == "l" or log_reg == 'Login':
        user_login_details()
    elif log_reg.lower() == 'r' or log_reg == 'Register':
        user_registration()
    elif log_reg.lower() != 'r' or 'l' or log_reg != 'login' or 'Register':
        print('You must select a valid option: Login or Register - YOU HAVE 1 MORE ATTEMPT\n')
        log_reg = input('Login(L) or Register(R)? : ')
        if log_reg.lower() == "l" or log_reg == 'Login':
            user_login_details()
        elif log_reg.lower() == 'r' or log_reg == 'Register':
            user_registration()
    else:
        print('Something has gone wrong here.')  

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
    password = getpass('Please enter your password: ')
    val_email = Validation.email_valid(email)
    val_password = Validation.psw_valid(password)
    return val_email, val_password

def user_registration():
    """
    Description:

    This function handles user registration.
    Calls on the user_login_detail

    Params:
            none

    Returns:
            str - name
            str - institution
            str - val_email
            str - val_password
    
    """
    print('Please fill out your details: \n')
    name = input('Please your name: ')
    institution = input('Please enter institution you work for: ')
    print('Please enter your email and the password you would like.\n')
    print('Please note that your email must include @ symbol')
    email = input('Please enter your email: ')
    print('Please your password must be at least 6 charecters long and must be alphanumeric')
    password = getpass('Please enter your password: ')
    val_email = Validation.email_valid(email)
    val_password = Validation.psw_valid(password)
    
    return name, institution, val_email, val_password




welcome_screen()

