import sqlite3


db_connect = sqlite3.connect('my_newdb')

with db_connect:
    curr = db_connect.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS tbl_text_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_name TEXT \
        )")
    db_connect.commit()
db_connect.close()


db_connect = sqlite3.connect('my_newdb')

with db_connect:
    curr = db_connect.cursor()

    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    for file in fileList:
        if file.endswith('.txt'):

            print(file)
    db_connect.commit()
db_connect.close()




