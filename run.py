# Imports
import gspread
from google.oauth2.service_account import Credentials


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
    This function handles the welcome screen for user when they first run program.
    It asks user whether they want to log in or register.

    Params:
    

    Returns:
    
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

            str - email
            str - password
    
    """

    print('Please enter your email and the password you would like.\n')
    print('Please note that your email must include @ symbol')
    print('Please your password must be at least 6 charecters long and must be alphanumeric')
    email, password = user_login_details()
    return email, password

def val_password(password):
    """
    Description:

    This function handles user registration.
    Calls on the user_login_detail

    Params:
            password

    """
    valid = 0
    password = password
    if len(password) < 6:
        for i in password:
            if (i.islower()):
                valid += 1
            if (i.isupper()):
                valid += 1
            if (i.isdigit()):
                valid += 1

    print(valid)       
    if valid < len(password):
        print("Your password was not valid, please try again")
    else:
        print('password is valid')


#welcome_screen()
email, password = user_login_details()
val_password(password)


