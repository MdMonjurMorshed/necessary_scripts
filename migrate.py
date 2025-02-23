import json
import uuid
from datetime import datetime

import psycopg2
from psycopg2 import sql


# Load JSON data from file
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Insert data into PostgreSQL
def insert_data_into_postgres(data, db_config):
    cur = None
    conn = None
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Prepare the SQL query
        query = sql.SQL("""
            INSERT INTO worklogs (
                uuid, created_at, updated_at, deleted_at, body, datetime,
                employee_code, employee_uuid, branch_uuid, company_uuid,
                multiple_worklog, day_identifier
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)

        # Insert each record
        for record in data:
            cur.execute(query, (
                str(uuid.uuid4()),  # Generate a new UUID for the record
                datetime.fromisoformat(record['createdAt']['$date'].replace('Z', '+00:00')),
                datetime.fromisoformat(record['updatedAt']['$date'].replace('Z', '+00:00')),
                None,  # Assuming DeletedAt is None
                record.get('body', ''),  # Use an empty string if 'body' is missing
                datetime.fromisoformat(record['datetime']['$date'].replace('Z', '+00:00')),
                record.get('employee_code', ''),  # Use an empty string if 'employee_code' is missing
                str(uuid.UUID(record.get('employee_uuid', '00000000-0000-0000-0000-000000000000'))),
                str(uuid.UUID(record.get('branch_uuid', '00000000-0000-0000-0000-000000000000'))),
                str(uuid.UUID(record.get('company_uuid', '00000000-0000-0000-0000-000000000000'))),
                record.get('multiple_worklog', False),  # Use False if 'multiple_worklog' is missing
                str(uuid.UUID(record.get('day_identifier', '00000000-0000-0000-0000-000000000000')))
            ))

        # Commit the transaction
        conn.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if cur:
            cur.close()
        if conn:
            conn.close()

# Database configuration
db_config = {
    'dbname': 'db_name',
    'user': 'doadmin',
    'password': 'pass123',  
    'host': 'some_host',
    'port': 'some_port'
}

# Path to your JSON file
json_file_path = '/home/istiaq/Downloads/ak_worklog.worklogv2.json'  # Fixed file path

# Load JSON data
data = load_json_data(json_file_path)

# Insert data into PostgreSQL
insert_data_into_postgres(data, db_config)