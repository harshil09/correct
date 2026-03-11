from abc import ABC, abstractmethod


class Banking(ABC):
    """
    Simple base class for banking accounts.
    """

    def __init__(self, balance: int):
        # Encapsulated balance
        self.__balance = int(balance)

    @property
    def balance(self) -> int:
        """Return the current balance."""
        return self.__balance

    def update_balance(self, amount: int) -> None:
        """Increase the balance by `amount`."""
        self.__balance += int(amount)

    def withdraw_balance(self, amount: int) -> None:
        """Decrease the balance by `amount`."""
        self.__balance -= int(amount)

    @abstractmethod
    def deposit(self, amount: int) -> str:
        """Deposit `amount` and return a status message."""
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, amount: int, *args, **kwargs) -> str:
        """Withdraw `amount` and return a status message."""
        raise NotImplementedError


class SavingsAccount(Banking):
    """Savings account implementation."""

    def deposit(self, amount: int) -> str:
        if amount > 0:
            self.update_balance(amount)
            return f"Amount deposited is {amount}"

        return "invalid deposit amount"

    def withdraw(self, amount: int) -> str:
        if amount <= 0:
            return "invalid withdraw amount"

        if amount > self.balance:
            return f"Insufficient funds. Your balance is {self.balance}"

        self.withdraw_balance(amount)
        return f"Withdrawn amount is {amount}"


class CheckingAccount(Banking):
    def __init__(self, balance: int, overdraft_limit: int = 30000, overdraft_fee: int = 100):
        super().__init__(balance)
        # Total overdraft facility and remaining available overdraft
        self.overdraft_limit = int(overdraft_limit)
        self.overdraft_remaining = int(overdraft_limit)
        self.overdraft_fee = int(overdraft_fee)

    def deposit(self, amount: int) -> str:
        if amount > 0:
            self.update_balance(amount)
            return f"Amount deposited is {amount} and new balance is {self.balance}"

        return "invalid deposit amount"

    def withdraw(self, amount: int, confirm_overdraft: bool = False) -> str:
        """
        Withdraw money from a checking account.

        - If `amount` is less than or equal to the current balance, a normal withdrawal
          is performed.
        - If `amount` is greater than the balance, an overdraft withdrawal is attempted.
          In that case an overdraft fee is charged and the extra amount (plus fee) is
          taken from the overdraft facility. The account balance will **not** go
          negative; instead the overdraft limit is reduced.
        """
        if amount <= 0:
            return "invalid withdraw amount"

        # Normal withdrawal (no overdraft)
        if amount <= self.balance:
            self.withdraw_balance(amount)
            return f"Withdrawn amount is {amount} and new balance is {self.balance}"

        # Potential overdraft: amount exceeds current balance
        shortfall = amount - self.balance

        # Total that will be taken from overdraft (shortfall + fee)
        total_from_overdraft = shortfall + self.overdraft_fee

        # Check if overdraft facility is sufficient
        if total_from_overdraft > self.overdraft_remaining:
            # Maximum amount that can be withdrawn while respecting overdraft_remaining
            max_overdraft_part = max(0, self.overdraft_remaining - self.overdraft_fee)
            max_withdrawable = self.balance + max_overdraft_part
            return (
                f"Overdraft limit exceeded. You can withdraw up to {max_withdrawable} "
                f"(including an overdraft fee of {self.overdraft_fee})."
            )

        # If not yet confirmed, only show what will happen
        if not confirm_overdraft:
            new_overdraft = self.overdraft_remaining - total_from_overdraft
            return (
                f"You are attempting to withdraw {amount} with a balance of {self.balance}. "
                f"This will use your overdraft facility, charge a fee of {self.overdraft_fee}, "
                f"and the extra amount plus fee will be deducted from your overdraft limit of {self.overdraft_limit}. "
                f"Your new available overdraft will be {new_overdraft}, and your account balance will not go negative. "
                f"Please confirm to proceed."
            )

        # Apply withdrawal: use full balance first, rest from overdraft
        amount_from_balance = min(amount, self.balance)
        if amount_from_balance > 0:
            self.withdraw_balance(amount_from_balance)

        self.overdraft_remaining -= total_from_overdraft

        return (
            f"Withdrawn amount is {amount}. Overdraft fee charged is {self.overdraft_fee}. "
            f"New balance is {self.balance} and remaining overdraft limit is {self.overdraft_remaining}."
        )