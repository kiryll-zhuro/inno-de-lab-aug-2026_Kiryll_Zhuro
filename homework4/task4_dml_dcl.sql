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
BEGIN;

INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('New AI Initiative', 300000.00, '2024-01-01', '2024-12-31');

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES
    (2, currval('projects_projectid_seq'), 50),
    (4, currval('projects_projectid_seq'), 60);

COMMIT;