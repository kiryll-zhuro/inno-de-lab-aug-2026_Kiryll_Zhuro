-- Customers who placed an order with the maximum amount
SELECT 
    first_name, 
    last_name, 
    amount
FROM 
    Customers, 
    Orders
WHERE
    Customers.customer_id = Orders.customer_id 
    AND amount = (SELECT
                      MAX(amount) AS amount 
                  FROM 
                      Orders)





