# Data Warehouse Reporting using IBM Db2

## Create an IBM Db2 instance

- Go to [ibmcloud]() to create an instance of IBM Db2 using the Lite plan. You can do it by following this tutorial.
- Name the instance ProductionDW, which means Production Data Warehouse.
- During the creation of the instance, choose Dallas (us-south) as the location of your instance.

- Select the instance you've just created to lunch it. You will have something like the following.

![alt text](./../../resources/images/lunch_db2_instance.png)

## Create Credentials for the IBM Db2 instance

To create credentials for your instance, select Service credential-> New credential -> Add

## Create the schema

The SQL script for creating the schema of the production data warehouse can be found [here](./../../resources/create_tables.sql).

In your IBM Db2 instance
- Select Manage-> Go to UI
- Click on RUN SQL

- Click on the Plus button, with the label Add new script

- Choose FROM file

- Select the tables creation script you/ve just downloaded.

- Click RUN all

You will get an output looking like the following.

![alt text](./../../resources/images/create_tables.png)

- Click on Reload icon, with label Reload objects
Then select the schama and then Tables and you'll see that the four tables have been created within a schema (WYB81330 in my case)

![alt text](./../../resources/tables_list.png)

## Loading Data

To load initial data into the data warehouse, we will use ibm_db, a python DB API to interact with DB2 on Cloud

### Set up a virtual environment
We will create a python virtual environment. This environment will help us load the data from our local system into our IBM Db2 instance, using a python API

- Create the environment

```sh
python3 -m venv ibm_db2_env
```

- Activate the environment

```sh
source ibm_db2_env/bin/activate
```
- Install Pandas and IBM Db2 API

```sh
pip install pandas ibm_db
```

- Deactivate the environment

```sh
deactivate
```

### Copy credentials

Access IBM Db2 instance

On the main page, click Service Credentials and click the copy icon the copy to the clipboard the credentials you've just created. Then paste it into a text file.

### Create the python script to load the data into the production data warehouse

The python script to load the dat can be found here [here](./../../load_data_template.py)

Make a copy of that the script
```
cp load_data_template.py load_data.py
```
- Update the script by using the informations in the credentions you've just copied. THe following infirmations need to be updated:
    - DATABASE: the name of the database
    - HOSTNAME: the database server name
    - PORT: The port on which the database server is listenning
    - UID: The databas user id
    - PWD: The password

### Run the script

Run the python script to get the data loaded into IBM Db2 on cloud. It should not take more than 5 minutes.

```sh
python3 python3 load_data.py
```

Go to your Db2 instance to check the data was realy loaded: Click SQL and paste the following script and click Run all

```sql
SELECT COUNT(*) FROM "FactSales";
```

The output should look like the following

![alt text](./../../resources/images/data_load.png)

## Queries for data analytics

### 1. Create a GROUPING SETS Query

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

![alt text](./../../resources/images/ibm_db2/groupingsets.png)

### 2. Create a ROLLUP Query

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

![alt text](./../../resources/images/ibm_db2/rollup.png)

### 3. Create a CUBE Query

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

![alt text](./../../resources/images/ibm_db2/cube.png)


### 4. Create an MQT

Create an MQT named total_sales_per_country that has the columns country and total_sales.

```sql
CREATE MATERIALIZED VIEW total_sales_per_country AS 
SELECT country, SUM(amount) AS total_sales
FROM (
    SELECT "DimCountry".country, "FactSales".countryid, "FactSales".amount 
    FROM "FactSales"
    JOIN "DimCountry" ON "FactSales".countryid = "DimCountry".countryid
) AS subquery
GROUP BY country;

-- To select from the materialized view
SELECT * FROM total_sales_per_country;
```
