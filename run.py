# Imports

import os
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
BREAK = '#' * 66

# Welcome message


def welcome_screen():
    """
    Description:

    This function handles the welcome screen for user when they first run
    program.

    Queries user whether they want to log in or register by comparing user_
    input against if/else statements.

    Params:
            none

    Returns:
            none

    """
    print(BREAK, flush=True)
    print('\n       Welcome to the Twitter sentiment application.\n',
          flush=True)
    print(BREAK, flush=True)
    time.sleep(1.5)
    print('\nThis is designed to retrieve stock data and twitter '
          'information\nadding sentiment scores to data.\n', flush=True)
    time.sleep(1)
    print('If you are returning user please Login.\n\nDont have an account or'
          ' first time vistor? Please select the\nRegister option.\n')
    time.sleep(1)
    # Login or Register query
    log_reg = input('Login(L) or Register(R)? : ')
    if log_reg.lower() == "l" or log_reg.lower() == 'login':
        user_login_details()
    elif log_reg.lower() == 'r' or log_reg.lower() == 'register':
        user_registration()
    else:
        os.system('clear')
        print('\n\nWARNING! You must select a vaild option: \n')
        print('options: Login(L) or Register(R)')
        print('\nReturning to Welcome screen....\n')
        time.sleep(4)
        os.system('clear')
        welcome_screen()


def user_login_details():
    """
    Description:

    This function handles colleciton of user log in input
    and exports results to access level function.

    Params:
            none

    Returns:

        str --> email
        str --> password
    """

    email = input('Please enter your email: ')
    password = getpass('Please enter your password: ')
    return access_level(email, password)


def user_registration():
    """
    Description:

    This function handles user registration.
    Calls on the user_login_detail to handle the inputs.
    Calls on validation to check user inputs.

    Params:
            none

    Returns:
            str --> name
            str --> institution
            str --> val_email
            str --> val_password
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
    print('Please your password must be at least 6 charecters long '
          'and must be alphanumeric\n')
    password = getpass('Please enter your password: ')
    val_email = Validation.email_valid(email)
    val_password = Validation.psw_valid(password)
    data = name, institution, email, password
    curr_sheet = 'Registration applications'
    sheets.update_worksheet_row(data, curr_sheet)
    os.system('clear')
    print(f'\nThank you {name} for your interest with us. Why not check'
          'out our twitter page @TSentiment123 \n')
    print('\nReturning to Welcome screen, admin team will be in contact\n')
    time.sleep(8)
    os.system('clear')
    welcome_screen()
    return name, institution, val_email, val_password


def access_level(user, password):
    """
    Description:

    This function handles access level when logging in.
    It is set to False by default.
    Runs main() with updated access level.

    Params:
            str --> user
            str --> password
    Returns:
             Boolean --> True or False

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


def admin_ready():
    """
    Description:
        Handles the ready status of admin. If input is yes returns to main
        menu.
        If invalid option entered, uses recursion to query user to try again.

    """
    print('\n\n\nAre you Ready?\n')
    ready = input('Yes(Y)? This will return you to Homescreen: ')
    if ready.lower() == 'yes' or ready.lower() == 'y':
        main(True)
    else:
        print('Not a valid option')
        admin_ready()


def user_ready():
    """
    Description:
        Handles the ready status of user. If input is yes returns to main menu.
        If invalid option entered, uses recursion to query user to try again.
    """
    print('\n\n\nAre you Ready?\n')
    ready = input('Yes(Y)? This will return you to Homescreen: ')
    if ready.lower() == 'yes' or ready.lower() == 'y':
        main(False)
    else:
        print('Not a valid option')
        user_ready()


def main(access_level):
    """
    This function handles Admin and user menu and options.

    User level - can access the Stocks Data sheet to query live stock data

    Admin level - can access protected sheets in Database & approve users.

    Params:
        Boolean --> access level
    """
    # User menu options
    user_menu = {
                    1: 'Get Top 500 companies stock info from SP500 and'
                       'sentiment?',
                    2: 'Get a companies stock data for the week',
                    3: 'Exit',
    }
    # Admin User options.
    admin_menu = {
                    1: 'View Users list?',
                    2: 'View Admin list?',
                    3: 'View User registration list?',
                    4: 'Exit',
    }
    # setting worksheets to vars
    user_sheet = SHEET.worksheet('Users')
    admin_sheet = SHEET.worksheet('Admin')
    reg_sheet = SHEET.worksheet('Registration applications')
    stock_sheet = GSPEAD_CLIENT.open('Stock').worksheet('Stock Data')

    if access_level is True:
        os.system('clear')
        print(BREAK)
        print('\n               YOU HAVE ACCESSES ADMIN LEVEL\n')
        print(BREAK)
        print('\nWhat would you like to do?\n')
        # Admin Menu
        for key in admin_menu.keys():
            print(f'{key} - {admin_menu[key]}', flush=True)
        option = input()
        check_option = Validation.has_digit(option)
        # check to ensure option enterd has digit
        if check_option is False:
            print('You must select a valid option!')
            time.sleep(1)
            os.system('clear')
            main(True)
        else:
            # converts to int before ps
            option = int(option)
            pass
        # credit to this code goes to Gerry McBride in python class
        if option in [1, 2, 3, 4]:
            pass
        else:
            print('You must select a valid option!')
            time.sleep(2)
            os.system('clear')
            main(True)
        # Users list
        if option == 1:
            os.system('clear')
            print('\nUsers list\n')
            users = sheets.show_worksheet(user_sheet)
            print(users)
            admin_ready()
        # Admin list
        elif option == 2:
            os.system('clear')
            print('\nAdmin list\n')
            admins = sheets.show_worksheet(admin_sheet)
            print(admins)
            admin_ready()
        # User registration list
        elif option == 3:
            os.system('clear')
            # presents user with registration list
            print('\nUser registration list\n')
            reg_list = sheets.show_worksheet(reg_sheet)
            print(reg_list)
            # Queries user if they want to do next
            print('\nApprove user? Yes(Y)')
            approval = input()
            if approval.lower() == 'yes' or approval.lower() == 'y':
                print('Which user from table above? Please pick by index '
                      'number')
                user_to_approve = input()
                check_input = Validation.has_digit(user_to_approve)
                # check to ensure option enterd has digit
                if check_input is False:
                    print('You must select a valid option!')
                    print('Returning to Home Menu')
                    main(True)
                else:
                    # converts to int before ps
                    user_to_approve = int(user_to_approve)
                    pass
                user_choice = user_to_approve + 2
                reg_user = sheets.get_row_vals('Registration applications',
                                               user_choice)
                move_to_user = sheets.update_worksheet_row([reg_user[1],
                                                            reg_user[2]],
                                                           'Users')
                print('Usersheet has been updated!\n')
                print('Now deleting from registration page...')
                sheets.del_reg(user_to_approve)
                print('All Done!')
                # waiting so script has chance to update
                time.sleep(10)
                print(reg_list)
                admin_ready()
            else:
                print('Need to input a valid option as this is sensitive data! Please try again\n')
                print('Returning to Home Menu')
                time.sleep(5)
                os.system('clear')
                main(True)
        else:
            print('Returning Home Screen.')
            time.sleep(3)
            os.system('clear')
            welcome_screen()
    # User Menu
    else:
        os.system('clear')
        print(BREAK)
        print('\n              Welcome to the home screen!\n')
        print(BREAK)
        print('\nWhat would you like to do?\n')
        for key in user_menu.keys():
            print(f'{key} - {user_menu[key]}')
        option = input()
        check_option = Validation.has_digit(option)
        # check to ensure option enterd has digit
        if check_option is False:
            print('You must select a valid option!')
            time.sleep(1)
            os.system('clear')
            main(False)
        else:
            # converts to int before ps
            option = int(option)
            pass
        # credit to this code goes to Gerry McBride in python class
        if option in [1, 2, 3]:
            pass
        else:
            print('You must select a valid option!')
            time.sleep(1)
            os.system('clear')
            main(False)
        # Stock sentiment Option
        if option == 1:
            sheets.clear_sheet_exit()
            os.system('clear')
            print('\nGet Top 500 companies stock info from SP500!\n')
            #  limiting to 10 as heavy on resources and time

            name = 'Stock'
            stockdata_sh = GSPEAD_CLIENT.open(name).sheet1
            data = ['Stock Name', 'Ticker', 'Price($)', 'Dividend', 'P/E',
                    'Polarity']
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
            try:
                stock_comp_list = si.get_ls_companies()
                stock_tick_list = si.get_ls_tickers()
                # limiting to 5 as heavy on resources and time
                # This adds stock name to the excel sheet
                for i in range(2, 7):
                    f_data = stock_comp_list[i]
                    stockdata_sh.update_cell(i, 1, f_data)
                    print('Updating stock sheet with data, please wait...\n\n')
                    # limiting to 5 as heavy on resources and time
                    # This adds ticker name and data to the excel sheet
                    # getting list of Stock Names and setting to data
                    data = stock_tick_list[i]
                    # getting qoute table to pass through for ticker, div, pe
                    quote_t = si.get_quote_table(data)
                    # getting Stock Names and setting to tick_data
                    tick_data = si.get_stock_price(quote_t)
                    # getting ticker list for Stock Names and setting to
                    # div_data
                    div_data = si.get_dividends(quote_t)
                    # getting ticker list for Stock Names and setting to
                    # pe_data
                    pe_data = si.get_pe_ratio(quote_t)
                    # getting polarity for Stock Names ticker and setting to
                    # pol_data
                    pol_data = tweet.polarity_analysis(data)
                    os.system('clear')
                    time.sleep(2)
                    print(f'Stock name: {f_data}')
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 2, data)
                    print(f'Wrote {data} ticker name to Stock sheet')
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 3, tick_data)
                    print(f'Wrote {tick_data} share price to Stock sheet')
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 4, div_data)
                    print(f'Wrote {div_data} dividend to Stock sheet')
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 5, pe_data)
                    print(f'Wrote {pe_data} PE ratio to Stock sheet')
                    time.sleep(2)
                    stockdata_sh.update_cell(i, 6, pol_data)
                    print(f'Wrote {pol_data} polarity data to Stock sheet')
                    time.sleep(2)
                    print('Sheet has been populated with live data!')
                    os.system('clear')
                    time.sleep(2)
                complete_stock_sheet = sheets.show_worksheet(stock_sheet)
                print(complete_stock_sheet)
                print('\\nA polarity above 0 means tweets about company is '
                      'trending positive')
                print('\nA polarity below 0 means tweets about company is '
                      'trending negative')
                print('A polarity of 0 is neutral!(It never happens ;-) )')
                user_ready()
            except:
                print('ERROR: Could not apply data to excelsheet,'
                      'please reach out to admin on this')
                sheets.clear_sheet_exit()
                time.sleep(2)
                os.system('clear')
                main(False)
        # Returns the stock data for the week to user for given stock name.
        elif option == 2:
            os.system('clear')
            print('\nGet a companies stock data for the week:\n')
            s = si.get_companies()
            print(s.iloc[:, 1])
            print('\nEnter stock you would like data for:\n')
            # user inputs the stock to check
            stock_p_item = input()
            if stock_p_item.islower() is True:
                stock_p_item = stock_p_item.title()
            else:
                pass
                user_ready()
            try:
                # Stock Data to be returned to terminal to user.
                stock_ticker = si.get_ticker(stock_p_item)
                stock_price = si.get_weeks_stock_data(stock_ticker)
                print(stock_price)
            except:
                print('ERROR: Could not retrieve data to excelsheet, please'
                      ' reach out to admin on this')
                time.sleep(5)
                main(False)
        else:
            # clears the stock data sheet on exit
            sheets.clear_sheet_exit()
            print('Exiting......')
            time.sleep(3)
            os.system('clear')
            welcome_screen()

welcome_screen()