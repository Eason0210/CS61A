"""Object Orient design:
"""
class Account:
    """An account has a balance and a holder

    """
    interest = 0.02 # A class attribute

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A back account that charges for withdrawals."""
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

# FIXME: TypeError: 'list' object is not callable
class Bank:
    """A bank *has* accounts.

    >>> bank = Bank()
    >>> john = bank.open_account('john', 10)
    >>> jack = bank.open_account('jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True

    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest():
        for a in self.accounts:
            a.deposit(a.balance * a.interest)


    def too_big_to_fail(self):
        return len(self.accounts) > 1
