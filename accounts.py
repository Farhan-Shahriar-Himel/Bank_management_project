from datetime import datetime

class Bank:
    def __init__(self, name, short_name, address, investment) -> None:
        self.name = name
        self.address = address
        self.balance = investment
        self.short_name = short_name
        self.total_loan = 0
        self.loan_feature = True
        self.sv_accounts = dict()
        self.cur_accounts = dict()
        self.__bankrupt = False
        self.__admin = None
        self.sv_counter = 0
        self.cur_counter = 0

    def add_admin(self, admin):
        self.__admin = admin

    @property
    def bankrupt(self):
        return self.__bankrupt
    
    @bankrupt.setter
    def bankrupt(self, truthy):
        self.__bankrupt = truthy

    def create_account(self, name, email, password, category, deposit):
        sort_num = None
        if category == "SV":
            sort_num = str(self.sv_counter + 1)
        else:
            sort_num = str(self.cur_counter + 1)
        
        while len(sort_num) < 4:
            sort_num = '0' + sort_num
        
        acc_number = self.short_name + category + sort_num

        new_acc = Account(name, email, password, category, deposit, self)
        self.balance += deposit
        if category == "SV":
            self.sv_accounts[acc_number] = new_acc
            self.sv_counter += 1
        else:
            self.cur_accounts[acc_number] = new_acc
            self.cur_counter += 1

    def delete_account(self, acc_number):
        if acc_number in self.sv_accounts:
            del self.sv_accounts[acc_number]
        elif acc_number in self.cur_accounts:
            del self.cur_accounts[acc_number]
        else:
            print("The account number is not correct\n")
            return
        print("Account has been deleted\n")

    def logIN(self, email, password):
        return password == self.__admin._password
    
    def off_the_loan(self):
        self.loan_feature = False

    def on_the_loan(self):
        self.loan_feature = True
    
    def show_all_user(self):
        print()
        print("-----------------------All Savings Account--")
        for key, value in self.sv_accounts.items():
            print(f"Name : {value.name}; email: {value.email}; Account Number: {key}")
        
        print()
        print("--All Current Account------------------------")
        for key, value in self.cur_accounts.items():
            print(f"Name : {value.name}; email: {value.email}; Account Number: {key}")
        print()


class Account:
    def __init__(self, name, email, password, category, balance, bank, loan=0) -> None:
        self.name = name
        self.email = email
        self.category = category
        self.balance = balance
        self.loan = 0
        self.password = password
        self.history = []
        self.bank = bank
        self.ln_cnt = 0
    
    def deposit(self, amount):
        if self.bank.bankrupt:
            print("The Bank is bankrupt")
            return
        self.balance += amount
        self.bank.balance += amount
        print("Successfully deposited")
        
        self.history.append(f"Deposited {amount}$")
    
    def withdraw(self, amount):
        if self.bank.bankrupt:
            print("The Bank is bankrupt")
            return False
        if self.category == "SV":
            if amount < self.balance:
                self.balance -= amount
                self.bank.balance -= amount
                
                self.history.append(f"withdrew {amount}$")
                return True
            else:
                print("Account balance exceed")
                return False
        else:
            if amount <= self.balance:
                self.balance -= amount
            else:
                self.loan += amount - self.balance
                self.balance = 0
            self.bank.balance -= amount
            
            self.history.append(f"withdrew {amount}$")
            return True
    
    def apply_loan(self, amount):
        if self.bank.bankrupt:
            print("The Bank is bankrupt")
            return  False
        if not self.bank.loan_feature:
            print("Bank Can not give you loan right now")
            return False
        if self.ln_cnt < 2 and amount < self.bank.balance:
            self.loan += amount
            self.bank.total_loan += amount
            self.bank.balance -= amount
            self.balance += amount
            self.ln_cnt += 1
            today = datetime.now
            self.history.append(f"applied for loan for {amount}$")
            return True
        else:
            print("Sorry we can't give you the loan")
            return False

    def log_In(self, password):
        return password == self.password
    
    def transfer(self, amount, acc_number):
        if self.bank.bankrupt:
            print("The Bank is bankrupt")
            return False
        if amount > 0 and self.balance - amount > 100:
            self.balance -= amount
            if acc_number in self.bank.sv_accounts:
                self.bank.sv_accounts[acc_number].balance += amount
                
                self.history.append(f"transfer {amount}$ from your account to {acc_number}")
                return True
            elif acc_number in self.bank.cur_accounts:
                self.bank.cur_accounts[acc_number].balance += amount 
                
                self.history.append(f"transfer {amount}$ from your account to {acc_number}")
                return True
            else:
                self.balance += amount
                print("Invalid Account")
                return False
        else:
            print("Balance Can not be transferred")
            return False
        
    def pay_the_loan(self, amount):
        print()
        if amount <= 0:
            print("You have given an invalid amount.\n")
            return
        
        if amount <= self.loan:
            self.loan -= amount
            self.bank.total_loan -= amount
            self.bank.balance += amount
            self.history.append(f"Loan has been decreased by {amount}$")
            print("The loan amount has been decreased")
            print()
        else:
            self.bank.total_loan -= self.loan
            self.loan = 0
            self.balance += self.loan - amount
            self.bank.balance += amount
            
            self.history.append(f"Loan has been cleared and extra amount has been added in bank balance")
            print("You have submitted a larger cash then your loan. Rest of the cash added to your bank balance. \nThank You")
            print()

        
    def show_details(self):
        print()
        print(f"Name: {self.name}, Email: {self.email}, passwod: {self.password}, balance: {self.balance}, loan: {self.loan}")
        print()

    def show_transaction_history(self):
        print()
        for el in self.history[::-1]:
            print(el)
        print()
    

class Admin():
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self._password = password
    