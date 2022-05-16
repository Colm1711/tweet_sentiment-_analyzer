# Imports

import gspread
from google.oauth2.service_account import Credentials
from getpass import getpass
from validation import Validation
from sheets import Sheets as sheets


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
user_data = users.col_values(1)
passw_data = users.col_values(2)

# Welcome message

def welcome_screen():
    """
    Description:

    This function handles the welcome screen for user when they first run
    program.

    Queries user whether they want to log in or register.

    Params:
            none

    Returns:
            none

    """
    print('\nWelcome to the Twitter sentiment application. This is designed to retrieve twitter information and add sentimant scores to data.\n')
    print('If you are returning user please Login. Dont have an account or first time vistor please select the Register option. \n' )

    log_reg = input('Login(L) or Register(R)? : ')
    if log_reg.lower() == "l" or log_reg.lower() == 'login':
        user_login_details()
    elif log_reg.lower() == 'r' or log_reg.lower() == 'Register':
        user_registration()
    elif log_reg.lower() != 'r' or 'l' or log_reg != 'login' or 'Register':
        print('\nWARNING! You must select a vaild option')
        log_reg = input('Login(L) or Register(R)? : ')
        welcome_screen()
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
        
    # checks details are valid email and password
    val_email = Validation.email_valid(email)
    val_password = Validation.psw_valid(password)
    if(val_email and val_password):
        return access_level(email, password)
    else:   
        print(f'This information failed validation.')
        user_login_details()
         

        
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
    # This handles user registering name
    print('Please fill out your details: \n')
    name = input('Please your name: ')

    # This handles user registering organization
    institution = input('Please enter institution you work for: ')

    # This handles user registering email
    print('Please enter your email and the password you would like.\n')
    print('Please note that your email must include @ symbol')
    email = input('Please enter your email: ')

    # This handles user registering password
    print('Please your password must be at least 6 charecters long and must be alphanumeric')
    password = getpass('Please enter your password: ')
    val_email = Validation.email_valid(email)
    val_password = Validation.psw_valid(password)
    
    return name, institution, val_email, val_password


def access_level(user, password):
    """
    Description:

    This function handles access level when logging in.
    It is set to False by default.

    Params:
            str - user
            str - password 

    Returns:
            Boolean - True or False

    """
    # setting access level to default of False
    admin_access = False

    # accessing the admin creds file
    admin_user = sheets.get_col_vals('Admin', 1)
    admin_passw = sheets.get_col_vals('Admin', 2)
    user_val = sheets.get_col_vals('Users', 1)  
    pswd_val = sheets.get_col_vals('Users', 2)
    # check to see if DB accessible
    # checking DB to see if user email and password are registered users
    # starts the main python file
    try:
        if user in user_val and password in pswd_val:
            main(admin_access, user, password)
        # user email and password are admin access updating var to True
        # starts the main python file
        elif user in admin_user and password in admin_passw:
            admin_access = True
            main(admin_access, user, password)
            return admin_access
        else:
            print('You have not entered valid details\n')
            user_login_details()
        return admin_access
    except:
        print('Could not access database')
  

def main(access_level, user, password):

        print('\nWhat stock would you like to get price and sentiment data for?\n')
        stock_p_item = input('Stock: ')
        print(stock_p_item)
    
welcome_screen()

