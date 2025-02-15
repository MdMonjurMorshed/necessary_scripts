
import psycopg2

# Database connection settings
# prod_conn_hr = psycopg2.connect(
#     dbname="ak_hr_service",
#     user="doadmin",
#     password="hJ6VXXIAqbfHnTfU",
#     host="evident-prod-postgres-do-user-9563394-0.b.db.ondigitalocean.com",
#     port="25060"
# )

# prod_conn_branching = psycopg2.connect(
#     dbname="attendance_keeper_branch_service",
#     user="doadmin",
#     password="hJ6VXXIAqbfHnTfU",
#     host="evident-prod-postgres-do-user-9563394-0.b.db.ondigitalocean.com",
#     port="25060"
# )

prod_conn_attendance = psycopg2.connect(
    dbname="ak-attendance-service",
    user="doadmin",
    password="hJ6VXXIAqbfHnTfU",
    host="evident-prod-postgres-do-user-9563394-0.b.db.ondigitalocean.com",
    port="25060"
)

test_prod_connection_attendance = psycopg2.connect(
    dbname="ak_attendanse_service_feb25",
    user="doadmin",
    password="hJ6VXXIAqbfHnTfU",
    host="evident-prod-postgres-do-user-9563394-0.b.db.ondigitalocean.com",
    port="25060"

)

# sandbox_conn = psycopg2.connect(
#     dbname="sandbox_ak_hr_service",
#     user="evident",
#     password="1qazXSW@",
#     host="sandbox-postgres-1gdyuf3h.evidentbd.com",
#     port="5432"
# )

# sandbox_conn_project = psycopg2.connect(
#     dbname="sandbox_ak_project_service",
#     user="evident",
#     password="1qazXSW@",
#     host="sandbox-postgres-1gdyuf3h.evidentbd.com",
#     port="5432"
# )

# sandbox_conn_attendance = psycopg2.connect(
#     dbname="sandbox-ak-attendance-service",
#     user="evident",
#     password="1qazXSW@",
#     host="sandbox-postgres-1gdyuf3h.evidentbd.com",
#     port="5432"
# )

COMPANY_UUIDS = ['0148ad01-c138-42f5-9609-01d3989e92f1']
