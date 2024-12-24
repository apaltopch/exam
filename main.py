from service_manager import ServiceManager
from models.account import Account
from models.service import Service
from models.charge import Charge

def main():
    # Создаем экземпляр ServiceManager для управления
    manager = ServiceManager()

    # Создаем услуги и их тариф
    service1 = Service(1, "Водоснабжение", 100)
    service2 = Service(2, "Электроснабжение", 150)

    manager.add_service(service1)
    manager.add_service(service2)

    # Создаем лицевые счета
    account1 = Account(1, "001", 1, "12", "", "45", "Иванов Иван Иванович")
    account2 = Account(2, "002", 1, "12", "", "46", "Петров Петр Петрович")

    manager.add_account(account1)
    manager.add_account(account2)

    # Создаем начисления
    charge1 = Charge(1, 1, 1, 5)  # 5 кубов воды
    charge2 = Charge(2, 1, 2, 10)  # 10 кВт электроэнергии

    manager.add_charge(charge1)
    manager.add_charge(charge2)

    invoice_df = manager.generate_invoice("001") # Генерация извещения для лицевого счета 001
    if invoice_df is not None:
        # Сохранение извещения в Excel
        manager.save_invoice_to_excel(invoice_df, "invoice_001.xlsx")
        print("Извещение успешно сохранено в invoice_001.xlsx")
    else:
        print("Счет не найден")

if __name__ == "__main__":
    main()
