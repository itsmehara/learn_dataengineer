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

Here are **four more advanced SQL mock interview case studies** covering **performance optimization, big data handling, query tuning, indexing, and complex analytical queries.** These are **real-world, industry-specific scenarios** that **require expert-level SQL skills.**  

---

# **🔥 Advanced SQL Mock Interview Case Studies**

## **📌 Case Study 5: Stock Market Data Analysis**
### **Problem Statement**  
You are a **data analyst for a stock trading platform**. Your job is to analyze stock prices, trading volumes, and customer transactions.  

### **Dataset**
#### **1. Stocks Table**
| stock_id | symbol | company_name      | sector        |
|---------|--------|------------------|--------------|
| 1       | AAPL   | Apple Inc.       | Technology   |
| 2       | TSLA   | Tesla Inc.       | Automotive   |

#### **2. Stock_Prices Table**
| stock_id | date       | open_price | close_price | volume  |
|---------|-----------|------------|-------------|---------|
| 1       | 2023-01-01 | 140        | 145         | 1000000 |

#### **3. Transactions Table**
| transaction_id | user_id | stock_id | transaction_date | quantity | transaction_type | price |
|---------------|--------|---------|-----------------|----------|-----------------|------|
| 5001         | 101    | 1       | 2023-01-02      | 10       | Buy             | 145  |

---

### **Interview Tasks**
1. **Calculate daily stock price change percentage.**
2. **Find the highest and lowest closing price for each stock in a given year.**
3. **Find users who have bought at least 10 different stocks.**
4. **Identify stocks with the highest average daily trading volume.**
5. **Find the top 3 most profitable stocks in the last 6 months.**

---

### **SQL Solutions**
#### **1️⃣ Daily Stock Price Change (%)**
```sql
SELECT 
    stock_id, 
    date, 
    ((close_price - open_price) / open_price) * 100 AS daily_change_percentage
FROM stock_prices;
```

#### **2️⃣ Highest and Lowest Closing Price Per Stock**
```sql
SELECT 
    stock_id, 
    MAX(close_price) AS highest_price, 
    MIN(close_price) AS lowest_price
FROM stock_prices
WHERE EXTRACT(YEAR FROM date) = 2023
GROUP BY stock_id;
```

#### **3️⃣ Users Who Bought At Least 10 Different Stocks**
```sql
SELECT user_id
FROM transactions
WHERE transaction_type = 'Buy'
GROUP BY user_id
HAVING COUNT(DISTINCT stock_id) >= 10;
```

#### **4️⃣ Stocks With Highest Average Daily Volume**
```sql
SELECT stock_id, AVG(volume) AS avg_daily_volume
FROM stock_prices
GROUP BY stock_id
ORDER BY avg_daily_volume DESC
LIMIT 5;
```

---

# **📌 Case Study 6: Ride-Sharing Platform Optimization**
### **Problem Statement**  
A ride-sharing platform (like Uber) wants to **analyze driver performance, peak hours, and revenue per trip**.  

### **Dataset**
#### **1. Drivers Table**
| driver_id | name  | city   | rating |
|----------|------|------|--------|
| 1        | John  | NYC  | 4.8    |

#### **2. Rides Table**
| ride_id | driver_id | user_id | start_time          | end_time            | distance | fare  | status   |
|--------|----------|--------|-------------------|-------------------|---------|------|---------|
| 101    | 1        | 1001   | 2023-01-02 08:30  | 2023-01-02 08:50  | 5       | 20   | Completed |

---

### **Interview Tasks**
1. **Find the top 5 highest-earning drivers.**
2. **Identify peak hours based on ride volume.**
3. **Find average trip duration per city.**
4. **Calculate cancellation rate per driver.**
5. **Find the driver with the highest number of 5-star rides.**

---

### **SQL Solutions**
#### **1️⃣ Top 5 Highest-Earning Drivers**
```sql
SELECT driver_id, SUM(fare) AS total_earnings
FROM rides
WHERE status = 'Completed'
GROUP BY driver_id
ORDER BY total_earnings DESC
LIMIT 5;
```

#### **2️⃣ Peak Hours Based on Ride Volume**
```sql
SELECT 
    EXTRACT(HOUR FROM start_time) AS hour, 
    COUNT(*) AS ride_count
FROM rides
GROUP BY hour
ORDER BY ride_count DESC;
```

#### **3️⃣ Average Trip Duration Per City**
```sql
SELECT 
    d.city, 
    AVG(EXTRACT(EPOCH FROM (r.end_time - r.start_time)) / 60) AS avg_trip_duration_mins
FROM rides r
JOIN drivers d ON r.driver_id = d.driver_id
WHERE r.status = 'Completed'
GROUP BY d.city;
```

---

# **📌 Case Study 7: Performance Optimization in a SaaS Platform**
### **Problem Statement**  
A **SaaS company** wants to optimize database performance for **millions of daily users**.  

### **Dataset**
#### **1. Users Table**
| user_id | name  | email         | signup_date |
|--------|------|--------------|-------------|
| 1      | Alice | alice@email.com | 2023-01-10 |

#### **2. Activity_Log Table**
| log_id | user_id | event_type | event_time           |
|-------|--------|-----------|-------------------|
| 1001  | 1      | Login     | 2023-02-01 10:30 |

---

### **Interview Tasks**
1. **Identify slow queries and suggest indexes.**
2. **Optimize query performance for user activity logs.**
3. **Find users who have been inactive for the last 6 months.**
4. **Partition large tables for faster query execution.**
5. **Implement a caching mechanism for frequently accessed data.**

---

### **SQL Solutions**
#### **1️⃣ Identifying Slow Queries**
```sql
EXPLAIN ANALYZE 
SELECT * FROM activity_log 
WHERE event_type = 'Login' AND event_time > NOW() - INTERVAL '1 month';
```
- **Solution:** Create an **index on event_type and event_time**  
```sql
CREATE INDEX idx_event_time ON activity_log(event_type, event_time);
```

#### **2️⃣ Finding Inactive Users**
```sql
SELECT user_id, name
FROM users
WHERE user_id NOT IN (
    SELECT DISTINCT user_id FROM activity_log
    WHERE event_time >= NOW() - INTERVAL '6 months'
);
```

#### **3️⃣ Partitioning Large Tables**
```sql
ALTER TABLE activity_log 
PARTITION BY RANGE (event_time) (
    PARTITION p2023 VALUES LESS THAN ('2023-01-01'),
    PARTITION p2024 VALUES LESS THAN ('2024-01-01')
);
```

---

# **📌 Case Study 8: Healthcare Patient Data Analytics**
### **Problem Statement**  
A hospital wants to **predict patient readmission rates, track chronic illness, and improve patient outcomes.**  

### **Dataset**
#### **1. Patients Table**
| patient_id | name  | age | gender | chronic_disease |
|------------|------|----|--------|----------------|
| 1          | Adam | 55 | M      | Diabetes       |

#### **2. Admissions Table**
| admission_id | patient_id | admission_date | discharge_date |
|-------------|------------|----------------|---------------|
| 1001       | 1          | 2023-01-01     | 2023-01-10    |

---

### **Interview Tasks**
1. **Find patients readmitted within 30 days.**
2. **Calculate average hospital stay duration per disease.**
3. **Identify high-risk patients with multiple admissions.**
4. **Find the top 3 most common chronic diseases.**
5. **Predict readmission likelihood using SQL queries.**

---

### **SQL Solutions**
#### **1️⃣ Identifying Patients Readmitted in 30 Days**
```sql
SELECT a1.patient_id
FROM admissions a1
JOIN admissions a2 
ON a1.patient_id = a2.patient_id
AND a1.admission_date BETWEEN a2.discharge_date AND a2.discharge_date + INTERVAL '30 days'
WHERE a1.admission_id != a2.admission_id;
```

---

### **🔥 Need more practice problems?**  

Will add **more advanced queries, indexing strategies, or performance tuning scenarios!** 🚀

---

Here are **four more advanced SQL mock interview case studies** focusing on **real-world performance tuning, big data querying, advanced joins, and data integrity management.** These **simulate high-level interview scenarios** that test your **problem-solving and optimization skills.**  

---

# **🔥 Advanced SQL Mock Interview Case Studies (Set 2)**  

## **📌 Case Study 9: E-commerce Order Analytics & Optimization**  
### **Problem Statement**  
You are working as a **Data Analyst for an e-commerce platform** like Amazon. Your goal is to optimize **order processing, detect fraudulent transactions, and improve delivery times.**  

### **Dataset**  
#### **1. Orders Table**  
| order_id | user_id | product_id | order_date | status     | amount | payment_method |
|---------|--------|------------|------------|-----------|--------|----------------|
| 5001    | 101    | 10001      | 2023-01-02 | Completed | 120.50 | Credit Card    |

#### **2. Deliveries Table**  
| delivery_id | order_id | shipped_date | delivered_date | status     | delivery_partner |
|------------|---------|--------------|---------------|-----------|----------------|
| 7001       | 5001    | 2023-01-03   | 2023-01-05   | Delivered | FedEx          |

---

### **Interview Tasks**  
1. **Calculate the total revenue per month.**  
2. **Identify the top 5 most purchased products.**  
3. **Find average delivery time per delivery partner.**  
4. **Detect orders that are delayed beyond expected delivery time.**  
5. **Identify potential fraudulent orders (orders placed & canceled within 5 minutes).**  

---

### **SQL Solutions**  
#### **1️⃣ Total Revenue Per Month**  
```sql
SELECT 
    DATE_TRUNC('month', order_date) AS order_month, 
    SUM(amount) AS total_revenue
FROM orders
GROUP BY order_month
ORDER BY order_month;
```

#### **2️⃣ Top 5 Most Purchased Products**  
```sql
SELECT product_id, COUNT(*) AS purchase_count
FROM orders
GROUP BY product_id
ORDER BY purchase_count DESC
LIMIT 5;
```

#### **3️⃣ Average Delivery Time Per Partner**  
```sql
SELECT delivery_partner, 
    AVG(EXTRACT(DAY FROM (delivered_date - shipped_date))) AS avg_delivery_days
FROM deliveries
WHERE status = 'Delivered'
GROUP BY delivery_partner;
```

#### **4️⃣ Detect Delayed Orders**  
```sql
SELECT o.order_id, d.delivery_id, d.delivered_date, o.order_date
FROM orders o
JOIN deliveries d ON o.order_id = d.order_id
WHERE d.delivered_date > o.order_date + INTERVAL '5 days';
```

#### **5️⃣ Detect Potential Fraud Orders**  
```sql
SELECT user_id, COUNT(order_id) AS fraud_attempts
FROM orders
WHERE status = 'Cancelled' 
AND order_date >= NOW() - INTERVAL '5 minutes'
GROUP BY user_id
HAVING fraud_attempts > 3;
```

---

## **📌 Case Study 10: Banking Transaction Data Optimization**  
### **Problem Statement**  
A **banking institution** wants to detect **fraudulent transactions, optimize SQL query performance, and analyze transaction patterns.**  

### **Dataset**  
#### **1. Transactions Table**  
| transaction_id | user_id | transaction_date | amount | transaction_type | location  |
|---------------|--------|-----------------|--------|-----------------|----------|
| 8001         | 2001   | 2023-02-01      | 500    | Withdrawal      | New York |

#### **2. Accounts Table**  
| account_id | user_id | account_type | balance |
|-----------|--------|-------------|--------|
| 3001      | 2001   | Savings     | 1500   |

---

### **Interview Tasks**  
1. **Identify high-value transactions (top 1% by amount).**  
2. **Find users who have withdrawn more than their available balance.**  
3. **Detect fraud transactions (multiple transactions in different cities within 1 hour).**  
4. **Optimize queries using indexing.**  
5. **Partition large tables for faster queries.**  

---

### **SQL Solutions**  
#### **1️⃣ Find High-Value Transactions (Top 1%)**  
```sql
SELECT transaction_id, user_id, amount
FROM transactions
WHERE amount >= (SELECT PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY amount) FROM transactions);
```

#### **2️⃣ Find Users Who Overdrew Their Accounts**  
```sql
SELECT t.user_id, t.transaction_id, t.amount, a.balance
FROM transactions t
JOIN accounts a ON t.user_id = a.user_id
WHERE t.transaction_type = 'Withdrawal' AND t.amount > a.balance;
```

#### **3️⃣ Detect Fraud Transactions (Same User, Different Cities, <1 Hour)**  
```sql
SELECT t1.user_id, t1.transaction_id AS txn1, t2.transaction_id AS txn2, 
       t1.location AS loc1, t2.location AS loc2, t1.transaction_date, t2.transaction_date
FROM transactions t1
JOIN transactions t2 
ON t1.user_id = t2.user_id 
AND t1.transaction_id <> t2.transaction_id
AND t1.location <> t2.location
AND ABS(EXTRACT(EPOCH FROM (t1.transaction_date - t2.transaction_date))) < 3600;
```

#### **4️⃣ Optimize Query Performance Using Indexing**  
```sql
CREATE INDEX idx_transactions_date ON transactions(transaction_date);
CREATE INDEX idx_user_location ON transactions(user_id, location);
```

#### **5️⃣ Partition Transactions Table (Year-Based)**  
```sql
ALTER TABLE transactions 
PARTITION BY RANGE (transaction_date) (
    PARTITION p2022 VALUES LESS THAN ('2023-01-01'),
    PARTITION p2023 VALUES LESS THAN ('2024-01-01')
);
```

---

## **📌 Case Study 11: Social Media Engagement Analysis**  
### **Problem Statement**  
A social media company wants to **analyze user engagement trends, track viral posts, and optimize query performance.**  

### **Dataset**  
#### **1. Posts Table**  
| post_id | user_id | post_date | content       | likes | shares |
|--------|--------|----------|-------------|------|--------|
| 9001   | 5001   | 2023-03-10 | "Hello World" | 100  | 20     |

#### **2. Comments Table**  
| comment_id | post_id | user_id | comment_text | comment_date |
|-----------|--------|--------|--------------|-------------|
| 1001      | 9001   | 6001   | "Nice post!" | 2023-03-10 |

---

### **Interview Tasks**  
1. **Find posts with the highest engagement (likes + shares).**  
2. **Detect fake engagement (posts with 50%+ of likes from fake accounts).**  
3. **Find average engagement per user.**  
4. **Identify posts with sudden popularity spikes.**  
5. **Optimize performance for querying viral posts.**  

---

### **SQL Solutions**  
#### **1️⃣ Find Most Engaging Posts**  
```sql
SELECT post_id, (likes + shares) AS total_engagement
FROM posts
ORDER BY total_engagement DESC
LIMIT 10;
```

#### **2️⃣ Detect Fake Engagement**  
```sql
SELECT p.post_id, p.user_id, 
       COUNT(c.user_id) AS suspicious_likes
FROM posts p
JOIN comments c ON p.post_id = c.post_id
JOIN users u ON c.user_id = u.user_id
WHERE u.account_status = 'Fake'
GROUP BY p.post_id, p.user_id
HAVING COUNT(c.user_id) > 0.5 * p.likes;
```

#### **3️⃣ Average Engagement Per User**  
```sql
SELECT user_id, AVG(likes + shares) AS avg_engagement
FROM posts
GROUP BY user_id;
```

#### **4️⃣ Identify Popularity Spikes**  
```sql
SELECT post_id, post_date, 
       (likes - LAG(likes) OVER (PARTITION BY post_id ORDER BY post_date)) AS daily_growth
FROM posts;
```

#### **5️⃣ Optimize Query Performance for Viral Posts**  
```sql
CREATE INDEX idx_post_engagement ON posts(likes, shares);
```

---

# **🔥 Need More SQL Scenarios?**  
Let me know if you need **more complex indexing, query optimization techniques, or real-time analytics scenarios!** 🚀


