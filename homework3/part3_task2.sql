-- Total number of orders and average amount for each item
SELECT 
    item,
    COUNT(*) AS count,
    AVG(amount) AS avg_amount
FROM 
    Orders
group BY 
    item 



