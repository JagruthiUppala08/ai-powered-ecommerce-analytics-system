SELECT 
EXTRACT(MONTH FROM order_purchase_timestamp) AS month,
COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;