username = str(input("enter your username: "))
password = input("enter your password: ")

password = len(password)
hidden_password = '*' * password


print(f'your username is {username} and password is {hidden_password}and your password lenght is {password}')