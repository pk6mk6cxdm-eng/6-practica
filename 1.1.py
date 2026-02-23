class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Бастапқы баланс теріс болмауы керек!")
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма 0-ден үлкен болуы керек!")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError("Қаражат жеткіліксіз!")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, balance):
        if owner in self.accounts:
            print("Бұл атпен шот бар!")
            return

        account = BankAccount(owner, balance)
        self.accounts[owner] = account
        print(f"{owner} шоты құрылды.")

    def get_account(self, owner):
        return self.accounts.get(owner)

    def close_account_if_zero(self, owner):
        account = self.accounts.get(owner)
        if account and account.get_balance() == 0:
            print("Баланс 0-ге жетті. Шот жабылды.")
            del self.accounts[owner]

bank = Bank()

while True:
    owner = input("Шот иесін енгізіңіз (stop - тоқтату): ")

    if owner.lower() == "stop":
        break

    account = bank.get_account(owner)

    if not account:
        try:
            balance = float(input("Бастапқы баланс: "))
            bank.create_account(owner, balance)
            account = bank.get_account(owner)
        except ValueError as e:
            print("Қате:", e)
            continue

    while account and account.get_balance() > 0:
        print("Баланс:", account.get_balance())
        choice = input("1 - салу, 2 - алу, stop - шығу: ")

        if choice == "stop":
            break

        try:
            amount = float(input("Сумма: "))

            if choice == "1":
                account.deposit(amount)

            elif choice == "2":
                account.withdraw(amount)

            else:
                print("Белгісіз операция!")
                continue

            bank.close_account_if_zero(owner)

        except Exception as e:
            print("Қате:", e)