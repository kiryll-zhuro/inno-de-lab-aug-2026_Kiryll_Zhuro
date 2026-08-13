-- Find all customers from country 'USA' older than 2
SELECT 
    first_name, 
    last_name, 
    age, 
    country 
FROM 
    Customers
WHERE 
    country = 'USA' 
    AND age > 25
