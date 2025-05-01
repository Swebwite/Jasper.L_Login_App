## importing data from database
logins = []
try:
    with open('plain_text.txt', 'r') as file:
        datalog = file.readlines()
    for login in datalog:
        logins.append(login.strip('\n'))
except FileNotFoundError:
    print('Error: User data file not found.')
    quit()

def login():
    ## login sequence for an existing user
    global iuser
    iuser = input('Username? ')
    ipass = input('Password? ')
    ilog = f'{iuser},{ipass}'
    for login in logins:
        if ilog == login:
            print('Logged in successfully\n')
            return True
    else:
        print('Wrong username or password, try again')
        selection()

def register():
    ## registering a new user to database
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
    ## menu and selection for a logged in user
    while True:
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
    ## changes the password of the currently logged in user
    nuser = iuser
    npass = input('New password? ')
    if len(npass) < 4:
        print('Password must be minimum 4 characters')
        return
    with open('plain_text.txt', 'r') as file:
        lines = file.readlines()
    with open('plain_text.txt', 'w') as file:
        for line in lines:
            user, _ = line.strip().split(',')
            if user == nuser:
                file.write(f'{nuser},{npass}\n')
            else:
                file.write(line)
    print('Password changed successfully\n')

def selection():
    ## main menu where user selects actions
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
                return False
        except (ValueError, UnboundLocalError):
            print('Please enter a valid option\n')

def main():
    ## starts the functions and quits
    mybool = bool(selection())
    if mybool == True:
        menu()
    if mybool == False:
        print('\nQuitting')
        quit()

main()