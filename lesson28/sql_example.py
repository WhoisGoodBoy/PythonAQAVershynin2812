import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='localhost',
    port='9999',
    database='postgres'
)

cursor = connection.cursor()
#cursor.execute('CREATE TABLE very_cool_users_table (id varchar(8) primary key, first_name varchar(25), last_name varchar(25), age integer, email varchar(50));COMMIT;')
'''cursor.execute("INSERT INTO very_cool_users_table (id, first_name, last_name, age, email) "
               "VALUES ('AAAAAAAA', 'Walter', 'White', 52, 'walter_white@gmail.com'), "
               "('BBBBBBBB', 'Jessie', 'Pinkman', 24, 'jessie_pinkman@gmail.com');COMMIT;")'''
cursor.execute('SELECT * FROM very_cool_users_table;')
connection.commit()
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
if connection:
    connection.close()

