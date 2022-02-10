import sqlite3


def conn():
    try:
        connect = sqlite3.connect("Manager.db")
    except Exception as e:
        print(e)
    return connect


def create_table():
    Create = """ CREATE TABLE IF NOT EXISTS Accounts (Password PRIMARY KEY,Email BLOB NOT NULL,Username BLOB NOT NULL,Url BLOB,Service TEXT NOT NULL); """
    connect = conn()
    cursor = connect.cursor()
    cursor.execute(Create)
    connect.commit()


def store_password(password, email, username, siteurl, service):
    connect = conn()
    cursor = connect.cursor()
    insertCommand = """INSERT INTO Accounts (Password, Email, Username, Url, Service) VALUES (?,?,?,?,?);"""
    dataToInsert = (password, email, username, siteurl, service)
    cursor.execute(insertCommand, dataToInsert)
    connect.commit()


def find_password(serviceName):
    connect = conn()
    cursor = connect.cursor()
    search = "SELECT * FROM Accounts WHERE Service LIKE '%{}%'".format(serviceName)
    cursor.execute(search)
    results = cursor.fetchall()
    connect.commit()
    if not results:
        return ""
    passw = results[0][0]
    return passw


def find_using_email(email):
    connect = conn()
    cursor = connect.cursor()
    search = 'SELECT * FROM Accounts WHERE Email = "{}"'.format(email)
    cursor.execute(search)
    results = cursor.fetchall()
    connect.commit()
    return results
