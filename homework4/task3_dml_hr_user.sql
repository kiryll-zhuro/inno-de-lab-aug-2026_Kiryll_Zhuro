-- Task 3: DCL

-- Test 1
SELECT * FROM Employees;

-- Test 2
-- Test 3
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Test', 'User', 'IT', 50000.00);

-- Test 3
UPDATE
    Employees
SET
    Salary = 52000.00
WHERE
    FirstName = 'Test'
    AND LastName = 'User';