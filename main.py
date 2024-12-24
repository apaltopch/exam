from street import Street
from account import Account
from service import Service
from accrual import Accrual
from openpyxl import Workbook
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from design import *
from residents_db import *


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.conn = sqlite3.connect("residents.db")
        self.cursor = self.conn.cursor()

        self.db = DataBase()
        self.db.create_tables()
        self.db.close_db()
        self.load_services()
        self.ui.save_pushButton.clicked.connect(self.add_accrual)

    def load_services(self):
        """Load services into the combo box."""
        self.cursor.execute("SELECT Name ||'-'|| Tariff FROM Services")
        services = self.cursor.fetchall()
        for service in services:
            self.ui.services_comboBox.addItem(service[0])

    def add_accrual(self):
        """Add an accrual to the database."""
        street = self.ui.street_lineEdit.text()
        acc_number = self.ui.acc_num_lineEdit.text()
        service = self.ui.services_comboBox.currentText()
        quantity = self.ui.accrual_lineEdit.text()

        if not (street and acc_number and service and quantity):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
            return

        try:
            quantity = float(quantity)
            self.cursor.execute(
                "INSERT INTO Accruals (AccountCode, ServiceCode, Quantity) "
                "SELECT a.AccountCode, s.ServiceCode, ? FROM Accounts a "
                "JOIN Services s ON s.Name = ? WHERE a.AccountNumber = ?",
                (quantity, service, acc_number),
            )
            self.conn.commit()
            QMessageBox.information(self, "Успех", "Начисление добавлено!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {e}")

def generate_payment_notice(account, accruals):
    wb = Workbook()
    ws = wb.active
    ws.title = "Payment Notice"

    ws.append(["Account Number", "Full Name", "Service", "Quantity", "Amount"])
    for accrual in accruals:
        ws.append([
            account.number,
            account.fio,
            accrual.service.name,
            accrual.quantity,
            accrual.calc_amount()
        ])

    filename = f"Payment_Notice_{account.number}.xlsx"
    wb.save(filename)
    print(f"Payment notice saved as {filename}")

def demonstrate_classes():
    # Example data
    street = Street(1, "Main Street")
    account = Account(101, "123456789", street, "10", "A", "5", "John Doe")
    service1 = Service(201, "Electricity", 5.5)
    service2 = Service(202, "Water", 2.0)

    accrual1 = Accrual(301, account, service1, 100)
    accrual2 = Accrual(302, account, service2, 50)

    accruals = [accrual1, accrual2]

    print("Demonstrating class interactions:")
    print(account)
    for accrual in accruals:
        print(accrual)

    generate_payment_notice(account, accruals)

if __name__ == "__main__":
    demonstrate_classes()
    import sys

    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

