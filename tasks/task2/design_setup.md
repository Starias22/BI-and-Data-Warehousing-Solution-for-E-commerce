# Data Warehouse Design and Setup

This consists to use the provided sample data to design a star schema for the data warehouse. Here is an overview of the sample data.

The design has been created using PgAdmin.

![alt text](./../../resources/images/sample_data.png)

## 0. Initialization
- Go to PgAdmin
- Create a database named `softcart`
- Perform the following: softcart->ERD for Database to create a database design file.

###1. Design the dimension table softcartDimDate

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

![alt text](./../../resources/images/softcartDimDate.png)

## 2. Design the dimension table softcartDimCategory

| Field | Description |
|----------|----------|
| categoryid   | The id of the category (Primary key) |
| category   | The category (Movie, Ebook, Song for examples) |

- In PgAdmin, create the dimension table softcartDimCategory

![alt text](./../../resources/images/softcartDimCategory.png)

## 3. Design the dimension table softcartDimItem

| Field | Description |
|----------|----------|
| itemid   | The id of the item (Primary key) |
| item   | The item (The Matrix, The Alchemist, Baby Shark, THe Lord of the Rings for examples) |

- In PgAdmin, create the dimension table softcartDimItem


![alt text](./../../resources/images/softcartDimItem.png)

## 4. Design the dimension table softcartDimCountry

| Field | Description |
|----------|----------|
| countryid   | The id of the country (Primary key) |
| country  | The name of the country (USA, Canada, Japan, Cyprus for examples) |

- In PgAdmin, create the dimension table softcartDimCountry

![alt text](./../../resources/images/softcartDimCountry.png)

## 5. Design the fact table softcartFactSales

| Field | Description |
|----------|----------|
| orderid   | The order id (Primary key) |
| price  | The quantity of waste colleted in tons (9.99, 5.99, 2.49, 6.99 for examples)  |
|dateid   | The  date id (foreign key) |
|categoryid   | The id of the category (Foreign key) |
| itemid   | The id of the item (Foreign key) |
| countryid   | The id of the country (Foreign key) |

- In PgAdmin, create the fact table softcartFactSales


![alt text](./../../resources/images/softcartFactSales.png)

## 6. Design the relationships

- In PgAdmin, create the relations between of the dimensions tables with the fact table.

![alt text](./../../resources/images/softcartRelationships.png)

## 7. Create the schema

In PgAdmin, use softcart->CREATE Script->Execute Script to run the query for the creation of the schema. 
![alt text](./../../resources/images/createschema.png)
