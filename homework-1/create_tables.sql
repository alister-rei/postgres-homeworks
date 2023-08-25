-- SQL-команды для создания таблиц

CREATE TABLE customers
(
    customer_id VARCHAR(20) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id VARCHAR(20) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date DATE,
	ship_city VARCHAR(100) NOT NULL
);
