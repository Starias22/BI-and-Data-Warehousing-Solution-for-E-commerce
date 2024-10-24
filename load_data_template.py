import ibm_db
import pandas as pd

# Connection string
dsn = (
    "DATABASE=your_db_name;" 
    "HOSTNAME=your_hostname;"
    "PORT=your_port;"
    "PROTOCOL=TCPIP;"
    "UID=your_db_uid;"
    "PWD=your_db_password;"
    "SECURITY=SSL;"
)

def insert_dim_date(conn, csv_file_path):
    """Inserts data into DimDate table."""
    df = pd.read_csv(csv_file_path)

    # Check for null values
    if df.isnull().values.any():
        print("Data contains null values in DimDate. Please check your CSV file.")
        return

    insert_query = """
    INSERT INTO "DimDate" (dateid, date, Year, Quarter, QuarterName, Month, Monthname, Day, Weekday, WeekdayName) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    # Prepare the statement once
    stmt = ibm_db.prepare(conn, insert_query)
    
    # Create a list of tuples for the data
    data = [(
        row['dateid'], 
        row['date'], 
        row['Year'], 
        row['Quarter'], 
        row['QuarterName'], 
        row['Month'], 
        row['Monthname'], 
        row['Day'], 
        row['Weekday'], 
        row['WeekdayName']
    ) for index, row in df.iterrows()]

    try:
        # Insert data in batches to avoid large inserts
        batch_size = 1000  # Adjust as needed
        for i in range(0, len(data), batch_size):
            batch_data = tuple(data[i:i + batch_size])
            #print(f"Inserting batch {i // batch_size + 1}: {batch_data}")  # Debug information
            ibm_db.execute_many(stmt, batch_data)
        print("DimDate data inserted successfully.")
    except Exception as e:
        print(f"Error inserting DimDate: {ibm_db.stmt_errormsg(stmt)}")

def insert_dim_category(conn, csv_file_path):
    """Inserts data into DimCategory table."""
    df = pd.read_csv(csv_file_path)

    # Check for null values
    if df.isnull().values.any():
        print("Data contains null values in DimCategory. Please check your CSV file.")
        return

    print("No NULL VALUE")

    # Convert data types if necessary
    df['categoryid'] = df['categoryid'].astype(int)  # Ensure categoryid is an integer
    df['category'] = df['category'].astype(str)  # Ensure category is a string

    insert_query = """
    INSERT INTO "DimCategory" (categoryid, category) 
    VALUES (?, ?)
    """
    
    stmt = ibm_db.prepare(conn, insert_query)
    print("Query prepared")

    # Create a list of tuples for the data
    data = [(row['categoryid'], row['category']) for index, row in df.iterrows()]
    
    try:
        # Insert data in batches
        batch_size = 1000  # Adjust as needed
        for i in range(0, len(data), batch_size):
            batch_data = tuple(data[i:i + batch_size])
            print(f"Inserting batch {i // batch_size + 1}: {batch_data}")  # Debug information
            result = ibm_db.execute_many(stmt, batch_data)
            print("Batch inserted, result:", result)  # Show result of the batch insert
        print("DimCategory data inserted successfully.")
    except Exception as e:
        print(f"Error inserting DimCategory: {str(e)}")
        print(f"IBM DB Error: {ibm_db.stmt_errormsg(stmt)}")


def insert_dim_country(conn, csv_file_path):
    """Inserts data into DimCountry table."""
    df = pd.read_csv(csv_file_path)

    # Check for null values
    if df.isnull().values.any():
        print("Data contains null values in DimCountry. Please check your CSV file.")
        return

    insert_query = """
    INSERT INTO "DimCountry" (countryid, country) 
    VALUES (?, ?)
    """
    
    stmt = ibm_db.prepare(conn, insert_query)

    data = [(row['countryid'], row['country']) for index, row in df.iterrows()]

    try:
        batch_size = 1000  # Adjust as needed
        for i in range(0, len(data), batch_size):
            batch_data = tuple(data[i:i + batch_size])
           # print(f"Inserting batch {i // batch_size + 1}: {batch_data}")  # Debug information
            ibm_db.execute_many(stmt, batch_data)
        print("DimCountry data inserted successfully.")
    except Exception as e:
        print(f"Error inserting DimCountry: {ibm_db.stmt_errormsg(stmt)}")

def insert_fact_sales(conn, csv_file_path):
    """Inserts data into FactSales table."""
    df = pd.read_csv(csv_file_path)

    # Check for null values
    if df.isnull().values.any():
        print("Data contains null values in FactSales. Please check your CSV file.")
        return

    insert_query = """
    INSERT INTO "FactSales" (orderid, dateid, countryid, categoryid, amount) 
    VALUES (?, ?, ?, ?, ?)
    """
    
    stmt = ibm_db.prepare(conn, insert_query)

    data = [
        (
            int(row['orderid']), 
            int(row['dateid']), 
            int(row['countryid']), 
            int(row['categoryid']), 
            int(row['amount'])
        ) for index, row in df.iterrows()
    ]

    try:
        batch_size = 100000  # Adjust as needed
        for i in range(0, len(data), batch_size):
            batch_data = tuple(data[i:i + batch_size])
            #print(f"Inserting batch {i // batch_size + 1}: {batch_data}")  # Debug information
            ibm_db.execute_many(stmt, batch_data)
        print("FactSales data inserted successfully.")
    except Exception as e:
        print(f"Error inserting FactSales: {ibm_db.stmt_errormsg(stmt)}")

try:
    # Establish connection to the database
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to the database")

    print("Loading Data into DimCategory")
    insert_dim_category(conn, 'DimCategory.csv')  # CSV for DimCategory

    print("Loading Data into DimDate")
    insert_dim_date(conn, 'DimDate.csv')  # CSV for DimDate

    
    
    
    print("Loading Data into DimCountry")
    insert_dim_country(conn, 'DimCountry.csv')  # CSV for DimCountry
    
    print("Loading Data into FactSales")
    insert_fact_sales(conn, 'FactSales.csv')  # CSV for FactSales
        
    # Close the connection
    ibm_db.close(conn)
    print("Connection closed")

except Exception as e:
    print(f"Error: {e}")
