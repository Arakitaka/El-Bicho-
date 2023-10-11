import sqlite3

conexion = sqlite3.connect("rfiddatabase.db")
conexion.execute("""create table if not exists RFID (
                          ID integer primary key AUTOINCREMENT,
                          hexcode text,
                          object text,
                          owner text,
                          location text                       
                    )""")
conexion.close()
