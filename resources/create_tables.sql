-- Drop tables if they exist
DROP TABLE IF EXISTS "FactSales";
DROP TABLE IF EXISTS "DimCountry";
DROP TABLE IF EXISTS "DimCategory";
DROP TABLE IF EXISTS "DimDate";

-- Create the DimDate table
CREATE TABLE "DimDate"
(
    dateid integer NOT NULL,
    date date,
    Year integer,
    Quarter integer,
    QuarterName character(50),
    Month integer,
    Monthname character(50),
    Day integer,
    Weekday integer,
    WeekdayName character(50),
    CONSTRAINT "DimDate_pkey" PRIMARY KEY (dateid)
);

-- Create the DimCategory table
CREATE TABLE "DimCategory"
(
    categoryid integer NOT NULL,
    category character(50),
    CONSTRAINT "DimCategory_pkey" PRIMARY KEY (categoryid)
);

-- Create the DimCountry table
CREATE TABLE "DimCountry"
(
    countryid integer NOT NULL,
    country character(50),
    CONSTRAINT "DimCountry_pkey" PRIMARY KEY (countryid)
);

-- Create the FactSales table with foreign key constraints
CREATE TABLE "FactSales"
(
    orderid integer NOT NULL,
    dateid integer,
    countryid integer,
    categoryid integer,
    amount integer,
    CONSTRAINT "FactSales_pkey" PRIMARY KEY (orderid),
    CONSTRAINT "FactSales_dateid_fkey" FOREIGN KEY (dateid) REFERENCES "DimDate" (dateid) ON DELETE CASCADE,
    CONSTRAINT "FactSales_countryid_fkey" FOREIGN KEY (countryid) REFERENCES "DimCountry" (countryid) ON DELETE CASCADE,
    CONSTRAINT "FactSales_categoryid_fkey" FOREIGN KEY (categoryid) REFERENCES "DimCategory" (categoryid) ON DELETE CASCADE
);
