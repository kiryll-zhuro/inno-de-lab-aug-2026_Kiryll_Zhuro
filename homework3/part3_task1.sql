-- List of shippings with status and customer name
SELECT 
    country,
    COUNT(*) AS count
FROM 
    Customers
GROUP BY 
    country
    



