import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="liese5378105", 
                        database="postgres"
                       )
cur = conn.cursor()
cur.execute('do $$ \
             Begin \
                 for i in 1..500 loop \
                     Insert Into employees(fname, lname) select substr(md5(random()::text), 0, 5), substr(md5(random()::text), 0, 5); \
                 End loop; \
             End; $$;')

print("Unformatted Results:")
print (cur.description)
print("\n\n Formatted Results:")
conn.commit()
cur.close()
conn.close()