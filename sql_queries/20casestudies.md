Here are **four SQL mock interview case studies** with **detailed problem statements, datasets, and solution approaches**. These cover a variety of SQL skills, including **joins, window functions, aggregations, performance tuning, and real-world data transformation**.  

---

# **🔥 SQL Mock Interview Case Studies**

## **📌 Case Study 1: E-Commerce Analytics**
### **Problem Statement**  
You are a **data analyst at an e-commerce company**. The company wants insights into **customer behavior, sales trends, and product performance**.  

### **Dataset**
#### **1. Customers Table**
| customer_id | name       | email             | signup_date |
|------------|-----------|------------------|-------------|
| 101        | Alice      | alice@email.com  | 2022-05-15  |
| 102        | Bob        | bob@email.com    | 2021-09-10  |

#### **2. Orders Table**
| order_id | customer_id | order_date | total_amount | status   |
|---------|------------|-----------|-------------|---------|
| 1001    | 101        | 2023-01-10 | 500         | Completed |
| 1002    | 102        | 2023-02-20 | 1200        | Cancelled |

#### **3. Products Table**
| product_id | product_name | category  | price |
|-----------|-------------|----------|-------|
| 1         | Laptop      | Electronics | 800   |
| 2         | Phone       | Electronics | 500   |

#### **4. Order_Items Table**
| order_item_id | order_id | product_id | quantity | price |
|--------------|---------|-----------|----------|------|
| 5001        | 1001    | 1         | 1        | 800  |
| 5002        | 1001    | 2         | 2        | 500  |

---

### **Interview Tasks**
1. **Find total revenue generated per month.**
2. **Find the top 3 customers who spent the most in 2023.**
3. **Find the most frequently ordered product category.**
4. **Calculate the average order value per customer.**
5. **Find customers who have never placed an order.**
6. **Find customers who have placed orders in every month of 2023.**

---

### **SQL Solutions**
#### **1️⃣ Total Revenue Per Month**
```sql
SELECT 
    DATE_TRUNC('month', order_date) AS month, 
    SUM(total_amount) AS total_revenue
FROM orders
WHERE status = 'Completed'
GROUP BY month
ORDER BY month;
```

#### **2️⃣ Top 3 Spending Customers**
```sql
SELECT 
    c.customer_id, c.name, 
    SUM(o.total_amount) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.status = 'Completed' AND EXTRACT(YEAR FROM o.order_date) = 2023
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 3;
```

#### **3️⃣ Most Frequently Ordered Product Category**
```sql
SELECT 
    p.category, COUNT(oi.product_id) AS order_count
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY order_count DESC
LIMIT 1;
```

#### **4️⃣ Average Order Value Per Customer**
```sql
SELECT 
    customer_id, 
    AVG(total_amount) AS avg_order_value
FROM orders
WHERE status = 'Completed'
GROUP BY customer_id;
```

#### **5️⃣ Customers Who Never Ordered**
```sql
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

---

# **📌 Case Study 2: Fraud Detection in Banking**
### **Problem Statement**  
A **bank wants to detect fraudulent transactions** based on unusual patterns. You need to analyze transaction history.  

### **Dataset**
#### **1. Transactions Table**
| transaction_id | customer_id | transaction_date | amount | transaction_type | status  |
|---------------|------------|-----------------|--------|-----------------|--------|
| 5001         | 101        | 2023-01-15      | 200    | Credit         | Approved |
| 5002         | 101        | 2023-01-15      | 5000   | Debit          | Declined |

---

### **Interview Tasks**
1. **Find customers who made more than 3 transactions in a day.**
2. **Detect transactions that are 5x the customer’s average transaction value.**
3. **Identify customers with repeated declined transactions.**
4. **Find customers who transacted from multiple locations on the same day.**

---

### **SQL Solutions**
#### **1️⃣ Customers with More Than 3 Transactions in a Day**
```sql
SELECT customer_id, transaction_date, COUNT(*) AS txn_count
FROM transactions
GROUP BY customer_id, transaction_date
HAVING COUNT(*) > 3;
```

#### **2️⃣ Transactions That Are 5x the Customer’s Average**
```sql
WITH avg_txn AS (
    SELECT customer_id, AVG(amount) AS avg_amount
    FROM transactions
    GROUP BY customer_id
)
SELECT t.*
FROM transactions t
JOIN avg_txn a ON t.customer_id = a.customer_id
WHERE t.amount > 5 * a.avg_amount;
```

---

# **📌 Case Study 3: Employee Management System**
### **Problem Statement**  
A company’s HR team wants to analyze **employee salaries, promotions, and attrition rates**.

### **Dataset**
#### **1. Employees Table**
| emp_id | name  | department | salary | hire_date |
|--------|------|-----------|--------|-----------|
| 1      | John  | IT        | 70000  | 2019-06-01 |

#### **2. Promotions Table**
| emp_id | promotion_date | new_salary |
|--------|---------------|------------|
| 1      | 2021-01-10    | 75000      |

---

### **Interview Tasks**
1. **Find employees who never got a promotion.**
2. **Find department-wise average salary.**
3. **Identify the top 3 highest-paid employees per department.**

---

### **SQL Solutions**
#### **1️⃣ Employees Who Never Got a Promotion**
```sql
SELECT e.emp_id, e.name
FROM employees e
LEFT JOIN promotions p ON e.emp_id = p.emp_id
WHERE p.emp_id IS NULL;
```

#### **2️⃣ Department-Wise Average Salary**
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

---

# **📌 Case Study 4: Healthcare Analytics**
### **Problem Statement**  
A hospital wants to analyze **patient visits, average stay duration, and readmission rates**.

### **Dataset**
#### **1. Patients Table**
| patient_id | name  | age | gender |
|------------|------|----|--------|
| 1          | Adam | 30 | M      |

#### **2. Admissions Table**
| admission_id | patient_id | admission_date | discharge_date |
|-------------|------------|----------------|---------------|
| 1001       | 1          | 2023-01-01     | 2023-01-05    |

---

### **Interview Tasks**
1. **Find the average hospital stay duration.**
2. **Identify patients readmitted within 30 days.**

---

### **SQL Solutions**
#### **1️⃣ Average Hospital Stay Duration**
```sql
SELECT AVG(discharge_date - admission_date) AS avg_stay
FROM admissions;
```

#### **2️⃣ Patients Readmitted Within 30 Days**
```sql
SELECT a1.patient_id
FROM admissions a1
JOIN admissions a2 
ON a1.patient_id = a2.patient_id
AND a1.admission_date BETWEEN a2.discharge_date AND a2.discharge_date + INTERVAL '30 days'
WHERE a1.admission_id != a2.admission_id;
```

---

### **🔥 Want more advanced case studies?**  
Will cover **more complex problems, industry-specific cases, or query optimizations!** 🚀

---

