username = input('Enter your username: ')
password = input('Enter your password: ')

password_length = len(password)
hidden_password = '*' * password_length

print(f'Hello {username}. Your password {hidden_password} is {password_length} letters long ')