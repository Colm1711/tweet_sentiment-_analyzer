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
user_data = users.col_values(1)
passw_data = users.col_values(2)

def new_sheet(input):
    """
    Description:

    This function creates a new worksheet in main tweet sentiment gspread page.

    Params:
            str - input of newsheet to be created

    Returns:
            new worksheet in gspread workspace 

    """
    try:
        new_sheet = GSPEAD_CLIENT.create(input)
        new_sheet.share('tweet.sentiment.123@gmail.com', perm_type='user', role='writer')
        print(f'Your new sheet {new_sheet} has been created!\n')
    except Exception as inst:
        print(f'{inst} error! Your new worksheet failed to create.')


def get_worksheets():
    """
    Description:

    This function returns a list worksheets in main.

    Params:
            

    Returns:
            list of worksheet in gspread workspace 

    """    

    worksheets_list = []

    worksheet_list = SHEET.worksheets()
    for i in worksheet_list:
        worksheets_list.append(i.title)
    return worksheets_list


def get_col_values(wrksht):
    """
    Description:

    This function returns a list worksheets in main.

    Params:
            

    Returns:
            list of lists - cols are the nested list.append(self, object)
            Returns first 10 by default.
            access via cols[i]

    """
    col_worksheet = SHEET.worksheet(wrksht)

    cols = []
    for ind in range(1, 10):
        column = col_worksheet.col_values(ind)
        cols.append(column)
    return cols


def display_worksheets(data):
    """
    Description:

    This displays worksheets with an index number to terminal.

    Params:
            list

    Returns:
            list of sheets and index numbers.

    """
    for i in data:
        index = data.index(i) + 1
        print(f'{index} : {i}')


def update_worksheet_row(data, worksheet):
    """
    Description:

    This updates a new row to the worksheet.

    Params:
            data(str) - informmation to update
            worksheet(str) - worsheet to update

    Returns:
            list of sheets and index numbers.

    """

    try:
        print(f'Updating the following {worksheet}\n')
        wsheet = SHEET.worksheet(worksheet)
        wsheet.append_row(data)
        print(f'Worksheet: {worksheet} updated successfully\n')
        current_ws = get_worksheets()
        return f'\n{current_ws}'

    except ValueError as e:
        return f'Invalid data {e}\n'   


def del_worksheet(ws):
    """
    Description:

    This deltes a worksheet.

    Params:
            ws(str) - worksheet to delete

    """
    del_worksheet = SHEET.worksheet(ws)
    try:
        SHEET.del_worksheet(del_worksheet)
        return f'Worksheeet {del_worksheet} has been deleted\n'
    except Exception as inst:
        return f'{inst} error! Failed to delete {del_worksheet}.\n'


def clear_worksheet(worksheet):
    """
    Description:

    This clears a worksheet of all data.

    Params:
        worksheet(str) - worksheet to clear

    """
    worksheet = worksheet
    try:
        worksheet.clear()
        return f'Worksheeet {worksheet} has been cleared of all values\n'
    except Exception as inst:
        return f'{inst} error! Failed to clear contents of {worksheet}.\n'

