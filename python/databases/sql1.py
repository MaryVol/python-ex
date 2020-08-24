import sqlite3

conn = sqlite3.connect('orgcount.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if line.startswith("From: "):
        pieces = line.split('@')
        org = pieces[1].strip()
        cur.execute('SELECT org FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute(
                '''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
        else:
            cur.execute(
                'UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
        conn.commit()
sqlstr = 'SELECT * FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
