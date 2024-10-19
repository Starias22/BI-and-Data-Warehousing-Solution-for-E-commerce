#!/bin/sh
MYSQL_PASSWORD=YajH4vC7HDlY3DkpPZFIzqFS
MYSQL_DB=sales
MYSQL_TABLE=sales_data
SALES_FILE=/home/project/sales.csv
SALES_TEMP_FILE=/home/project/temp_sales_commas.csv
DIM_DATE_FILE=/home/project/DimDate.csv
FACT_SALES_FILE=/home/project/FactSales.csv
PGHOST=postgres

# Load data from the sales database into a CSV file
mysql -h mysql -P 3306 -u root --password=$MYSQL_PASSWORD \
  --database=$MYSQL_DB \
  --execute="select * from $MYSQL_TABLE" \
  --batch --silent > $SALES_FILE

# The csv generated will have tabs. Replace all the tabs with commas
tr '\t' ',' < $SALES_FILE >  $SALES_TEMP_FILE

# Move the temporary file with commas to the original file location
mv $SALES_TEMP_FILE $SALES_FILE

# Set Postgres password
#export PGPASSWORD=YG5WsiqE2ICLPB3sxSvuM4jM

# Load the data from the CSV file into PostgreSQL
psql --username=postgres --host=$PGHOST --dbname=sales_new \
  -c "\COPY sales_data(rowid, product_id, customer_id, price, quantity, timestamp) \
      FROM '$SALES_FILE' DELIMITER ',' CSV HEADER;"

# Delete sales.csv
rm $SALES_FILE

# Load DimDate table from the data present in sales_data table
psql --username=postgres --host=$PGHOST --dbname=sales_new \
  -c "INSERT INTO DimDate(dateid, day, month, year) \
      SELECT rowid, to_char(timestamp, 'DAY'), to_char(timestamp, 'mon'), to_char(timestamp, 'YYYY') \
      FROM sales_data;"

# Load FactSales table from the data present in sales_data table
psql --username=postgres --host=$PGHOST --dbname=sales_new \
  -c "INSERT INTO FactSales \
      SELECT rowid, product_id, customer_id, price, quantity*price AS total_price \
      FROM sales_data;"

# Export DimDate table to a CSV
psql --username=postgres --host=$PGHOST --dbname=sales_new \
  -c "\COPY DimDate TO '$DIM_DATE_FILE' DELIMITER ',' CSV HEADER;"

# Export FactSales table to a CSV
psql --username=postgres --host=$PGHOST --dbname=sales_new \
  -c "\COPY FactSales TO '$FACT_SALES_FILE' DELIMITER ',' CSV HEADER;"

