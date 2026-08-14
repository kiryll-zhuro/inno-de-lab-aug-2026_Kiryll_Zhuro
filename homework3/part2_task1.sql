-- List of orders with the name of the customer who placed the order
SELECT 
    first_name,
    last_name,
    item,
    amount
FROM 
    Orders 
INNER JOIN Customers 
    ON Orders.customer_id = Customers.customer_id 


