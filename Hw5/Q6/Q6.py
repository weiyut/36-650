import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="liese5378105", 
                        database="postgres"
                       )
cur = conn.cursor()
cur.execute("CREATE TABLE employees(id SERIAL,fname varchar(10),lname varchar(10));")
cur.execute("SELECT * FROM employees")
print("Unformatted Results:")
print (cur.description)
print("\n\n Formatted Results:")
    
conn.commit()
cur.close()
conn.close()