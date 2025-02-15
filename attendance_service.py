


def process_data(cur):
    limit=100000
    offset = 60000
    query = f"SELECT * FROM  device_screenshots LIMIT {limit} OFFSET {offset}"
    cur.execute(query)
    screenshorts = cur.fetchall()

    

    columns = ('created_at', 'updated_at', 'deleted_at', 'uuid', 'device_uuid', 'link')
   
    value_list = []
    for screenshort in  screenshorts:
       
            id = screenshort['id']
            created_at = f"'{screenshort['created_at']}'" if screenshort['created_at'] else "NULL"
            updated_at = f"'{screenshort['updated_at']}'" if screenshort['updated_at'] else "NULL"
            deleted_at = f"'{screenshort['deleted_at']}'" if screenshort['deleted_at'] else "NULL"
            uuid = f"'{screenshort['uuid']}'" if screenshort['uuid'] else "NULL"
            device_uuid = f"'{screenshort['device_uuid']}'" if screenshort['device_uuid'] else "NULL"
            link = f"'{screenshort['link']}'" if screenshort['link'] else "NULL"
            employee_uuid = 'NULL'
            

            values = f"({id}, {created_at}, {updated_at}, {deleted_at}, {uuid}, {device_uuid},\
                    {link},{employee_uuid})"
            
            value_list.append(values)

    # insert_query += ', '.join(value_list)


    # print(insert_query)
    return value_list







def migrate_device_screenshorts(from_cur,to_cur):

    insert_query_list = process_data(from_cur)
    insert_query = ''' INSERT INTO device_screenshots (id,created_at, updated_at, deleted_at, uuid, device_uuid, link, employee_uuid)

    VALUES 
    {placeholser}
    '''
    print(len(insert_query_list))
    try:
        chunk_size = 10
        for i in range(0,len(insert_query_list),chunk_size):
            chunk = insert_query_list[i:i+chunk_size]
          
            rows = ',\n'.join(chunk)
            insert_query = f''' INSERT INTO device_screenshots (id,created_at, updated_at, deleted_at, uuid, device_uuid, link, employee_uuid)

    VALUES 
    {rows}
    '''
            
           
      
            to_cur.execute(insert_query)
            
        print("data migrate to device screen short")
    except Exception as e:
         print(str(e))
             
