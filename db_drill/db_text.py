import sqlite3

db_connect = sqlite3.connect('my_file_db.db')

with db_connect:
    curr = db_connect.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS tbl_text_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_name TEXT \
        )")
    db_connect.commit()
db_connect.close()


# connect to db
db_connect = sqlite3.connect('my_file_db.db')

# while connected to DD
with db_connect:
    # create db cursor
    curr = db_connect.cursor()

    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    # loop through fileList
    for item in fileList:
        # grab files that are txt files
        if item.endswith('.txt'):
            # add text file to db

            curr.execute("INSERT INTO tbl_text_files(col_file_name) VALUES (?)", (item,))
            # print text files to terminal
            print(item)
    db_connect.commit()
db_connect.close()




