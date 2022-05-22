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

    def get_col_vals(sheet, col):
        """
        Description:

        Returns first col of worksheets as list.

        Params:
            str -->  sheet
            int -->  col

        Returns:
                list of str's excluding first row.

        """
        try:
            return SHEET.worksheet(sheet).col_values(col)[1:]
        except ValueError as e:
            print(f'Error {e} occurred when retrieving data!')

    def get_row_vals(sheet, row):
        """
        Description:

        Returns first row of worksheets as list.

        Params:
            str --> sheet
            int --> row

        Returns:
                list of str's excluding first row.

        """
        try:
            return SHEET.worksheet(sheet).row_values(row)[1:]
        except ValueError as e:
            print(f'Error {e} occurred when retrieving data!')

    def update_worksheet_row(data, worksheet):
        """
        Description:

        This updates a new row to the worksheet.

        Params:
            str -->  data - informmation to update
            str -->  worksheet - worsheet to update

        Returns:
                print message of success

        """
        try:
            wsheet = SHEET.worksheet(worksheet)
            wsheet.append_row(data)
            return f'Worksheet: {worksheet} updated successfully\n'

        except ValueError as e:
            return f'Invalid data {e}\n'

    def show_worksheet(data):
        """
        Description:

            This shows worksheet in table form

        Params:

            str --> data - sheet to display

        Returns:

            prints table to terminal

        """
        dataframe = pd.DataFrame(data.get_all_records())
        return dataframe

    def clear_sheet_exit():
        """
        Description:

        This function handles clearing the Stock Dasta sheet on users exit from
        application

        """
        name = 'Stock'
        stockdata_sh = GSPEAD_CLIENT.open(name).sheet1
        fmt_undo = stockdata_sh.format("1", {"backgroundColor": {
                                                "red": 1.0,
                                                "green": 1.0,
                                                "blue": 1.0
                                            }, "textFormat": {
                                            "foregroundColor": {
                                                "red": 1.0,
                                                "green": 1.0,
                                                "blue": 1.0
                                                                },
                                            "bold": False}})
        stockdata_sh.clear()

    def del_reg(row):
        """
    	Description:

        This function handkes the deletion of user from Registration
        after the user details have been moved to User sheets.

        int --> row

        """
        name = 'authentication'
        sheet = 'Registration applications'
        # increments value by two due to difference in indexing between
        # terminal output and excelsheet
        row = row + 2
        # delete record
        reg_data_sh = GSPEAD_CLIENT.open(name).worksheet(sheet)
        reg_data_sh.delete_rows(row)
