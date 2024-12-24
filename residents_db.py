import sqlite3

class DataBase():
    def __init__(self):
        self.conn = sqlite3.connect('residents.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute(""" CREATE TABLE if not exists Streets (
    StreetCode INTEGER PRIMARY KEY,
    Name TEXT NOT NULL)""")

        self.cursor.execute(""" CREATE TABLE if not exists Accounts (
    AccountCode INTEGER PRIMARY KEY,
    AccountNumber TEXT NOT NULL,
    StreetCode INTEGER NOT NULL,
    House TEXT NOT NULL,
    Building TEXT,
    Apartment TEXT NOT NULL,
    FullName TEXT NOT NULL,
    FOREIGN KEY (StreetCode) REFERENCES Streets(StreetCode)
) """)
        self.cursor.execute(""" CREATE TABLE if not exists Services (
    ServiceCode INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Tariff REAL NOT NULL
);""")
        self.cursor.execute(""" CREATE TABLE if not exists Accruals (
    AccrualCode INTEGER PRIMARY KEY,
    AccountCode INTEGER NOT NULL,
    ServiceCode INTEGER NOT NULL,
    Quantity REAL NOT NULL,
    FOREIGN KEY (AccountCode) REFERENCES Accounts(AccountCode),
    FOREIGN KEY (ServiceCode) REFERENCES Services(ServiceCode)
);""")

        services = [
            ("Электричество", 5.50),
            ("Водоснабжение", 3.75),
            ("Газоснабжение", 4.20),
            ("Вывоз мусора", 2.00),
            ("Отопление", 6.00)
        ]

        # Вставка данных
        self.cursor.executemany("INSERT or ignore INTO Services (Name, Tariff) VALUES (?, ?)", services)

        self.conn.commit()
        print('таблицы созданы')

    def close_db(self):
        self.cursor.close()
        self.conn.close()




