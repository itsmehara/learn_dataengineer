### Types of Data : Structured, Semi-Structured, and Unstructured Data

#### **1. Structured Data**  
Data that is highly organized, stored in rows and columns, and easily searchable in databases.

1. Customer details in a CRM (e.g., name, email, phone number).  
2. Sales transactions in an Excel sheet or SQL table.  
3. Employee payroll information.  
4. Inventory data in a warehouse system.  
5. Banking transaction logs.  
6. Sensor data from IoT devices (e.g., temperature, pressure).  
7. Financial reports (balance sheets, P&L statements).  
8. Flight schedules and ticket bookings.  
9. Product catalogs with IDs and prices.  
10. Hospital patient records (e.g., diagnoses, prescriptions).  

---

#### **2. Semi-Structured Data**  
Data that has some organizational structure (e.g., tags or key-value pairs) but isn’t stored in traditional rows and columns.

1. JSON files storing API responses (e.g., user data from a social media app).  
2. XML files used for configuration (e.g., web application settings).  
3. Email data (metadata like sender, receiver, subject + message content).  
4. Log files from servers (e.g., Apache logs).  
5. CSV files with missing or inconsistent columns.  
6. HTML documents for web pages.  
7. Sensor readings sent in key-value format.  
8. NoSQL database entries (e.g., MongoDB documents).  
9. Configuration files for applications.  
10. YAML files used in DevOps pipelines.  

---

#### **3. Unstructured Data**  
Data that doesn’t follow a predefined model or format and is often difficult to process with traditional tools.

1. Images (e.g., photos, X-rays, CT scans).  
2. Videos (e.g., YouTube content, surveillance footage).  
3. Audio files (e.g., music, podcasts, voice recordings).  
4. Freeform text documents (e.g., Word docs, PDFs).  
5. Social media posts (e.g., tweets, Instagram captions).  
6. Chat transcripts from customer support.  
7. Scientific research papers.  
8. Satellite imagery and maps.  
9. Raw log files with no clear structure.  
10. Scanned handwritten notes.  

------

### What is Schema Evolution?
Schema evolution refers to the ability to change a table's schema (like adding, deleting, or renaming columns) without needing to rewrite or reload the data. Apache Iceberg supports schema evolution seamlessly, allowing you to update the structure of your data over time while maintaining compatibility.

---

### Example of Schema Evolution

#### Initial Schema:
You create a table with this schema:
```sql
CREATE TABLE sales (
    id BIGINT,
    product_name STRING,
    price DOUBLE
);
```

#### Evolving the Schema:
1. **Add a New Column**: Add a `discount` column without affecting existing data.
   ```sql
   ALTER TABLE sales ADD COLUMN discount DOUBLE;
   ```

2. **Rename a Column**: Rename `product_name` to `item_name`.
   ```sql
   ALTER TABLE sales RENAME COLUMN product_name TO item_name;
   ```

3. **Drop a Column**: Remove the `discount` column if it's no longer needed.
   ```sql
   ALTER TABLE sales DROP COLUMN discount;
   ```

#### Query After Evolution:
Even after these changes, old and new queries will work:
```sql
SELECT id, item_name, price FROM sales; -- Works seamlessly
```

---

### Key Benefits:
- No downtime or data rewrite is required.
- Old data remains compatible with the new schema.
- Simplifies handling changes in evolving datasets.

---

Got it! Let's start with the basics.

---

### What is a Data Lake?
A **data lake** is a centralized repository that allows you to store all your structured, semi-structured, and unstructured data at any scale. It’s designed to hold **raw data** until it’s needed for processing, analysis, or machine learning. 

#### Key Characteristics:
1. **Scalable Storage:**
   - Can store massive amounts of data (petabytes or exabytes).
2. **Flexible Schema:**
   - Allows storing data in its native/raw format. Schema is applied only when reading the data ("schema-on-read").
3. **Diverse Data Types:**
   - Can handle a mix of structured (e.g., tables), semi-structured (e.g., JSON, XML), and unstructured (e.g., images, videos) data.
4. **Low-Cost Storage:**
   - Often built on cost-effective storage systems like Amazon S3, Azure Blob Storage, or Hadoop Distributed File System (HDFS).

---

### Purpose of Data Lakes
Data lakes are used to:
- **Ingest data from diverse sources** (e.g., logs, IoT devices, social media).
- **Enable analytics** like business intelligence (BI), data science, and machine learning.
- **Serve as a single source of truth** for an organization’s data.

---

### Data Lake vs. Data Warehouse
| **Aspect**            | **Data Lake**                         | **Data Warehouse**               |
|------------------------|---------------------------------------|-----------------------------------|
| **Data Type**          | Raw (structured, semi-structured, unstructured) | Processed (structured only)      |
| **Schema**             | Schema-on-read                      | Schema-on-write                  |
| **Cost**               | Low (commodity hardware, object storage) | High (expensive hardware/software) |
| **Use Case**           | Big data, AI/ML, exploratory analysis | BI, operational reporting        |
| **Technology Examples**| S3, HDFS, Delta Lake, Iceberg        | Snowflake, Redshift, BigQuery    |

---

### Evolution of Data Lakes
Initially, Hadoop-based data lakes using HDFS became popular. Over time, the shift to **cloud-based object storage** (e.g., Amazon S3) made data lakes more cost-effective and scalable. However, challenges like managing data consistency and performance emerged.

---

### Modern Data Lake Ecosystem
Modern data lakes are built using advanced storage and table formats that add structure, governance, and performance to raw data. These components include:

1. **Table Formats:**
   - *Apache Iceberg*: Advanced table format with features like schema evolution, time travel, and ACID transactions.
   - *Delta Lake*: Focuses on ACID transactions and simplified data pipelines.
   - *Apache Hudi*: Optimized for near-real-time use cases and streaming data.

2. **Query Engines:**
   - *Trino (Presto)*: Distributed SQL engine for querying large datasets in data lakes.
   - *Apache Spark*: Unified analytics engine for big data and machine learning.

3. **Storage Systems:**
   - *Amazon S3*: Cloud object storage widely used for data lakes.
   - *Azure Data Lake Storage*: Microsoft's cloud-based data lake solution.
   - *HDFS*: Legacy on-premises distributed file system.

---

### Benefits of Modern Data Lakes
1. **Unified Analytics Platform:**
   - Combine BI, ML, and batch/stream processing.
2. **Cost Efficiency:**
   - Pay-as-you-go storage and processing.
3. **Interoperability:**
   - Integrate with multiple tools and frameworks.
4. **Governance:**
   - Data lakes now support features like versioning and auditing (thanks to tools like Iceberg).

---

### Challenges of Data Lakes
1. **Data Swamps:**
   - Without proper governance, data lakes can become unmanageable.
2. **Performance:**
   - Querying raw data can be slower compared to optimized systems like data warehouses.
3. **Complexity:**
   - Requires expertise in managing distributed systems, table formats, and query engines.

---

---

### What is Apache IceBerg?
- Apache Iceberg is an **open-source table format** for managing large datasets in data lakes.  
- It provides **better performance, scalability, and reliability** for data management.  
- Supports advanced features like:  
  - **Schema evolution** (updating table structure without rewriting data).  
  - **Time travel** (accessing previous versions of data).  
  - **ACID transactions** (ensuring consistency and integrity).  
- Works seamlessly with query engines like **Trino**, **Spark**, and **Flink**.  
- Ideal for modern **big data and analytics** use cases.


