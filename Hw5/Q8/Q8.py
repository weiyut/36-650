import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="liese5378105", 
                        database="postgres"
                       )
cur = conn.cursor()
cur.execute('SELECT * FROM employees LIMIT 10;')
print("Unformatted Results:")
print (cur.description)
print("\n\n Formatted Results:")
for row in cur:
    print (row)
    
conn.commit()
cur.close()
conn.close()