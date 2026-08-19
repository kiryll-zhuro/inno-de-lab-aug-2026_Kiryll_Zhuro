-- Task 6 (optional)

-- 1. Projects where Bob Johnson worked > 150 hours
SELECT
    p.ProjectName
FROM
    Projects p
JOIN EmployeeProjects ep
    ON ep.ProjectID = p.ProjectID
JOIN Employees e
    ON e.EmployeeID = ep.EmployeeID
WHERE
    e.FirstName = 'Bob'
    AND e.LastName = 'Johnson'
    AND ep.HoursWorked > 150;

-- 2. +10% budget for projects with at least one IT employee
UPDATE
    Projects
SET
    Budget = Budget * 1.10
WHERE
    EXISTS (
        SELECT
            0
        FROM
            EmployeeProjects ep
        JOIN Employees e
            ON e.EmployeeID = ep.EmployeeID
        WHERE
            ep.ProjectID = Projects.ProjectID
            AND e.Department = 'IT'
    );

-- 3. EndDate = StartDate + 1 year where EndDate is NULL
UPDATE
    Projects
SET
    EndDate = StartDate + INTERVAL '1 year'
WHERE
    EndDate IS NULL;

-- 4. TCL: one transaction - new employee on 'Website Redesign' (80h)
BEGIN;

WITH new_employee AS (
    INSERT INTO Employees (FirstName, LastName, Department, Salary)
    VALUES ('Henry', 'Wilson', 'Marketing', 55000.00)
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
    ne.EmployeeID,
    p.ProjectID,
    80
FROM
    new_employee ne,
    Projects p
WHERE
    p.ProjectName = 'Website Redesign';

COMMIT;