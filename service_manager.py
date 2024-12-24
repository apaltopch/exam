import pandas as pd
from account import Account
from service import Service
from accrual import  Accrual

class ServiceManager:
    def __init__(self):
        self.accounts = []  # Список лицевых счетов
        self.services = []  # Список услуг
        self.charges = []   # Список начислений

    def add_account(self, account):
        self.accounts.append(account)  # Добавление лицевого счета

    def add_service(self, service):
        self.services.append(service)  # Добавление услуги

    def add_charge(self, charge):
        self.charges.append(charge)  # Добавление начисления

    def generate_invoice(self, account_number):
        # Поиск счета по номеру
        account = next((a for a in self.accounts if a.number == account_number), None)
        if not account:
            return None
        # Логика генерации счета (не была представлена, добавьте свою)
