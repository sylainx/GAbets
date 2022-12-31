import bcrypt


# def hash_password(password):
#     # PASSWORD IS ENCODE to BYTE before hashed
#     # RESULT is DECODE to store in DB
    
#     # password must be convert firstly in str and utf-8 after
#     password = str(password)
#     b = password.encode('utf-8')
#     hashed_password = bcrypt.hashpw(b, bcrypt.gensalt())

#     return hashed_password.decode('utf-8')


def verify_password( pwd: str, hashed_pwd: str):
    # TODO not correct

    # Taking user entered password
    user_password = str(pwd)

    # encoding user password
    user_bytes = user_password.encode('utf-8')
    print(f"pwd: {hashed_pwd}")
    if not isinstance(hashed_pwd, bytes):
        hashed_pwd = hashed_pwd.encode('utf-8')
    
    # checking password
    result = bcrypt.checkpw(user_bytes, hashed_pwd)

    return result

print(verify_password("1234","$2b$12$mjUuVJn1Z7n3VjmtKYIoQOwLw6MM782YyAI9qJJIORxuuinwZ6pxm"))
