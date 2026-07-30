class BankAccount:

    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            return True
        return False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Please log in first.")

        if amount <= 0:
            raise Exception("Deposit amount must be positive.")

        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Please log in first.")

        if amount <= 0:
            raise Exception("Withdraw amount must be positive.")

        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")


class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Please log in first.")

        if amount <= 0:
            raise Exception("Withdraw amount must be positive.")

        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: minimum balance would be exceeded.")

        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")


class ATM:

    def __init__(self, account_list, try_limit):

        if not isinstance(account_list, list):
            raise Exception("account_list must be a list.")

        for account in account_list:
            if not isinstance(account, BankAccount):
                raise Exception("All elements must be BankAccount or MinimumBalanceAccount instances.")

        try:
            if try_limit <= 0:
                raise Exception
        except:
            print("Invalid try limit. Setting try_limit to 2.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):

        while True:
            print("\n===== ATM MENU =====")
            print("1. Log in")
            print("2. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)

            elif choice == "2":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

    def log_in(self, username, password):

        for account in self.account_list:
            if account.authenticate(username, password):
                print("Login successful!")
                self.current_tries = 0
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print("Incorrect username or password.")

        if self.current_tries >= self.try_limit:
            print("Maximum number of login attempts reached.")
            exit()

    def show_account_menu(self, account):

        while True:
            print("\n===== ACCOUNT MENU =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Logout")

            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                except Exception as e:
                    print(e)

            elif choice == "2":
                try:
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(e)

            elif choice == "3":
                print(f"Current balance: {account.balance}")

            elif choice == "4":
                account.authenticated = False
                print("Logged out.")
                break

            else:
                print("Invalid choice.")


# ---------------- TEST ---------------- #

account1 = BankAccount(1000, "alice", "1234")
account2 = MinimumBalanceAccount(2000, "bob", "abcd", minimum_balance=500)

accounts = [account1, account2]

atm = ATM(accounts, 3)