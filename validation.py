# Imports

import sys
import re
from string import punctuation, whitespace, digits, ascii_uppercase, ascii_lowercase


# CONSTANTS

REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Validation():
    """
        Description:

        This Class handles validating of information.

        Params:

        Returns:

    
    """


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
        digit = Validation._has_digit(data_to_val)
        lowercase = Validation._has_lowercase(data_to_val)
        punc = Validation._has_punc(data_to_val)
        upper = Validation._has_uppercase(data_to_val)
        
        if len(data_to_val) > 6:
            if digit and lowercase and punc and upper == True:
                return True
            else:
                print('This password is not valid, must be alphanumeric with lowercase, uppercase & punctuation symbols\n')
                return False
        else:
            print('\nThis is not a valid password.')
            #Setting to system exit for now. Need to add handling of incorrect information
            return sys.exit()

    def email_valid(email):
        """
        Description:

        This function handles email validating using regular expressions.

        Params:
                email --> use regualr expressions to check for email

        Returns:

                Boolean - True --> if all conditions are met
                Boolean - False --> if any conditions are not met
        
        """
        if re.fullmatch(REGEX, email):
            return True
        else:
            print('\nThis is not a valid email')
            return False

    def _has_digit(data_to_val):
        # This will evaluate if there is a digit and will return true if present.
        # This is a private function
        pw_has_digits = False
        data_to_val = data_to_val.strip()

        for i in data_to_val:
            if i in digits:
                pw_has_digits = True
                break

        if not pw_has_digits:
            return False

        return True

    def _has_uppercase(data_to_val):    
        # This will evaluate if there is uppercase and will return true if 
        # present
        # This is a private function
        pw_has_upper = False
        data_to_val = data_to_val.strip()

        for i in data_to_val:
            if i in ascii_uppercase:
                pw_has_upper = True
                break
            
        if not pw_has_upper:
            return False

        return True


    def _has_lowercase(data_to_val):
        # This will evaluate if password has lowercase and will return true if 
        # present
        # This is a private function
        pw_has_lower = False
        data_to_val = data_to_val.strip()

        for i in data_to_val:
            if i in ascii_lowercase:
                pw_has_lower = True
                break
            
        if not pw_has_lower:
            return False

        return True


    def _has_punc(data_to_val):
        # This will evaluate if password has punctutiations and will return true if 
        # present
        # This is a private function
        pw_has_punc = False
        data_to_val = data_to_val.strip()

        for i in data_to_val:
            if i in punctuation:
                pw_has_punc = True
                break
            
        if not pw_has_punc:
            return False

        return True

