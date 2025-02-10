1. SQL Basics
Introduction to SQL
Data Types in SQL (Numeric, String, Date & Time)
NULL Values & Handling
Basic CRUD Operations (SELECT, INSERT, UPDATE, DELETE)

SQL is a standard language for accessing and manipulating databases.

What is SQL?
SQL stands for Structured Query Language
SQL lets you access and manipulate databases
SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987
What Can SQL do?
SQL can execute queries against a database
SQL can retrieve data from a database
SQL can insert records in a database
SQL can update records in a database
SQL can delete records from a database
SQL can create new databases
SQL can create new tables in a database
SQL can create stored procedures in a database
SQL can create views in a database
SQL can set permissions on tables, procedures, and views
SQL is a Standard - BUT....
Although SQL is an ANSI/ISO standard, there are different versions of the SQL language.

However, to be compliant with the ANSI standard, they all support at least the major commands (such as SELECT, UPDATE, DELETE, INSERT, WHERE) in a similar manner.

Note: Most of the SQL database programs also have their own proprietary extensions in addition to the SQL standard!

Using SQL in Your Web Site
To build a web site that shows data from a database, you will need:

An RDBMS database program (i.e. MS Access, SQL Server, MySQL)
To use a server-side scripting language, like PHP or ASP
To use SQL to get the data you want
To use HTML / CSS to style the page

RDBMS
RDBMS stands for Relational Database Management System.

RDBMS is the basis for SQL, and for all modern database systems such as MS SQL Server, IBM DB2, Oracle, MySQL, and Microsoft Access.

The data in RDBMS is stored in database objects called tables. A table is a collection of related data entries and it consists of columns and rows.

Look at the "Customers" table:

ExampleGet your own SQL Server
SELECT * FROM Customers;
Every table is broken up into smaller entities called fields. The fields in the Customers table consist of CustomerID, CustomerName, ContactName, Address, City, PostalCode and Country. A field is a column in a table that is designed to maintain specific information about every record in the table.

A record, also called a row, is each individual entry that exists in a table. For example, there are 91 records in the above Customers table. A record is a horizontal entity in a table.

A column is a vertical entity in a table that contains all information associated with a specific field in a table.

===SQL Data Types START====
SQL data types define the type of data that a column can store in a database table. They ensure that the data being inserted or updated in the table is of the correct type, which helps maintain data integrity. Here’s a breakdown of common SQL data types with examples:

1. Numeric Data Types
These data types are used to store numbers.

INT (or INTEGER): Stores whole numbers without decimal points.

Example: INT(10) can store values like -2147483648 to 2147483647.
Example value: 25
BIGINT: Stores large whole numbers.

Example: BIGINT can store values like -9223372036854775808 to 9223372036854775807.
Example value: 9223372036854775806
DECIMAL (or NUMERIC): Stores numbers with fixed decimal points. This is useful for storing precise values, such as currency.

Syntax: DECIMAL(p, s) where p is the precision (total number of digits) and s is the scale (number of digits to the right of the decimal point).
Example: DECIMAL(10, 2) can store values like 12345.67.
Example value: 12345.67
FLOAT: Stores approximate numeric values with floating decimal points.

Example: FLOAT can store values like 3.14 or 9.81.
Example value: 3.14159
DOUBLE: Similar to FLOAT, but with more precision.

Example value: 3.1415926535
2. String Data Types
These data types are used to store text or strings of characters.

CHAR(n): Stores fixed-length strings. If you enter fewer characters than specified, it pads the remaining space with spaces.

Example: CHAR(10) will always store 10 characters. If you enter 'hello', it will be stored as 'hello '.
Example value: 'hello '
VARCHAR(n): Stores variable-length strings. You define a maximum length, but the string is only stored with the actual number of characters entered.

Example: VARCHAR(50) can store up to 50 characters.
Example value: 'Hello, world!'
TEXT: Stores variable-length strings with a large capacity (used for longer text).

Example value: 'This is a long text that could be more than 255 characters long... and so on.'
VARCHAR(MAX): Similar to TEXT, but used in some database systems (like SQL Server) for larger variable-length strings.

Example value: 'This is an extremely large amount of text.'
3. Date and Time Data Types
These data types are used to store date and time values.

DATE: Stores only the date (year, month, and day).

Example: '2025-02-10'
TIME: Stores only the time (hour, minute, second).

Example: '14:30:00'
DATETIME: Stores both the date and the time (including fractional seconds in some DBMS).

Example: '2025-02-10 14:30:00'
TIMESTAMP: Similar to DATETIME, but used in some databases for storing a point in time. It typically includes timezone information in some databases.

Example: '2025-02-10 14:30:00.123'
YEAR: Stores a year value, typically in the format YYYY.

Example: '2025'
4. Boolean Data Type
Used to store TRUE or FALSE values.

BOOLEAN: Stores logical values. In many systems, it’s represented as TRUE or FALSE (or 1 for TRUE and 0 for FALSE).
Example value: TRUE or FALSE
5. Binary Data Types
These data types are used to store binary data like images, audio files, or other multimedia.

BINARY(n): Stores fixed-length binary data.

Example: BINARY(8) can store a fixed length of 8 bytes of binary data.
Example value: 0x12345678
VARBINARY(n): Stores variable-length binary data.

Example: VARBINARY(50) can store up to 50 bytes of binary data.
Example value: 0x12345678ABCDEF
BLOB (Binary Large Object): Used for storing large binary data (e.g., images, audio, etc.).

Example: BLOB can store large amounts of binary data, like an image file.
6. Other Data Types
ENUM: A string object with a predefined set of values. Used to represent a column with a limited number of options.

Example: ENUM('Small', 'Medium', 'Large') where the column can store one of the values: Small, Medium, or Large.
Example value: 'Medium'
SET: A string object with a collection of values. It’s similar to ENUM, but can store multiple values from the predefined set.

Example: SET('Red', 'Blue', 'Green') where the column can store combinations like 'Red, Blue' or 'Green'.
Example value: 'Red, Blue'
Examples of SQL Column Definitions:
sql
Copy
Edit
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,               -- Integer data type
    FirstName VARCHAR(50),                    -- String data type
    LastName VARCHAR(50),                     -- String data type
    BirthDate DATE,                           -- Date data type
    HireDate DATETIME,                        -- Date and Time data type
    IsActive BOOLEAN,                         -- Boolean data type
    Salary DECIMAL(10, 2),                    -- Numeric data type with precision and scale
    ProfilePicture BLOB                       -- Binary data type for storing large objects
);
Summary:
Numeric Data Types: For storing numbers.
String Data Types: For storing text.
Date and Time Data Types: For storing date and time values.
Boolean Data Type: For logical TRUE/FALSE values.
Binary Data Types: For storing binary data.
Other Data Types: Specialized types like ENUM and SET.
Each of these data types plays an important role in ensuring that the data stored in your SQL database is accurate, efficient, and adheres to the appropriate format for various use cases.
===SQL Data Type END====


===SQL Null values START====
SQL NULL Values
What is a NULL Value?
A field with a NULL value is a field with no value.

If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.

Note: A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!

How to Test for NULL Values?
It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

We will have to use the IS NULL and IS NOT NULL operators instead.

IS NULL Syntax
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

IS NOT NULL Syntax
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;


The IS NULL Operator
The IS NULL operator is used to test for empty values (NULL values).

The following SQL lists all customers with a NULL value in the "Address" field:

ExampleGet your own SQL Server
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;

===SQL Null values END====

====CRUD OPERATIONS START ===
The SQL SELECT Statement
The SELECT statement is used to select data from a database.

ExampleGet your own SQL Server
Return data from the Customers table:

SELECT CustomerName, City FROM Customers;
Syntax
SELECT column1, column2, ...
FROM table_name;

Here, column1, column2, ... are the field names of the table you want to select data from.

The table_name represents the name of the table you want to select data from.

Select ALL columns
If you want to return all columns, without specifying every column name, you can use the SELECT * syntax:

Example
Return all the columns from the Customers table:

SELECT * FROM Customers;


The SQL INSERT INTO Statement
The INSERT INTO statement is used to insert new records in a table.

INSERT INTO Syntax
It is possible to write the INSERT INTO statement in two ways:

1. Specify both the column names and the values to be inserted:

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

2. If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the INSERT INTO syntax would be as follows:

INSERT INTO table_name
VALUES (value1, value2, value3, ...);

INSERT INTO Example
The following SQL statement inserts a new record in the "Customers" table:

ExampleGet your own SQL Server
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

Insert Data Only in Specified Columns
It is also possible to only insert data in specific columns.

The following SQL statement will insert a new record, but only insert data in the "CustomerName", "City", and "Country" columns (CustomerID will be updated automatically):

Example
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');

Insert Multiple Rows
It is also possible to insert multiple rows in one statement.

To insert multiple rows of data, we use the same INSERT INTO statement, but with multiple values:

Example
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
Make sure you separate each set of values with a comma ,.


The SQL UPDATE Statement
The UPDATE statement is used to modify the existing records in a table.

UPDATE Syntax
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

UPDATE Table
The following SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city.

ExampleGet your own SQL Server
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

UPDATE Multiple Records
It is the WHERE clause that determines how many records will be updated.

The following SQL statement will update the ContactName to "Juan" for all records where country is "Mexico":

Example
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';

Update Warning!
Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!

Example
UPDATE Customers
SET ContactName='Juan';

The SQL DELETE Statement
The DELETE statement is used to delete existing records in a table.

DELETE Syntax
DELETE FROM table_name WHERE condition;

SQL DELETE Example
The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:

ExampleGet your own SQL Server
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';


====CRUD OPERATIONS END ===