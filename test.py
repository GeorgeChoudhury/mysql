import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", password="root", auth_plugin='mysql_native_password')
try:
    if conn.is_connected:
        print("Connected to database")
    else:
        print("Failed to connect")

    crr=conn.cursor()

    st1="""CREATE DATABASE IF NOT EXISTS medicine"""
    st2="""USE medicine"""
    st3="""CREATE TABLE IF NOT EXISTS medicine_details
            (medicine_ID INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(40),
            quantity INT)"""
    l1=[st1,st2,st3]
    for i in l1:
        crr.execute(i)
except mysql.connector.Error as err:
    print(err)

st4="""INSERT INTO medicine_details
        (name,quantity)
        VALUES(%s,%s)"""
val=[
    ("Ampicillin", 50),
    ("Mylotarg",30),
    ("Insulin Regular",40),
    ("Paracetamol",50),
    ("Zolgensma",5)
]
try:
    crr.executemany(st4,val)
except mysql.connector.Error as err:
    print(err)
conn.commit()
conn.close()
temp=0
st5="""SELECT *FROM medicine_details"""
crr.execute(st5)
for db in crr:
    temp+=db[2]
print(temp)
count=0
crr.execute(st5)
for db in crr:
    if db[2]<10:
        print(db)
        count=count+1
print(count)