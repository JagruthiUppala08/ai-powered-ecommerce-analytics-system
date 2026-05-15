SELECT COUNT(*) AS total_products
FROM products;
SELECT
product_category_name,
COUNT(*) AS total_products
FROM products
GROUP BY product_category_name
ORDER BY total_products DESC
LIMIT 10;
SELECT ROUND(AVG(product_weight_g)::numeric, 2) AS avg_product_weight
FROM products;