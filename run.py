# Imports

import gspread
import stocks_info as si
import time
from google.oauth2.service_account import Credentials
from getpass import getpass
from validation import Validation
from sheets import Sheets as sheets
from tweet_api import TweetSentiment as tweet


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
    print('\nWelcome to the Twitter sentiment application. This is designed to\
 retrieve sotck data and twitter information adding sentimant scores to\
 data.\n')
    print('If you are returning user please Login. Dont have an account or first\
 time vistor please select the Register option. \n')

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
    return access_level(email, password)


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
    print('\nPlease enter your email and the password you would like.\n')
    print('Please note that your email must include @ symbol\n')
    email = input('Please enter your email: ')

    # This handles user registering password
    print('Please your password must be at least 6 charecters long and must be\
 alphanumeric\n')
    password = getpass('Please enter your password: ')
    val_email = Validation.email_valid(email)
    val_password = Validation.psw_valid(password)
    data = name, institution, email, password
    curr_sheet = 'Registration applications'
    sheets.update_worksheet_row(data, curr_sheet)
    print('\n Thank you for submitting your interest with us. Why not check\
        out our twitter page @TSentiment123 \n')
    print('\n Returning to Welcome screen, admin team will be in contact\n')
    welcome_screen()
    return name, institution, val_email, val_password


def access_level(user, password):
    """
    Description:

    This function handles access level when logging in.
    It is set to False by default.
    Runs main() with update.

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
    if user in user_val and password in pswd_val:
        main(admin_access)
    # user email and password are admin access updating var to True
    # starts the main python file
    elif user in admin_user and password in admin_passw:
        admin_access = True
        main(admin_access)
    else:
        print('You have not entered valid details\n')
        user_login_details()


def main(access_level):
    """
    This function handles Admin and user menu and options.

    Params:
            access level - Boolean
    """

    user_menu = {
                    1: 'Get Top 500 companies stock info from SP500 and sentiment?',
                    2: 'Get a companies stock data for the week',
                    3: 'Exit',
    }
    admin_menu = {
                    1: 'View Users list?',
                    2: 'View Admin list?',
                    3: 'View User registration list?',
                    4: 'Exit',
    }

    user_sheet = SHEET.worksheet('Users')
    admin_sheet = SHEET.worksheet('Admin')
    reg_sheet = SHEET.worksheet('Registration applications')

    if access_level is True:
        print('\nYou have accessed admin level\n')
        print('What would you like to do?\n')
        # Admin Menu
        for key in admin_menu.keys():
            print(f'{key} - {admin_menu[key]}')
        option = int(input())
        # Users list
        if option == 1:
            print('\nUsers list\n')
            users = sheets().show_worksheet(user_sheet)
            print(users)
            print('\n\n\nAre you Ready?\n')
            ready = input('Yes(Y)? This will return you to Homescreen: ')
            if ready.lower() == 'yes' or 'y':
                main(True)
        # Admin list
        elif option == 2:
            print('\nAdmin list\n')
            admins = sheets().show_worksheet(admin_sheet)
            print(admins)
            print('\n\n\nAre you Ready?\n')
            ready = input('Yes(Y)? This will return you to Homescreen: ')
            if ready.lower() == 'yes' or 'y':
                main(True)
        # User registration list
        elif option == 3:
            print('\nUser registration list\n')
            reg_list = sheets().show_worksheet(reg_sheet)
            # print(reg_sheet)
            print(reg_list)

            print('Approve user?Yes(Y)')
            approval = input()
            if approval.lower() == 'yes' or 'y':
                print('Which user from table above? Please pick by idnex number')
                user_to_approve = int(input())
                user_choice = user_to_approve +  2
                reg_user = sheets.get_row_vals('Registration applications', user_choice)
                move_to_user = sheets.update_worksheet_row([reg_user[1], reg_user[2]], 'Users')
                print(' Usersheet has been updated!\n')
                print('Now deleting from registration page...')
                sheets.del_reg(user_to_approve)
                print('All Done!')
                main(True)
            else:
                print('\n\n\nAre you Ready?\n')
                ready = input('Yes(Y)? This will return you to Homescreen: ')
                if ready.lower() == 'yes' or 'y':
                    main(True)
        else:
            print('Reurning Home')
            welcome_screen()
    # User Menu
    else:
        print('\nWelcome to the home screen!\n')
        print('What would you like to do?\n')
        for key in user_menu.keys():
            print(f'{key} - {user_menu[key]}')
        option = int(input())
        # Stock sentiment Option
        if option == 1:
            print('\nGet Top 500 companies stock info from SP500!\n')
            print('Updating stock sheet with data, please wait')
            #  limiting to 10 as heavy on resources and time
            try:
                name = 'Stock'
                stockdata_sh = GSPEAD_CLIENT.open(name).sheet1
                data = ['Stock Name', 'Ticker', 'Price($)', 'Dividend', 'P/E', 'Polarity']
                stockdata_sh.append_row(data)
                stockdata_sh.format('1', {
                                            "backgroundColor": {
                                                "red": 0.0,
                                                "green": 0.0,
                                                "blue": 1.0
                                                            },
                                            "horizontalAlignment": "CENTER",
                                            "textFormat": {
                                                "foregroundColor": {
                                                    "red": 1.0,
                                                    "green": 1.0,
                                                    "blue": 1.0
                                                                    },
                                                    "fontSize": 12,
                                                    "bold": True
                                                            }
                                            })
                stock_comp_list = si.get_ls_companies()
                # limiting to 5 as heavy on resources and time
                # This adds stock name to the excel sheet
                for i in range(2, 7):
                    data = stock_comp_list[i]
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 1, data)
                # limiting to 5 as heavy on resources and time
                # This adds ticker name and data to the excel sheet
                stock_tick_list = si.get_ls_tickers()
                for i in range(2, 7):
                    data = stock_tick_list[i]
                    quote_t = si.get_quote_table(data)
                    tick_data = si.get_stock_price(quote_t)
                    div_data = si.get_dividends(quote_t)
                    pe_data = si.get_pe_ratio(quote_t)
                    pol_data = tweet.polarity_analysis(tick_data)
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 2, data)
                    time.sleep(1)
                    stockdata_sh.update_cell(i, 3, tick_data)
                    time.sleep(1)
                    stockdata_sh.update_cell(i, 4, div_data)
                    time.sleep(1)
                    stockdata_sh.update_cell(i, 5, pe_data)
                    time.sleep(1)
                    stockdata_sh.update_cell(i, 6, pol_data)
                print('Done')
                main(False)
            except:
                print('ERROR: Could not apply data to excelsheet, please reach out to admin on this')
                main(False)
        # Saved retuns
        elif option == 2:
            print('Get a companies stock data for the week')
            s = si.get_companies()
            print(s.iloc[:, 1])
            print('\nEnter stock you would like data for(Please note you must\
                enter companies name as it appears e.g. "Apple" not "apple"):\n')
            stock_p_item = input()
            try:
            # Stock Data
                stock_ticker = si.get_ticker(stock_p_item)
                stock_price = si.get_weeks_stock_data(stock_ticker)
                print(stock_price)
            except:
                print('ERROR: Could not get data, please reach out to admin on this')
                main(False)
            print('\n\n\nAre you Ready?\n')
            ready = input('Yes(Y)? This will return you to Homescreen: ')
            if ready.lower() == 'yes' or 'y':
                main(False)
        else:
            # clears the stock data sheet on exit
            sheets.clear_sheet_exit()
            print('Exiting......')
            welcome_screen()

main(True)



