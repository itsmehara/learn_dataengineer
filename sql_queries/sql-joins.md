2. SQL Joins & Relationships
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL OUTER JOIN
CROSS JOIN
SELF JOIN
NATURAL JOIN
Anti-joins and Semi-joins

SQL JOIN
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

Let's look at a selection from the "Orders" table:

OrderID	CustomerID	OrderDate
10308	2	1996-09-18
10309	37	1996-09-19
10310	77	1996-09-20
Then, look at a selection from the "Customers" table:

CustomerID	CustomerName	ContactName	Country
1	Alfreds Futterkiste	Maria Anders	Germany
2	Ana Trujillo Emparedados y helados	Ana Trujillo	Mexico
3	Antonio Moreno Taquería	Antonio Moreno	Mexico
Notice that the "CustomerID" column in the "Orders" table refers to the "CustomerID" in the "Customers" table. The relationship between the two tables above is the "CustomerID" column.

Then, we can create the following SQL statement (that contains an INNER JOIN), that selects records that have matching values in both tables:

ExampleGet your own SQL Server
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

Different Types of SQL JOINs
Here are the different types of the JOINs in SQL:

(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

INNER JOIN
The INNER JOIN keyword selects records that have matching values in both tables.

Let's look at a selection of the Products table:

ProductID	ProductName	CategoryID	Price
1	Chais	1	18
2	Chang	1	19
3	Aniseed Syrup	2	10
And a selection of the Categories table:

CategoryID	CategoryName	Description
1	Beverages	Soft drinks, coffees, teas, beers, and ales
2	Condiments	Sweet and savory sauces, relishes, spreads, and seasonings
3	Confections	Desserts, candies, and sweet breads
We will join the Products table with the Categories table, by using the CategoryID field from both tables:

ExampleGet your own SQL Server
Join Products and Categories with the INNER JOIN keyword:

SELECT ProductID, ProductName, CategoryName
FROM Products
INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

Note: The INNER JOIN keyword returns only rows with a match in both tables. Which means that if you have a product with no CategoryID, or with a CategoryID that is not present in the Categories table, that record would not be returned in the result.

Syntax
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

JOIN or INNER JOIN
JOIN and INNER JOIN will return the same result.

INNER is the default join type for JOIN, so when you write JOIN the parser actually writes INNER JOIN.

Example
JOIN is the same as INNER JOIN:

SELECT Products.ProductID, Products.ProductName, Categories.CategoryName
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID;

JOIN Three Tables
The following SQL statement selects all orders with customer and shipper information:

Here is the Shippers table:

ShipperID	ShipperName	Phone
1	Speedy Express	(503) 555-9831
2	United Package	(503) 555-3199
3	Federal Shipping	(503) 555-9931
Example
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

SQL LEFT JOIN Keyword
The LEFT JOIN keyword returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

LEFT JOIN Syntax
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
Note: In some databases LEFT JOIN is called LEFT OUTER JOIN.

SQL LEFT JOIN Example
The following SQL statement will select all customers, and any orders they might have:

ExampleGet your own SQL Server
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
Note: The LEFT JOIN keyword returns all records from the left table (Customers), even if there are no matches in the right table (Orders).

SQL RIGHT JOIN Keyword
The RIGHT JOIN keyword returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match.

RIGHT JOIN Syntax
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
Note: In some databases RIGHT JOIN is called RIGHT OUTER JOIN.

SQL RIGHT JOIN Example
The following SQL statement will return all employees, and any orders they might have placed:

ExampleGet your own SQL Server
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
Note: The RIGHT JOIN keyword returns all records from the right table (Employees), even if there are no matches in the left table (Orders).

SQL FULL OUTER JOIN Keyword
The FULL OUTER JOIN keyword returns all records when there is a match in left (table1) or right (table2) table records.

Tip: FULL OUTER JOIN and FULL JOIN are the same.

FULL OUTER JOIN Syntax
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;


SQL FULL OUTER JOIN Example
The following SQL statement selects all customers, and all orders:

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;

SQL Self Join
A self join is a regular join, but the table is joined with itself.

Self Join Syntax
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
T1 and T2 are different table aliases for the same table.

SQL Self Join Example
The following SQL statement matches customers that are from the same city:

ExampleGet your own SQL Server
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;

The SQL UNION Operator
The UNION operator is used to combine the result-set of two or more SELECT statements.

Every SELECT statement within UNION must have the same number of columns
The columns must also have similar data types
The columns in every SELECT statement must also be in the same order
UNION Syntax
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
UNION ALL Syntax
The UNION operator selects only distinct values by default. To allow duplicate values, use UNION ALL:

SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
Note: The column names in the result-set are usually equal to the column names in the first SELECT statement.

SQL UNION Example
The following SQL statement returns the cities (only distinct values) from both the "Customers" and the "Suppliers" table:

ExampleGet your own SQL Server
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
Note: If some customers or suppliers have the same city, each city will only be listed once, because UNION selects only distinct values. Use UNION ALL to also select duplicate values!

SQL UNION ALL Example
The following SQL statement returns the cities (duplicate values also) from both the "Customers" and the "Suppliers" table:

Example
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;
SQL UNION With WHERE
The following SQL statement returns the German cities (only distinct values) from both the "Customers" and the "Suppliers" table:

Example
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
SQL UNION ALL With WHERE
The following SQL statement returns the German cities (duplicate values also) from both the "Customers" and the "Suppliers" table:

Example
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
Another UNION Example
The following SQL statement lists all customers and suppliers:

Example
SELECT 'Customer' AS Type, ContactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers;
Notice the "AS Type" above - it is an alias. SQL Aliases are used to give a table or a column a temporary name. An alias only exists for the duration of the query. So, here we have created a temporary column named "Type", that list whether the contact person is a "Customer" or a "Supplier".

===========

SQL Joins are used to combine rows from two or more tables based on a related column between them. Joins allow you to fetch related data across multiple tables. SQL provides different types of joins to handle various scenarios, which will be explained below, including CROSS JOIN, NATURAL JOIN, and Anti-joins and Semi-joins.

1. Types of SQL Joins
INNER JOIN (Default Join)
The INNER JOIN is used to select records that have matching values in both tables. If there’s no match, no row is returned.

Example: Let’s say we have two tables:

Employees:

EmpID	Name
1	Alice
2	Bob
3	Charlie
Departments:

EmpID	Department
1	HR
2	Finance
sql
Copy
Edit
SELECT Employees.Name, Departments.Department
FROM Employees
INNER JOIN Departments
ON Employees.EmpID = Departments.EmpID;
Result:

Name	Department
Alice	HR
Bob	Finance
Only employees who have a matching department (based on EmpID) are returned.

LEFT JOIN (or LEFT OUTER JOIN)
The LEFT JOIN returns all records from the left table, and the matched records from the right table. If there is no match, the result will contain NULL values for columns from the right table.

Example:

sql
Copy
Edit
SELECT Employees.Name, Departments.Department
FROM Employees
LEFT JOIN Departments
ON Employees.EmpID = Departments.EmpID;
Result:

Name	Department
Alice	HR
Bob	Finance
Charlie	NULL
Here, Charlie doesn’t have a department, so the department column contains NULL.

RIGHT JOIN (or RIGHT OUTER JOIN)
The RIGHT JOIN returns all records from the right table and the matched records from the left table. If no match exists, NULL values are returned for columns from the left table.

Example:

sql
Copy
Edit
SELECT Employees.Name, Departments.Department
FROM Employees
RIGHT JOIN Departments
ON Employees.EmpID = Departments.EmpID;
Result:

Name	Department
Alice	HR
Bob	Finance
NULL	Marketing
Here, the Marketing department has no employee in the Employees table, so the Name is NULL.

FULL OUTER JOIN
The FULL OUTER JOIN returns all records when there is a match in either the left or right table. If there’s no match, NULL values are filled in for the missing side.

Example:

sql
Copy
Edit
SELECT Employees.Name, Departments.Department
FROM Employees
FULL OUTER JOIN Departments
ON Employees.EmpID = Departments.EmpID;
Result:

Name	Department
Alice	HR
Bob	Finance
Charlie	NULL
NULL	Marketing
CROSS JOIN
The CROSS JOIN produces the Cartesian product of two tables. That is, it returns all possible combinations of rows from both tables.

Example:

sql
Copy
Edit
SELECT Employees.Name, Departments.Department
FROM Employees
CROSS JOIN Departments;
Result:

Name	Department
Alice	HR
Alice	Finance
Alice	Marketing
Bob	HR
Bob	Finance
Bob	Marketing
Charlie	HR
Charlie	Finance
Charlie	Marketing
Every employee is paired with every department in the Departments table. The number of rows in the result will be the product of the number of rows in both tables.

2. NATURAL JOIN
A NATURAL JOIN automatically joins tables based on columns that have the same name and compatible data types in both tables. This join eliminates the need to explicitly specify the joining condition.

Example: Assuming both Employees and Departments have a column EmpID in common:

sql
Copy
Edit
SELECT Employees.Name, Departments.Department
FROM Employees
NATURAL JOIN Departments;
Result:

Name	Department
Alice	HR
Bob	Finance
The join is done automatically based on the EmpID column, which both tables have in common.

3. Anti-joins
An Anti-Join is a type of join that returns rows from one table where no matching rows exist in another table. SQL does not have a direct ANTI JOIN, but it can be simulated using a combination of LEFT JOIN and a WHERE clause.

Example: Let’s say we want to find employees who are not assigned to any department (those not present in the Departments table).

sql
Copy
Edit
SELECT Employees.Name
FROM Employees
LEFT JOIN Departments
ON Employees.EmpID = Departments.EmpID
WHERE Departments.EmpID IS NULL;
Result:

Name
Charlie
In this case, the query returns Charlie because he has no department assigned to him.

4. Semi-joins
A Semi-Join returns rows from the left table that have at least one matching row in the right table, but without duplicating data from the right table. SQL does not have a direct SEMI JOIN syntax, but it can be simulated using EXISTS.

Example: Let’s find employees who are assigned to at least one department (i.e., employees that have a corresponding record in the Departments table).

sql
Copy
Edit
SELECT Employees.Name
FROM Employees
WHERE EXISTS (
    SELECT 1
    FROM Departments
    WHERE Employees.EmpID = Departments.EmpID
);
Result:

Name
Alice
Bob
Here, we used EXISTS to ensure that only employees who are assigned to a department (i.e., those with matching EmpIDs in the Departments table) are returned.

5. SQL Relationships
Relationships between tables are crucial to how SQL queries are structured. Common types of relationships are:

One-to-One: A row in one table is linked to only one row in another table.

Example: A Person table with a PersonID and a Passport table with PersonID as a foreign key.
One-to-Many: A row in one table can be linked to multiple rows in another table.

Example: A Department table where one department can have multiple Employees.
Many-to-Many: A row in one table can be linked to multiple rows in another table, and vice versa. This requires a junction table.

Example: A Students table and a Courses table, where students can enroll in multiple courses, and courses can have multiple students. A junction table (Enrollments) links the two.
Summary of SQL Joins:
INNER JOIN: Only returns rows that have matching values in both tables.
LEFT JOIN: Returns all rows from the left table and matched rows from the right table.
RIGHT JOIN: Returns all rows from the right table and matched rows from the left table.
FULL OUTER JOIN: Returns all rows when there’s a match in either table.
CROSS JOIN: Returns the Cartesian product of two tables (every combination of rows).
NATURAL JOIN: Automatically joins tables on columns with the same name and compatible data types.
Anti-Join: Returns rows from one table where no matching rows exist in another table (simulated with LEFT JOIN and NULL).
Semi-Join: Returns rows from the left table that have matching rows in the right table, but without duplicating data from the right table (simulated with EXISTS).
These joins and relationships allow you to combine data efficiently, based on the needs of your query.

=======