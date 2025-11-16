#Import libraries
import csv
import cowsay
import requests
from pyfiglet import Figlet

#Configurations
f = Figlet(font='speed')
fieldnames = ('username' ,'password', 'currency', 'balance')

response = requests.get('https://api.frankfurter.dev/v1/currencies')
currencies = []

for currency in response.json():
    currencies.append(currency)




#Create Class for a bank balance
class Balance:
    def __init__(self,username):
        with open('database.csv') as file:
            reader = csv.DictReader(file, fieldnames = fieldnames)
            for row in reader:
                if username==row['username']:
                    self.username=row['username']
                    self.password=row['password']
                    self.currency=row['currency']
                    self.balance=float(row['balance'])
                    break
                else:
                    pass

    def deposit(self,n):
        if n.isalpha():
            return('!!!Invalid Amount!!!')
        if not n:
            return('!!!Invalid Amount!!!')
        else:
            self.balance = float(n) + float(self.balance)
            self.balance = float(self.balance)


    def withdraw(self,n):
        if n.isalpha():
            return('!!!Invalid Amount!!!')
        elif not n:
            return('!!!Invalid Amount!!!')

        else:
            self.balance = float(self.balance) - float(n)
            self.balance = float(self.balance)

    def delete_account(self):
        new_data = []
        with open ('database.csv') as file:
            reader = csv.DictReader(file, fieldnames = fieldnames)
            for row in reader:
                if self.username == row['username']:
                    pass
                elif 'username' == row['username']:
                    pass
                else:
                    new_data.append(row)
        with open('database.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()

        with open ('database.csv', 'a') as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)

            for data in new_data:
                writer.writerow(data)

    def update(self):
            new_data = []
            with open ('database.csv') as file:
                    reader = csv.DictReader(file, fieldnames = fieldnames)
                    for row in reader:
                        if self.username == row['username']:
                            row['currency'] = self.currency
                            row['balance'] = round(self.balance,2)
                            new_data.append(row)
                        elif 'username' == row['username']:
                            pass
                        else:
                            new_data.append(row)
            with open('database.csv', 'w') as file:
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                writer.writeheader()

            with open ('database.csv', 'a') as file:
                writer = csv.DictWriter(file,fieldnames=fieldnames)

                for data in new_data:
                    writer.writerow(data)





#Welcome Page
def main():
    print(f.renderText('Welcome to TRAVEL WALLET!'))
    print()
    while True:
        print('Do you wish to open or create an account?')

        x = input('Enter "o" to open, "c" to create:').lower().strip()

        if x == 'o':
            print()
            print('*--------------------------------------*')
            user_name = input("Username: ")
            pass_word = input("Password: ")
            if open_account(user_name,pass_word) == True:
                account = Balance(user_name)
                account_details(account.username,account.currency,account.balance)
                break
            else:
                print('*--------------------------------------*')
                print('Account not found :(')
                print('*--------------------------------------*')
                main()

        elif x == 'c':
            print()
            print('*--------------------------------------*')
            print('Please input the details to create your account')
            print()
            user_name = input("Username: ").strip()
            pass_word = input("Password: ").strip()
            if user_name == 'username' or pass_word == 'password':
                print('!!!Invalid Username and Password!!!!')
                main()
            elif not user_name or not pass_word:
                print('!!!Invalid Username and Password!!!!')
                main()
            with open('database.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if user_name == row['username'] or pass_word == row['password']:
                        print('!!!Username or Password already exists!!!')
                        main()
            print()
            print('Available Currency Codes:')
            print('*----------------------------------------------------------------------------------------------------------------------------*')
            print(*currencies)
            print('*----------------------------------------------------------------------------------------------------------------------------*')
            print()
            currency = input("Select a currency: ").strip().upper()
            if currency not in currencies:
                print('!!!Invalid Currency!!!')
                main()
            balance = input("How much is your balance: ")
            if balance.isalpha():
                print('!!!Invalid Balance!!!')
                main()
            else:
                print()
                print('*--------------------------------------*')
                print('Account successfully made! :)')
                print(create_account(user_name,pass_word,currency,balance))
                print('*--------------------------------------*')
                print()
                pass

        else:
            print()
            print('*--------------------------------------*')
            print('!!!Invalid input, please try again!!!')
            print('*--------------------------------------*')
            print()
            pass

#Create an account(test)
def create_account(user_name,pass_word,currency,balance):
    with open ('database.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writerow({'username': user_name, 'password':pass_word, 'currency':currency, 'balance':round(float(balance),2)})
        return(f'Username:{user_name}, Password:{pass_word}, Currency:{currency}, Balance:{round(float(balance),2)}')




#Open an account(test)
def open_account(user_name,pass_word):
        ValidAccount = False
        with open ('database.csv') as file:
            reader = csv.DictReader(file, fieldnames = fieldnames)
            for row in reader:
                if user_name == row['username'] and pass_word == row['password']:
                    ValidAccount = True
                    return True
                else:
                    pass

        if ValidAccount == False:
            return False



#Show account page
def account_details(x,y,z):
    print()
    print('*--------------------------------------*')
    print(f.renderText('Your Account'))
    print('*--------------------------------------*')
    print()
    cowsay.cow(f'Welcome, {x}! Your account balance is {y} {round(float(z),2)}!')

    while True:
        commands = ['E', 'D', 'A', 'W', 'C']
        print()
        print('What do you want to do?')
        print('*--------------------------------------*')
        print('[E] to EXIT your account')
        print('[D] to DELETE your account')
        print('[A] to DEPOSIT an amount')
        print('[W] to WITHDRAW an amount')
        print('[C] to CHANGE your currency')
        print('*--------------------------------------*')
        print()
        command = input('Type your command: ').upper().strip()

        if command in commands:
            if command == 'E':
                main()
                break
            if command == 'D':
                delete = input('Are you sure you wish to delete your account? [Y/N]: ').upper()
                if delete == 'Y':
                    print('*--------------------------------------*')
                    print(delete_account(x))
                    print('*--------------------------------------*')
                    main()
                    break
                elif delete == 'N':
                    print('*--------------------------------------*')
                    print('Deletion Cancelled')
                    print('*--------------------------------------*')
                else:
                    print('!!!Invalid Command!!!')
            if command == 'A':
                balance = Balance(x)
                n = input('How much will you like to deposit? ')
                print()
                balance.deposit(n)
                balance.update()
                print('*--------------------------------------*')
                print(f'Your new balance is {balance.currency} {round(balance.balance,2)}!')
                print('*--------------------------------------*')
                print()
                pass
            if command == 'W':
                balance = Balance(x)
                n = input('How much will you like to withdraw? ')
                print()
                balance.withdraw(n)
                if balance.balance < 0:
                    print('*--------------------------------------*')
                    print('!!!You are withdrawing more than your current balance!!!')
                    print('*--------------------------------------*')
                else:
                    balance.update()
                    print('*--------------------------------------*')
                    print(f'Your new balance is {balance.currency} {round(balance.balance,2)}!')
                    print('*--------------------------------------*')
                    print()
                pass
            if command == 'C':
                print('Currencies available:')
                print('*----------------------------------------------------------------------------------------------------------------------------*')
                print(*currencies)
                print('*----------------------------------------------------------------------------------------------------------------------------*')
                c = input('What currency will you like to convert to? ').upper().strip()
                if c not in currencies:
                    print('!!!Invalid Currency!!!')
                    pass
                else:
                    print()
                    print('*--------------------------------------*')
                    print(change_currency(x,c))
                    print('*--------------------------------------*')
                    print()
                    pass

        else:
            print('!!!Invalid Command!!!')
            pass

#Delete account feature(test)
def delete_account(x):
        balance = Balance(x)
        balance.delete_account()
        return("Account successfully deleted!")


#Change currency using Frankfurter API
def change_currency(username,c):
    new_currency = c
    account = Balance(username)
    old_currency = account.currency
    balance = account.balance

    if old_currency == new_currency:
        return('!!!Your current currency is the same as the new currency!!!')

    response = requests.get(f'https://api.frankfurter.dev/v1/latest?base={old_currency}&symbols={new_currency}')
    content = response.json()['rates']
    if new_currency in currencies:
        m=(content[new_currency])
    else:
        return('!!!Invalid currency!!!')

    new_balance = balance*m

    account.currency = new_currency
    account.balance = new_balance
    account.update()
    return(f'Your new balance is {account.currency} {round(account.balance,2)}!')








#Start
if __name__ == "__main__":
    main()
