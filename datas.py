import sqlite3

db = sqlite3.connect('users.db')
cursor = db.cursor()

async def start_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS qollaniwshi(
        id INTEGER,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number INTEGER
    )
    ''')

async def add_user(id,username,first_name,last_name,phone_number):
    cursor.execute('''
    INSERT INTO qollaniwshi(
        id,username,first_name,last_name,phone_number
    )
          VALUES(?,?,?,?,?)
    ''',(id,username,first_name,last_name,phone_number))
    db.commit()

# async def start_db():
#     cursor.execute('''
# CREATE TABLE IF NOT EXISTS userlar(
#       id INTEGER,
#       username TEXT,
#       first_name TEXT,
#       last_name TEXT,
#       phone_number INTEGER
# )    
# ''')


# async def add_user(id,username,first_name,last_name,phone_number):
#     cursor.execute('''
# INSERT INTO userlar(
#               id,username,first_name,last_name,phone_number
# )
#               VALUES(?,?,?,?,?)
# ''',(id,username,first_name,last_name,phone_number))
#     db.commit()


async def show_user():
    cursor.execute('SELECT id FROM qollaniwshi')
    ids = cursor.fetchall()
    return ids