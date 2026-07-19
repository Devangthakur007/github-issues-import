#!/usr/bin/env python3

import getpass
import sys

def username(question: str) -> str:
    """
    Prompts for a username. Includes a framework to disallow spaces 
    or special characters if needed in the future.
    """
    while True:
        name = input(question).strip()
        if not name:
            print("Username cannot be empty. Please try again.")
            continue
        
        # Optional: Uncomment the lines below when you want strict alphanumeric validation
        # if not name.isalnum():
        #     print("Invalid username. Only alphanumeric characters are allowed.")
        #     continue
            
        return name

def password(question: str) -> str:
    """
    Securely prompts for a password masking user input in the terminal.
    """
    return getpass.getpass(question)

def yes_no(question: str, default: bool = True) -> bool:
    """
    Ask a yes/no question via input() and return a boolean value.
    
    Validates variations of yes/no options and handles default fallback execution.
    Refactored from http://code.activestate.com/recipes/577058-query-yesno/
    """
    choices = {
        "yes": True, "y": True, "ye": True,
        "no": False, "n": False
    }
    
    if default is None:
        prompt = " [y/n] "
    elif default is True:
        prompt = " [Y/n] "
    elif default is False:
        prompt = " [y/N] "
    else:
        raise ValueError(f"Invalid default answer: '{default}'")

    while True:
        # standard print with end='' keeps the cursor text on the exact same line safely
        print(question + prompt, end='', flush=True)
        choice = input().strip().lower()
        
        if default is not None and choice == '':
            return default
        
        if choice in choices:
            return choices[choice]
            
        print("Please respond with 'yes' or 'no' (or 'y' or 'n').")

# --- Example Usage to Test the Script ---
if __name__ == "__main__":
    print("--- User Registration System ---")
    user = username("Enter new username: ")
    pwd = password("Enter new password: ")
    
    confirm = yes_no("Do you want to save these profile settings?")
    print(f"\n[Result Data] User: {user} | Password Set: {'Yes' if pwd else 'No'} | Saved: {confirm}")
