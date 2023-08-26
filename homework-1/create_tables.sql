-- SQL-команды для создания таблиц

CREATE TABLE IF NOT EXISTS customers
(
    customer_id VARCHAR(20) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees
(
    employee_id int PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS orders
(
	order_id int PRIMARY KEY,
	customer_id VARCHAR(20) REFERENCES customers(customer_id) ON DELETE CASCADE,
	employee_id int REFERENCES employees(employee_id) ON DELETE CASCADE,
	order_date DATE,
	ship_city VARCHAR(100) NOT NULL
);
