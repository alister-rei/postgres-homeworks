"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2


# Параметры для подключения к базе данных
USER = "alister"
PASSWORD = "1234"
HOST = "localhost"
DB = "north"

# Путь к файлам с данными
PATH_CUSTOMERS = os.path.join(os.path.dirname(__file__), "north_data", "customers_data.csv")
PATH_EMPLOYEES = os.path.join(os.path.dirname(__file__), "north_data", "employees_data.csv")
PATH_ORDERS = os.path.join(os.path.dirname(__file__), "north_data", "orders_data.csv")

if __name__ == '__main__':
    with open(PATH_CUSTOMERS, 'r', encoding='Windows-1251') as file:
        file_data = csv.DictReader(file)
        with psycopg2.connect(host=HOST, database=DB, user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                for row in file_data:
                    tup = tuple(row.values())
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", tup)

    conn.close()

    with open(PATH_EMPLOYEES, 'r', encoding='Windows-1251') as file:
        file_data = csv.DictReader(file)
        with psycopg2.connect(host=HOST, database=DB, user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                for row in file_data:
                    tup = tuple(row.values())
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", tup)

    conn.close()

    with open(PATH_ORDERS, 'r', encoding='Windows-1251') as file:
        file_data = csv.DictReader(file)
        with psycopg2.connect(host=HOST, database=DB, user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                for row in file_data:
                    tup = tuple(row.values())
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", tup)

    conn.close()
