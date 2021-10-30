import mysql.connector

db = mysql.connector.connect(
    host="bzzjfyftctulzq8snonn-mysql.services.clever-cloud.com",
    user="ubbrfehac6hrccub",
    passwd="Jd2tANFBeUnMXdOU8iE7",
    database="bzzjfyftctulzq8snonn")

mycursor = db.cursor()