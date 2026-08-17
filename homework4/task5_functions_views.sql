-- Task 5: function and view

-- 1. Bonus function (10% of salary)
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(p_employee_id INT, p_salary DECIMAL)
RETURNS DECIMAL AS $$
DECLARE
    v_bonus DECIMAL;
BEGIN
    v_bonus := p_salary * 0.10;
    RETURN v_bonus;
END;
$$ LANGUAGE plpgsql;

-- 2. Potential bonus per employee
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary,
    CalculateAnnualBonus(EmployeeID, Salary) AS AnnualBonus
FROM
    Employees;

-- 3. View: only IT employees
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM
    Employees
WHERE
    Department = 'IT';

-- 4. Read from the view 
SELECT
    *
FROM
    IT_Department_View;