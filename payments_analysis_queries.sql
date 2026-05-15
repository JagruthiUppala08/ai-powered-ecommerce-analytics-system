SELECT COUNT(*) AS total_transactions
FROM payments;
SELECT ROUND(SUM(payment_value), 2) AS total_revenue
FROM payments;
SELECT ROUND(AVG(payment_value), 2) AS avg_payment_value
FROM payments;
SELECT
payment_type,
COUNT(*) AS total_transactions
FROM payments
GROUP BY payment_type
ORDER BY total_transactions DESC;
SELECT
payment_installments,
COUNT(*) AS total_orders
FROM payments
GROUP BY payment_installments
ORDER BY total_orders DESC
LIMIT 10;