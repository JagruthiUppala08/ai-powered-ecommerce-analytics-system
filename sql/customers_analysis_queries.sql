SELECT COUNT(*) AS total_customers
FROM customers;
SELECT
customer_state,
COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;
SELECT
customer_city,
COUNT(*) AS total_customers
FROM customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 10;
SELECT COUNT(DISTINCT customer_unique_id) AS unique_customers
FROM customers;