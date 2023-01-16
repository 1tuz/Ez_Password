import secrets

password_length = int(input("Type lenght of the password : "))
print(secrets.token_urlsafe(password_length))
