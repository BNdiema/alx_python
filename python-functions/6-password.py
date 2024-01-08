#!/usr/bin/python3

#Password Validation Function

def validate_password(password):
    if len (password) >= 8:
        return(True)
    
    got_upper = False
    got_lower = False
    got_digit = False

    for char in password:
        if char.isupper():
            got_upper = True
        elif char.islower():
            got_lower = True
        elif char.isdigit():
            got_digit = True
        if not (got_upper and got_lower and got_digit):
            return(False)
        
        empty = (' ')
        
    if empty in password:
        return(False)
    
    return(True)

    
