-- Task 3: DCL

-- 1. Create new PostgreSQL role hr_user with password
CREATE ROLE hr_user WITH LOGIN PASSWORD 'hr_password_123';

-- 2. Grant SELECT on Employees to hr_user
GRANT SELECT ON Employees TO hr_user;

-- 4. As admin, grant INSERT and UPDATE on Employees
GRANT INSERT, UPDATE ON Employees TO hr_user;

-- Also grant access to the SERIAL sequence
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;

