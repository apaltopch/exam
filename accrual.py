"""для работы с таблицей начислений"""

class Accrual:
    def __init__(self, accrual_code, account, service, quantity):
        self.accrual_code = accrual_code
        self.account = account
        self.service = service
        self.quantity = quantity

    def calc_amount(self):
        return self.quantity * self.service.tarif

    def __str__(self):
        return (f"Accrual {self.accrual_code}: {self.quantity} x {self.service.name} "
                f"= {self.calc_amount()} for Account {self.account.number}")
