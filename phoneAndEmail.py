#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

emailRegex = re.compile(r"'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))", re.VERBOSE)

phoneRegex = re.compile(r"'(
                        (\d{3}|\(d{3}\))?    #area code
                        (\s|-|\.)?           #separator
                        (\d{3})              #first 3 digits
                        (\s|-|\.)            #separator
                        (\d{4})              #last 4 digits
                        (\s*(ext[x]ext.)\s*(\d{2,5}))?       #extension
                        )"', re.VERBOSE)

#TODO:Create email Regex
#Find matches in clipboard text
#Copy results to the clipboard