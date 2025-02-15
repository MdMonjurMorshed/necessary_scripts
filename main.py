import psycopg2
import psycopg2.extras

from attendance_service import migrate_device_screenshorts
from config import prod_conn_attendance, test_prod_connection_attendance


def migrate_attendance_service_data():

    prod_att_cursor = prod_conn_attendance.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    test_prod_att_cursor = test_prod_connection_attendance.cursor()

    

    # try:
    #     delete_data(test_prod_connection_attendance,'branch_preferences',COMPANY_UUIDS)
    # except:
    #     pass

    migrate_device_screenshorts(from_cur=prod_att_cursor,to_cur=test_prod_att_cursor)

    test_prod_connection_attendance.commit()

if __name__== "__main__":
    migrate_attendance_service_data()
