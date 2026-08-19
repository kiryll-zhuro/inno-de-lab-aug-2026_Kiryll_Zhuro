-- Task 2: DDL

-- 1. Create Departments table (drop first so the script can be re-run)
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

-- 2. Add Email column to Employees (only if it does not exist yet)
ALTER TABLE Employees
ADD COLUMN IF NOT EXISTS Email VARCHAR(100);

-- 3. Fill Email column with unique values
UPDATE
    Employees
SET
    Email = LOWER(FirstName) || '.' || LOWER(LastName) || '@company.com'
WHERE
    Email IS NULL;

-- 4. Add UNIQUE constraint to Email column (recreate safely)
ALTER TABLE Employees
ADD CONSTRAINT UQ_Employees_Email UNIQUE (Email);

-- 5. Rename Location column to OfficeLocation in Departments
ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;