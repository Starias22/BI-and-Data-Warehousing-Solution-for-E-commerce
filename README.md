# BI-and-Data-Warehousing-Solution-for-E-commerce
## Table of Contents
1. [Summary](#summary)
2. [Key tasks](key-tasks)
3. [Architecture](#architecture)
4. [Tools](#tools)
5. [Database Design](#database-design)
6. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup Steps](#setup-steps)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact Information](#contact-information)

## Summary
The BI-and-Data-Warehousing-Solution-for-E-commerce 
is a project inspired by the [Course 9](https://github.com/Starias22/IBM-Data-Warehouse-Engineer-Professional-Certificate/blob/main/Course9/notes.md) of
the [IBM Data Warehouse Engineer Professional Certificate](https://github.com/Starias22/IBM-Data-Warehouse-Engineer-Professional-Certificate/), titled Data Warehousing Capstone Project. It consists to build a data platform for retails analytics.


## Process Description
SoftCart's online presence is primarily through its website, which customers access using a variety of devices like laptops, mobiles and tablets.

All the catalog data of the products and transactional data like inventory and sales are stored in the MySQL database server.

SoftCart's webserver is driven entirely by this database.

Data is periodically extracted from this database and put into the staging data warehouse running on PostgreSQL.

Production data warehouse is on the cloud instance of IBM DB2 server.

BI teams connect to the IBM DB2 for operational dashboard creation. IBM Cognos Analytics is used to create dashboards.

An ETL process using a shell script is set up to extract new transactional data for each day from the OLTP database and load it into the staging data warehouse.

## Architecture

Here is the architecture of the data platform

![alt text](./resources/images/architecure.png)

## Tools
- **MySQL**: Used as the OLTP (Online Transaction Processing) database to store transactional sales data.
- **phpMyAdmin**: A web-based tool for managing MySQL databases, used for database administration and visualization.
- **PostgreSQL**: Used for the staging data warehouse, where data is temporarily stored before being moved to the production data warehouse.
- **IBM Db2 on Cloud**: The production data warehouse for long-term data storage and analytics.
- **IBM Cognos Analytics**: A BI tool for creating dashboards and generating reports.
- **Bash**: A Unix shell used for writing ETL (Extract, Transform, Load) scripts to automate the data pipeline.
- **Cron**: A job scheduling utility to automate the regular execution of ETL scripts.
- **PgAdmin**: A web-based administration tool for managing PostgreSQL databases, used for database design and querying.


## Key Tasks

Here are key tasks with a short description. For more details informations and the codes to perform each of them, refers to the links bellow corrsponding to each task.

### [Task 1](./tasks/task1.md): Set up the transactional database:
- Design the OLTP database
- Populate the OLTP database with the provided data
- Create an index to accelerate data retrieval
- Create a data backup script

Here is the schema of the `sales_data` table in the `sales` database

| Field        | Description                             |
|--------------|-----------------------------------------|
| product_id   | The ID of the product (Primary key)      |
| customer_id  | The ID of the customer (Foreign key)     |
| price        | The price of the product   |
| quantity     | The quantity of products sold            |
| timestamp    | The timestamp of the transaction         |

### [Task 2](./tasks/task2.md): Build the data warehouse:
- Design a schema for the data warehouse
- Create the schema and load the data into fact and dimension tables
- Automate the daily incremental data insertion into the data warehouse
- Create CUBES and ROLLUP to make the reporting easier

Here is the design of the data warehouse
![Data Warehouse Design](./resources/images/softcartRelationships.png)

### [Task 3](./tasks/task3.md): Create a BI dashboard:
- Create a barchart of quarterly sales of cell phones 
- Craete a piechart of sales of electronic goods by category
- Create a line chart of total sales per month for a given year

Here are the three charts created within the dashboard.
![Bar Chart](./resources/images/barchart.png)
![Pie Chart](./resources/images/piechart.png)
![Line Chart](./resources/images/linechart.png)

### [Task 4](./tasks/task4.md) Create ETL Data Pipelines 

- create ETL Data Pipelines to feed the Data Warehouse on a regular basis with new data:
   - Extract data from an OLTP database into CSV format
   - Transform the OLTP data to suit the data warehouse schema
   - Load the transformed data into the data warehouse
   - Verify that the data is loaded properly.

Find the complete final scrit [here](./resources/ETL.sh)
