-- Task 4: DML/DCL

-- 1. Increase Salary by 10% for all employees in 'HR' department
UPDATE
    Employees
SET
    Salary = Salary * 1.10
WHERE
    Department = 'HR';

-- 2. Update Department to 'Senior IT' for employees with Salary > 70000
UPDATE
    Employees
SET
    Department = 'Senior IT'
WHERE
    Salary > 70000.00;

-- 3. Delete employees not assigned to any project
DELETE FROM
    Employees
WHERE
    NOT EXISTS (
        SELECT
            0
        FROM
            EmployeeProjects
        WHERE
            EmployeeProjects.EmployeeID = Employees.EmployeeID
    );

-- 4. Transaction: insert a new project and assign two employees
RETURNING
BEGIN;

WITH new_project AS (
    INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
    VALUES ('New AI Initiative', 300000.00, '2024-01-01', '2024-12-31')
    RETURNING ProjectID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
    e.EmployeeID,
    np.ProjectID,
    CASE
        WHEN e.EmployeeID = 2 THEN 50
        ELSE 60
    END
FROM
    new_project np,
    Employees e
WHERE
    e.EmployeeID IN (2, 4);

COMMIT;