-- List of shippings with status and customer name
SELECT 
    status,
    first_name,
    last_name
FROM Shippings 
    INNER JOIN customers 
    ON Shippings.customer = Customers.customer_id 



