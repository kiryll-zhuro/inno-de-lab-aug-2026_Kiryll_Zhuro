-- Task 1: DML

-- 1. Insert two new employees (not in 'IT' department)
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Frank', 'Miller', 'Finance', 65000.00),
('Grace', 'Lee', 'HR', 55000.00);

-- 2. Select all employees
SELECT
    *
FROM
    Employees;

-- 3. Select FirstName and LastName of employees from 'IT' department
SELECT
    FirstName,
    LastName
FROM
    Employees
WHERE
    Department = 'IT';

-- 4. Update salary of 'Alice Smith' to 65000.00
UPDATE
    Employees
SET
    Salary = 65000.00
WHERE
    FirstName = 'Alice'
    AND LastName = 'Smith';

-- 5. Delete employee 'Eve Davis'
DELETE FROM
    Employees
WHERE
    FirstName = 'Eve'
    AND LastName = 'Davis';

-- 6. Check all changes
SELECT
    *
FROM
    Employees;