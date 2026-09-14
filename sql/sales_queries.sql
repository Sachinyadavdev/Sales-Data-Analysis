-- Sales Analysis Queries

-- 1. Total Revenue
-- Calculates the sum of all sales across the dataset
SELECT SUM(sales_amount) AS total_revenue 
FROM sales;

-- 2. Total Orders
-- Counts the number of unique orders
SELECT COUNT(DISTINCT order_id) AS total_orders 
FROM sales;

-- 3. Revenue by Product
-- Groups sales by product and sorts them from highest to lowest revenue
SELECT product, SUM(sales_amount) AS revenue 
FROM sales 
GROUP BY product 
ORDER BY revenue DESC;

-- 4. Revenue by Region
-- Aggregates total sales for each region to find the best performing region
SELECT region, SUM(sales_amount) AS revenue 
FROM sales 
GROUP BY region 
ORDER BY revenue DESC;

-- 5. Revenue by Category
-- Calculates total revenue generated per product category
SELECT category, SUM(sales_amount) AS revenue 
FROM sales 
GROUP BY category 
ORDER BY revenue DESC;

-- 6. Monthly Revenue
-- Extracts year and month from order_date and aggregates sales to show monthly trends
SELECT strftime('%Y-%m', order_date) AS month, SUM(sales_amount) AS revenue 
FROM sales 
GROUP BY month 
ORDER BY month;

-- 7. Top Five Customers
-- Identifies the top 5 customers based on their total spending
SELECT customer_id, SUM(sales_amount) AS total_spent 
FROM sales 
GROUP BY customer_id 
ORDER BY total_spent DESC 
LIMIT 5;

-- 8. Average Order Value
-- Calculates the average revenue generated per unique order
SELECT SUM(sales_amount) / COUNT(DISTINCT order_id) AS avg_order_value 
FROM sales;

-- 9. Products with total quantity sold greater than a selected threshold
-- Filters out products that have sold a low total quantity (e.g., threshold of 10)
SELECT product, SUM(quantity) AS total_quantity 
FROM sales 
GROUP BY product 
HAVING total_quantity > 10 
ORDER BY total_quantity DESC;
