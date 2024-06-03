import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="l1o2v3e4"
)

mycursor = mydb.cursor()

mycursor.execute('use grafana')


print(mycursor.rowcount, "record inserted.")


def push(name,age,output):
  
  
    with open("out.png", "rb") as file:
        image_data = file.read()

    
    sql = "INSERT INTO patient (name, age , image,tumor) VALUES (%s, %s , %s , %s)"
    val = (name,age,image_data,output )
    mycursor.execute(sql, val)
    mydb.commit()
    
# push('mari',20,'tumor')





# '''
#     Sql Qurey


#     CREATE TABLE patient (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255),
#         age INT,
#         image LONGBLOB,
#         tumer VARCHAR(255),
#     );
# '''