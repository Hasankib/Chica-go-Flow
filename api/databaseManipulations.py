import sqlite3

conn = sqlite3.connect('database.db')

for i in range(1,78):
    x = str(i)
    l = "community" + x
    y = 'DROP TABLE ' + l 
    conn.execute(y)
    d = "Table " + l + " deleted successfully" 
    print(d)


for i in range(1,78):
    x = str(i)
    l = "community" + x
    y = 'CREATE TABLE ' + l + ' (neighbour INTEGER, frequency INTEGER)'
    conn.execute(y)
    d = "Table " + l + " created successfully" 
    print(d)

cur = conn.cursor()
for i in range(1,78):
    x = str(i)
    l = "community" + x
    for s in range(1,78):
        if s != i:
            y = 'INSERT INTO ' + l + ' (neighbour,frequency) VALUES(?,?)'
            cur.execute(y,(s,0))
            conn.commit()
            print("executed:" + x + ": " + str(s))

conn.close()

