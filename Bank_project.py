from accounts import *


def menu():
    print("Press 1. to deposit amount")
    print("Press 2. to withdrew amount")
    print("Press 3. to transfer money")
    print("Press 4. to see All details")
    print("Press 5. to See transaction history")
    print("Press 6. to apply loan")
    print("Press 7. to pay the loan.")
    print("Press 8. to log out")


manager = Admin("Phitron", "phitron@gmail.com", "1234")
SonaliBank = Bank("Sonali Bank", "SBL", "dhaka/1212", 100000000)
SonaliBank.add_admin(manager)

while True:
    print("Press 1. Admin log in")
    print("Press 2. For User Log in")
    print("Press 3. To exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        email = input("Enter your Email:(phitron@gmail.com) ")
        password = input("Enter your password:(1234) ")
        if SonaliBank.logIN(email, password):
            while True:
                print("Press 1. To Create an account")
                print("Press 2. to Delete an account")
                print("Press 3. to See All user account list")
                print("Press 4. to check total Available balance of the Bank")
                print("Press 5. to check the total loan amount of the Bank")
                print("Press 6. to Off the loan feature")
                print("Press 7. to on the loan feature")
                print("Press 8. to bankrupt the bank.")
                print("Press 9. to log out")
                option = input("Enter your choice: ")
                print()
                if option == '1':
                    name = input("Enter your name: ")
                    email = input("Enter your email: ")
                    password = input("Enter a password: ")
                    category = input("Which type of account you want SV/CR: ")
                    deposit = int(input("Enter a amount to deposit: "))
                    category = category.upper()
                    SonaliBank.create_account(name, email, password, category, deposit)
                    print()
                    print("Account has been created please log in.")
                    print()

                if option == '2':
                    ac_number = input("Enter account number you want to delete: ")
                    SonaliBank.delete_account(ac_number)
                    print()

                if option == '3':
                    SonaliBank.show_all_user()
                    print()

                if option == '4':
                    print()
                    print("The remaining balance is", SonaliBank.balance)
                    print()

                if option == '5':
                    print()
                    print("The total loan amount is", SonaliBank.total_loan)
                    print()

                if option == '6':
                    print()
                    SonaliBank.off_the_loan()
                    print("The loan system has bee turned off")
                    print()

                if option == '7':
                    print()
                    SonaliBank.on_the_loan()
                    print("The loan system has been turned on")
                    print()

                if option == '8':
                    print()
                    SonaliBank.bankrupt = True
                    print("The bank is bankrupted")
                    print()

                if option == '9':
                    break
        else:
            print("Wrong Password")

    elif choice == '2':
        print()
        ac_number = input("Enter your bank account number: ")
        password = input("Enter your password: ")
        print()

        if ac_number in SonaliBank.sv_accounts:
            if SonaliBank.sv_accounts[ac_number].log_In(password):
                while True:
                    menu()
                    option = input("Enter your choice: ")

                    if option == '1':
                        print()
                        amount = int(input("Enter your amount: "))
                        SonaliBank.sv_accounts[ac_number].deposit(amount)
                        print()
                        continue

                    if option == '2':
                        print()
                        amount = int(input("Enter your amount: "))
                        ok = SonaliBank.sv_accounts[ac_number].withdraw(amount)
                        if ok:
                            print("withdrew done successfully")
                        print()

                    if option == '3':
                        print()
                        receiver = input("Enter receiver account number: ")
                        amount = int(input("Enter your amount: "))
                        ok = SonaliBank.sv_accounts[ac_number].transfer(amount, receiver)
                        if ok: 
                            print("Successfully transferred")
                        print()

                    if option == '4':
                        print()
                        SonaliBank.sv_accounts[ac_number].show_details()
                        print()

                    if option == '5':
                        print()
                        SonaliBank.sv_accounts[ac_number].show_transaction_history()
                        print()

                    if option == '6':
                        print()
                        amount = int(input("Enter your amount: "))
                        ok = SonaliBank.sv_accounts[ac_number].apply_loan(amount)
                        if ok:
                            print("You have collected the loan.")
                        print()

                    if option == '7':
                        amount = int(input("Enter your amount: "))
                        SonaliBank.sv_accounts[ac_number].pay_the_loan(amount)
                    
                    elif option == '8':
                        break
            else:
                print()
                print("Wrong password")
                print()

        elif ac_number in SonaliBank.cur_accounts:
            if SonaliBank.cur_accounts[ac_number].log_In(password):
                while True:
                    menu()
                    option = input("Enter your choice: ")

                    if option == '1':
                        print()
                        amount = int(input("Enter your amount: "))
                        SonaliBank.cur_accounts[ac_number].deposit(amount)
                        print()

                    if option == '2':
                        print()
                        amount = int(input("Enter your amount: "))
                        ok = SonaliBank.cur_accounts[ac_number].withdraw(amount)
                        if ok:
                            print("Withdrew done successfully")
                        print()

                    if option == '3':
                        print()
                        receiver = input("Enter receiver account number: ")
                        amount = int(input("Enter your amount: "))
                        ok = SonaliBank.cur_accounts[ac_number].transfer(amount, receiver)
                        if ok: 
                            print("Successfully transferred")
                        print()

                    if option == '4':
                        print()
                        SonaliBank.cur_accounts[ac_number].show_details()
                        print()

                    if option == '5':
                        print()
                        SonaliBank.cur_accounts[ac_number].show_transaction_history()
                        print()

                    if option == '6':
                        print()
                        amount = int(input("Enter your amount: "))
                        ok = SonaliBank.cur_accounts[ac_number].apply_loan(amount)
                        if ok:
                            print("You have collected the loan")
                        print()
                    
                    if option == '7':
                        amount = int("Enter your amount: ")
                        SonaliBank.cur_accounts[ac_number].pay_the_loan(amount)

                    elif option == '8':
                        break
            else:
                print()
                print("Wrong password")
                print()
    else:
        break
