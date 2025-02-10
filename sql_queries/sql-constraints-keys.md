SQL Constraints & Keys
Primary Key
Foreign Key
Unique Constraint
NOT NULL Constraint
CHECK Constraint
DEFAULT Constraint

SQL Constraints and Keys are used to enforce rules for data integrity and relationships between tables in a database. They ensure that data is valid, consistent, and reliable. Let's break down the most common types of constraints and keys with examples.

1. Primary Key (PK)
A Primary Key is a field (or combination of fields) that uniquely identifies each row in a table. It must contain unique values and cannot contain NULL values.

A table can only have one Primary Key.
It is automatically indexed, ensuring efficient querying.
Example:

sql
Copy
Edit
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT
);
EmpID is the Primary Key because it uniquely identifies each employee.
Inserting Data:

sql
Copy
Edit
INSERT INTO Employees (EmpID, Name, Age)
VALUES (1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35);
EmpID cannot contain NULL and must have unique values for each record.
2. Foreign Key (FK)
A Foreign Key is a field (or combination of fields) in one table that uniquely identifies a row in another table. It is used to enforce referential integrity between two related tables.

A Foreign Key creates a relationship between two tables, where the values in the Foreign Key column must match the values in the Primary Key of another table.
Example:

Assume there are two tables: Employees and Departments.

sql
Copy
Edit
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(100)
);

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(100),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);
The DeptID in the Employees table is a Foreign Key that refers to the DeptID in the Departments table.
This ensures that every employee must be assigned to a valid department.
Inserting Data:

sql
Copy
Edit
INSERT INTO Departments (DeptID, DeptName)
VALUES (1, 'HR'), (2, 'Finance');

INSERT INTO Employees (EmpID, Name, DeptID)
VALUES (1, 'Alice', 1), (2, 'Bob', 2);
If you try to insert an employee with an invalid DeptID (not present in Departments), it will result in a referential integrity violation.

3. Unique Constraint
A Unique Constraint ensures that all values in a column (or a combination of columns) are unique. Unlike the Primary Key, a table can have multiple Unique Constraints. However, it can still allow NULL values unless combined with a NOT NULL constraint.

It is used to prevent duplicate entries in a column.
Example:

sql
Copy
Edit
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE
);
Email has a Unique Constraint, meaning that no two users can have the same email address.
Inserting Data:

sql
Copy
Edit
INSERT INTO Users (UserID, Email)
VALUES (1, 'alice@example.com'), (2, 'bob@example.com');

-- This will result in an error since 'alice@example.com' is already used
INSERT INTO Users (UserID, Email)
VALUES (3, 'alice@example.com');
The second insertion would fail because the email is not unique.

4. NOT NULL Constraint
The NOT NULL constraint ensures that a column cannot have NULL values. It forces the user to provide a value for that column when inserting or updating data.

Example:

sql
Copy
Edit
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT
);
Name has a NOT NULL Constraint, so when inserting data, the Name field must always have a value.
Inserting Data:

sql
Copy
Edit
-- This is valid
INSERT INTO Employees (EmpID, Name, Age)
VALUES (1, 'Alice', 30);

-- This will result in an error because Name cannot be NULL
INSERT INTO Employees (EmpID, Name, Age)
VALUES (2, NULL, 25);
The second insertion fails because the Name field cannot be NULL.

5. CHECK Constraint
The CHECK constraint ensures that values in a column satisfy a specific condition. It can be applied to individual columns to enforce domain integrity.

Example:

sql
Copy
Edit
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT CHECK (Age >= 18)
);
The CHECK constraint ensures that the Age column can only have values greater than or equal to 18.
Inserting Data:

sql
Copy
Edit
-- This is valid
INSERT INTO Employees (EmpID, Name, Age)
VALUES (1, 'Alice', 30);

-- This will result in an error because Age must be greater than or equal to 18
INSERT INTO Employees (EmpID, Name, Age)
VALUES (2, 'Bob', 16);
The second insertion fails because Age is less than 18.

6. DEFAULT Constraint
The DEFAULT constraint is used to assign a default value to a column if no value is provided during an insert operation. It is useful when you want to assign a predefined value for a column when it is not explicitly mentioned.

Example:

sql
Copy
Edit
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(100),
    JoiningDate DATE DEFAULT CURRENT_DATE
);
The JoiningDate column will default to the current date (CURRENT_DATE) if no value is provided when inserting a record.
Inserting Data:

sql
Copy
Edit
-- This will use the current date as the JoiningDate
INSERT INTO Employees (EmpID, Name)
VALUES (1, 'Alice');

-- This will explicitly provide the JoiningDate
INSERT INTO Employees (EmpID, Name, JoiningDate)
VALUES (2, 'Bob', '2025-01-01');
The first insert will automatically use the current date for JoiningDate, while the second insert will use the provided date '2025-01-01'.

Summary of Constraints and Keys:
Primary Key (PK):

Uniquely identifies each row in a table.
Cannot contain NULL values.
A table can only have one Primary Key.
Foreign Key (FK):

Enforces a relationship between two tables.
Ensures data integrity by referencing a Primary Key in another table.
Unique Constraint:

Ensures all values in a column are unique.
A table can have multiple Unique Constraints.
Allows NULL unless combined with NOT NULL.
NOT NULL Constraint:

Ensures a column cannot have NULL values.
Forces the user to provide a value for the column.
CHECK Constraint:

Ensures that values in a column meet a specific condition.
Useful for validating data before insertion.
DEFAULT Constraint:

Assigns a default value to a column when no value is provided during insertion.
Useful for setting default values like the current date or a specific number.
These constraints help in maintaining data integrity and consistency in a database. They ensure that the data inserted into the database meets predefined rules and conditions.