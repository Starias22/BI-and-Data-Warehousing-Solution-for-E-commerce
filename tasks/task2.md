# Task 2: Build the data warehouse

## Data Warehouse Design and Setup

This consists to use the provided sample data to design a star schema for the data warehouse. Here is an overview of the sample data.

The design has been created using PgAdmin.

![alt text](./../resources/images/sample_data.png)

### 0. Initialization
- Go to PgAdmin
- Create a database named `softcart`
- Perform the following: softcart->ERD for Database to create a database design file.

### 1. Design the dimension table softcartDimDate

| Field | Description |
|----------|----------|
| dateid   | The id of the date (Primary key) |
| date   | The date (20-Feb-21)  |
 weekday   | The day number in the week (from 1 to 7) |
| weekdayname  | The name of the day in the week (from Monday to Sunday)|
| month | The month number (from 1 to 12) |
| monthname | The name of the month (from January to December) |
| quarter   | The quarter number (1, 2, 3 or 4) |
| quartername   | The name of the quarter (Q1, Q2, Q3 or Q4) |
| year   | The year (2022, 2023 for examples) |

In PgAdmin, create the dimension table softcartDimDate

![alt text](./../resources/images/softcartDimDate.png)

### 2. Design the dimension table softcartDimCategory

| Field | Description |
|----------|----------|
| categoryid   | The id of the category (Primary key) |
| category   | The category (Movie, Ebook, Song for examples) |

- In PgAdmin, create the dimension table softcartDimCategory

![alt text](./../resources/images/softcartDimCategory.png)

### 3. Design the dimension table softcartDimItem

| Field | Description |
|----------|----------|
| itemid   | The id of the item (Primary key) |
| item   | The item (The Matrix, The Alchemist, Baby Shark, THe Lord of the Rings for examples) |

- In PgAdmin, create the dimension table softcartDimItem


![alt text](./../resources/images/softcartDimItem.png)

### 4. Design the dimension table softcartDimCountry

| Field | Description |
|----------|----------|
| countryid   | The id of the country (Primary key) |
| country  | The name of the country (USA, Canada, Japan, Cyprus for examples) |

- In PgAdmin, create the dimension table softcartDimCountry

![alt text](./../resources/images/softcartDimCountry.png)

### 5. Design the fact table softcartFactSales

| Field | Description |
|----------|----------|
| orderid   | The order id (Primary key) |
| price  | The quantity of waste colleted in tons (9.99, 5.99, 2.49, 6.99 for examples)  |
|dateid   | The  date id (foreign key) |
|categoryid   | The id of the category (Foreign key) |
| itemid   | The id of the item (Foreign key) |
| countryid   | The id of the country (Foreign key) |

- In PgAdmin, create the fact table softcartFactSales


![alt text](./../resources/images/softcartFactSales.png)

### 6. Design the relationships

- In PgAdmin, create the relations between of the dimensions tables with the fact table.

![alt text](./../resources/images/softcartRelationships.png)

### 7. Create the schema

In PgAdmin, use softcart->CREATE Script->Execute Script to run the query for the creation of the schema. 
![alt text](./../resources/images/createschema.png)

## Data Warehouse Reporting

There are two opions for reporting:either using PostgreSQL or using IBM Db2

### Data Warehouse Reporting using PostgreSQL

- First of all download this script either [manually](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nm75oOK5n7AGME1F7_OIQg/CREATE-SCRIPT.sql) or using wget.

```sh
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nm75oOK5n7AGME1F7_OIQg/CREATE-SCRIPT.sql
```

- Run th script to get the dimension tables and the fact table created.

```sql
\include CREATE-SCRIPT.sql 
```

#### Loading Data

##### 1. Load data into the dimension table `DimDate`

- Download the data either [manually](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv) or using wget.

```sh
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv
```

- Load the data

```sql
\COPY "DimDate"
FROM 'DimDate.csv' 
DELIMITER ',' CSV HEADER;
```

- List the first five (5) rows of the table `DimDate`

```sql
SELECT * FROM "DimDate" LIMIT 5;
```
![alt text](./../resources/images/DimDate.png)


##### 2. Load data into the dimension table `DimCategory`

- Download the data either [manually](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv) or using wget

```sh
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv
```

- Load the data

```sql
\COPY "DimCategory"
FROM 'DimCategory.csv'
DELIMITER ',' CSV HEADER;
```

- List the first five (5) rows of the table `DimCategory`



![alt text](./../resources/images/DimCategory.png)


##### 3. Load data into the dimension table `DimCountry`

- Download the data either [manually](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv) or using wget

```sh
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv
```

- Load the data

```sql
\COPY "DimCountry"
FROM 'DimCountry.csv'
DELIMITER ',' CSV HEADER;
```

- List the first five (5) rows of the table `DimCountry`

```sql
SELECT * FROM "DimCountry" LIMIT 5;
```

![alt text](./../resources/images/DimCountry.png)


##### 4. Load data into the fact table `FactSales`

- Download the data either [manually](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv) or using wget

```sh
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv
```

- Load the data


```sql
\COPY "FactSales"
FROM 'FactSales.csv'
DELIMITER ',' CSV HEADER;
```

- List the first five (5) rows of the table `FactSales`

```sql
SELECT * FROM "FactSales" LIMIT 5;
```
![alt text](./../resources/images/FactSales.png)

#### Queries for data analytics

##### 1. Create a GROUPING SETS Query

Create a grouping sets query using the columns country, category, totalsales.

```sql
SELECT country, category, SUM(amount)
FROM (
    SELECT "DimCountry".country, "DimCategory".category, "FactSales".countryid, "FactSales".categoryid, amount FROM "FactSales"
    JOIN "DimCountry" ON "FactSales".countryid="DimCountry".countryid
    JOIN "DimCategory" ON "FactSales".categoryid="DimCategory".categoryid
) AS subquery
GROUP BY
GROUPING SETS(country, category);
```

![alt text](./../resources/images/groupingsets.png)

##### 2. Create a ROLLUP Query

Create a rollup query using the columns year, country, and totalsales.

```sql
SELECT year, country, SUM(amount)
FROM (
    SELECT "DimDate".year, "DimCountry".country, "FactSales".dateid, "FactSales".countryid, amount FROM "FactSales"
    JOIN "DimDate" ON "FactSales".dateid="DimDate".dateid
    JOIN "DimCountry" ON "FactSales".countryid="DimCountry".countryid
) AS subquery
GROUP BY
ROLLUP(year, country);
```

![alt text](./../resources/images/rollup.png)

##### 3. Create a CUBE Query

Create a cube query using the columns year, country, and average sales.

```sql
SELECT year, country, AVG(amount)
FROM (
    SELECT "DimDate".year, "DimCountry".country, "FactSales".dateid, "FactSales".countryid, amount FROM "FactSales"
    JOIN "DimDate" ON "FactSales".dateid="DimDate".dateid
    JOIN "DimCountry" ON "FactSales".countryid="DimCountry".countryid
) AS subquery
GROUP BY
CUBE(year, country);
```

![alt text](./../resources/images/cube.png)

##### 4. Create an MQT

Create an MQT named total_sales_per_country that has the columns country and total_sales.

```sql
CREATE MATERIALIZED VIEW total_sales_per_country AS 
SELECT country, SUM(amount) AS total_sales
FROM (
    SELECT "DimCountry".country, "FactSales".countryid, amount FROM "FactSales"
    JOIN "DimCountry" ON "FactSales".countryid="DimCountry".countryid
) AS subquery
GROUP BY country;

SELECT * FROM total_sales_per_country;
```

![alt text](./../resources/images/mtq.png)


### Data Warehouse Reporting using IBM Db2

Remove the public for ach table creation statement
Create an instance of Db 2 in IBM Cloud

Select the instance

Click on RUN SQL

Click on the PLus button, with the label Add new script

Choose FROM file

Select the file  CREATE-SCRIPT.sql

Click RUN all

Select Tables and you'll see that the four tables are created
