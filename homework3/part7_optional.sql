-- Customers with at least 2 orders and at least one 'Delivered' delivery
SELECT
    first_name || ' ' || last_name AS full_name,
    country,
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_amount
FROM
    Customers,
    Orders
WHERE
    Orders.customer_id = Customers.customer_id
    AND EXISTS (
        SELECT
            0
        FROM
            Shippings
        WHERE
            customer = Customers.customer_id
            AND status = 'Delivered'
    )
GROUP BY
    Customers.customer_id,
    first_name,
    last_name,
    country
HAVING
    COUNT(order_id) >= 2






