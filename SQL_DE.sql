-- 1. SELECT, WHERE, DISTINCT, ORDER BY, LIMIT

SELECT
    customer_id,
    customer_name,
    city
FROM customers;

SELECT
    customer_id,
    customer_name,
    city
FROM customers
WHERE city = 'Atlanta';

SELECT DISTINCT
    city
FROM customers;

SELECT
    customer_id,
    customer_name,
    city
FROM customers
ORDER BY customer_name ASC;

SELECT
    customer_id,
    customer_name,
    city
FROM customers
ORDER BY customer_id DESC
LIMIT 5;

-- 2. INNER JOIN

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;

-- 3. LEFT JOIN

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;

-- 4. RIGHT JOIN

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id;

-- 5. FULL OUTER JOIN

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id
FROM customers c
FULL OUTER JOIN orders o
    ON c.customer_id = o.customer_id;

-- 6. SELF JOIN

SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id;

-- 7. GROUP BY, HAVING, Aggregate Functions, Aliasing

SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(order_amount) AS total_sales,
    AVG(order_amount) AS avg_order_value,
    MAX(order_amount) AS highest_order,
    MIN(order_amount) AS lowest_order
FROM orders
GROUP BY customer_id;

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 2;

-- 8. NULL Handling

SELECT
    customer_id,
    customer_name,
    COALESCE(phone_number, 'Not Available') AS phone_number
FROM customers;

SELECT
    customer_id,
    customer_name
FROM customers
WHERE phone_number IS NULL;

SELECT
    customer_id,
    customer_name
FROM customers
WHERE phone_number IS NOT NULL;

-- 9. CASE Statement

SELECT
    order_id,
    order_amount,
    CASE
        WHEN order_amount >= 1000 THEN 'High Value'
        WHEN order_amount >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_category
FROM orders;

-- 10. Basic Data Cleansing in SQL

SELECT
    customer_id,
    TRIM(customer_name) AS customer_name,
    LOWER(email) AS email,
    UPPER(city) AS city,
    COALESCE(phone_number, 'Not Available') AS phone_number
FROM customers;

-- 11. Primary Key and Foreign Key

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 12. Relationship Awareness Example

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;

---Hands on Tasks
---Write a report to show daily sales, top customers, and product category performance.

SELECT
    order_date,
    SUM(order_amount) AS total_sales,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY order_date
ORDER BY order_date;

-- Top Customers
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.order_amount) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- Category Performance
SELECT
    p.category,
    SUM(o.order_amount) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

---Join orders, customers, and products tables to create a business-ready report.

SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    p.product_name,
    p.category,
    o.quantity,
    o.order_amount
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id;

--Compare raw row counts with filtered row counts for data sanity checking.

SELECT
    COUNT(*) AS total_rows,
    COUNT(CASE WHEN order_amount > 0 THEN 1 END) AS valid_rows,
    COUNT(CASE WHEN order_amount <= 0 OR order_amount IS NULL THEN 1 END) AS invalid_rows
FROM orders;

---Build a daily SQL reporting dataset showing total orders, revenue, returned orders, and average order value by region using customers, orders, payments, and returns tables.


SELECT
    o.order_date,
    c.region,

    COUNT(DISTINCT o.order_id) AS total_orders,

    SUM(p.payment_amount) AS total_revenue,

    COUNT(DISTINCT r.order_id) AS returned_orders,

    ROUND(
        SUM(p.payment_amount) / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value

FROM orders o

JOIN customers c
    ON o.customer_id = c.customer_id

LEFT JOIN payments p
    ON o.order_id = p.order_id

LEFT JOIN returns r
    ON o.order_id = r.order_id

WHERE o.order_date = CURRENT_DATE

GROUP BY
    o.order_date,
    c.region

ORDER BY
    c.region;