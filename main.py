logins = []
with open('plain_text.txt', 'r') as file:
    datalog = file.readlines()
for login in datalog:
    logins.append(login.strip('\n'))

def login():
    iuser = input('Username? ')
    ipass = input('Password? ')
    ilog = f'{iuser},{ipass}'
    for login in logins:
        if ilog == login:
            return True
    else:
        print('Wrong username or password, try again')
        selection()

def register():
    while True:
        nuser = input('New username? ')
        npass = input('New password? ')
        nlog = f'{nuser},{npass}'
        if len(npass) < 4:
            print('Password must be minimum 4 characters')
        else:
            with open('plain_text.txt', 'a') as file:
                file.write(f'{nlog}\n')
            print('Registered successfully')
            break

def menu():
    while True:
        print('Logged in successfully\n')
        print(f'1. Change password\n2. Logout\n')
        try:
            select = int(input('Choice? '))
            if select == 1:
                passwordchange()
            if select == 2:
                print('\nLogging out')
                break
        except (ValueError, UnboundLocalError):
            print('Please enter a valid option')

def passwordchange():
    while True:
        nuser = input('Username? ')
        npass = input('New password? ')
        nlog = f'{nuser},{npass}'
        if len(npass) < 4:
            print('Password must be minimum 4 characters')
        else:
            with open('plain_text.txt', 'a') as file:
                file.write(f'{nlog}\n')
            print('Password changed successfully')
            break

def selection():
    while True:
        print(f'\n1. Login\n2. Register\n3. Quit\n')
        try:
            select = int(input('Choice? '))
            if select == 1:
                mybool = bool(login())
                if mybool == True:
                    return True
            if select == 2:
                register()
            if select == 3:
                print('\nQuitting')
                return False
        except (ValueError, UnboundLocalError):
            print('Please enter a valid option\n')

def main():
    mybool = bool(selection())
    if mybool == True:
        menu()
    if mybool == False:
        quit

main()