username = input('Enter your username')

password = input('Enter your password')

password_lenght = len(password)
hidden_password = '*' * password_lenght

print(f '{username}, your password, {hidden_password}, is {password_lenght} characters long')
