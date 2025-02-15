
def delete_data(cur,table,company_uuid):
    truncate_query = F"DELETE FROM {table} WHERE company_uuid='{company_uuid}'"

    try:
        cur.execute(truncate_query)
        print(f"Data deleted from {table} successfully!")
    except Exception as e:
        print(str(e))    