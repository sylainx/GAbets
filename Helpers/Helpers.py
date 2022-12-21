import bcrypt
from datetime import date
import re

class Helpers:

    
    def __init__(self):
        # TODO:
        pass

    def hash_password(self, password: str):
        # PASSWORD IS ENCODE to BYTE before hashed
        # RESULT is DECODE to store in DB

        # password must be convert firstly in str and utf-8 after
        password = str(password)
        b = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(b, bcrypt.gensalt())

        return hashed_password.decode('utf-8')

    # end hash_password

    def verify_password(self, pwd: str, hashed_pwd: str):
        # TODO not correct

        # Taking user entered password
        user_password = str(pwd)

        # encoding user password
        user_bytes = user_password.encode('utf-8')
        hashed_pwd = hashed_pwd.encode('utf-8')

        # checking password
        result = bcrypt.checkpw(user_bytes, hashed_pwd)

        return result

    
    def get_day(self,):
        return date.today()

    
    
    # Define a function for validating an Email
    def check_email(self,email:str):
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if(re.fullmatch(regex_email, email)):
            return True    
        else:
            return False
    
    def is_validate(self,val):
        if val:
            return True
        return False
   
    def validate_password(self,pwd):
        MIN_PWD=4
        MAX_PWD=30

        if len(pwd) >= MIN_PWD and len(pwd) <= MAX_PWD and pwd.isalpha():
            return True
        
        return False