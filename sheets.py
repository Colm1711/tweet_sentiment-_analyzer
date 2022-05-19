import gspread
import pandas as pd
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


class Sheets():

    def __init__(self):
        self.self = self

    def new_sheet(self, input):
        """
        Description:

        This function creates a new worksheet in main tweet sentiment gspread\
            page.

        Params:
                str - input of newsheet to be created

        Returns:
                new worksheet in gspread workspace

        """
        self.input = input

        try:
            new_sheet = GSPEAD_CLIENT.create(input)
            new_sheet.share('tweet.sentiment.123@gmail.com', perm_type='user',
                            role='writer')
            print(f'Your new sheet {new_sheet} has been created!\n')
        except Exception as inst:
            print(f'{inst} error! Your new worksheet failed to create.')

    def get_worksheets(wksheet):
        """
        Description:

        This function returns a list worksheets in main.

        Params:

        Returns:
                list of worksheet in gspread workspace

        """

        worksheets_list = []

        worksheet_list = wksheet.worksheets()
        for i in worksheet_list:
            worksheets_list.append(i.title)
        return worksheets_list

    def get_col_value_lists(self, wrksht):
        """
        Description:

        This function returns a list worksheets in main.

        Params:


        Returns:
                list of lists - cols are the nested list.
                Returns first 10 by default.

                ex. access list item:

                cols[i]

        """

        self.wrksht = wrksht

        col_worksheet = SHEET.worksheet(wrksht)

        cols = []
        for ind in range(1, 10):
            column = col_worksheet.col_values(ind)
            cols.append(column)
        return cols

    def get_col_vals(sheet, col):
        """
        Description:

        Returns first col of worksheets as list.

        Params:
                sheet = str
                col = int

        Returns:
                list of str's excluding first row.

        """
        try:
            return SHEET.worksheet(sheet).col_values(col)[1:]
        except ValueError as e:
            print(f'Error {e} occurred when retrieving data!')

    def get_row_vals(self, sheet, row):
        """
        Description:

        Returns first row of worksheets as list.

        Params:
                sheet = str
                row = int

        Returns:
                list of str's excluding first row.

        """

        self.sheet = sheet
        self.row = row
        try:
            return SHEET.worksheet(sheet).row_values(row)[1:]
        except ValueError as e:
            print(f'Error {e} occurred when retrieving data!')

    def display_worksheets(self, data):
        """
        Description:

        This displays worksheets with an index number to terminal.

        Params:
                list

        Returns:
                list of sheets and index numbers.
        """
        self.data = data

        for i in data:
            # adding one as index is to start 1 instead of 0
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
            wsheet = SHEET.worksheet(worksheet)
            wsheet.append_row(data)
            return f'Worksheet: {worksheet} updated successfully\n'

        except ValueError as e:
            return f'Invalid data {e}\n'

    def clear_worksheet(self, worksheet):
        """
        Description:

        This clears a worksheet of all data.

        Params:
            worksheet(str) - worksheet to clear

        """
        self.worksheet = worksheet

        try:
            worksheet.clear()
            return f'Worksheeet {worksheet} has been cleared of all values\n'
        except Exception as inst:
            return f'{inst} error! Failed to clear contents of {worksheet}.\n'

    def show_worksheet(self, data):
        """
        Description:

            This shows worksheet in table form

        Params:

            data(str) - sheet to display

        Returns:

            prints table to terminal

        """
        self.data = data

        dataframe = pd.DataFrame(data.get_all_records())
        return dataframe





#1Creates new sheet stock
name = 'Stock'
Ssd = GSPEAD_CLIENT.open(name)
# nw = Sheets().new_sheet(name)
# Just need to add if exists for the spreadsheets

#2Adds new sheet
# sw = Ssd.add_worksheet(title='Stock Data', rows=100, cols=100)
# data = ['Stock Name', 'Dividends', 'P/E', 'Polarity']
# srow = sw.append_row(data)


#3gets rid of the first defaul sheet
# dele = Ssd.get_worksheet(0)
# Ssd.del_worksheet(dele)


#4Make First rpw bold
# upd = Ssd.get_worksheet(0)
# upd.format('1', {'textFormat': {'bold': True}})


#USer to Add new data
# stock_data_row = Ssd.get_worksheet(0)
# stock_data_row.append_row([])

# Logs off and clears
# dele = Ssd.get_worksheet(0)
# dele.clear()