from mongoengine import  connect

connect(db='recipe-mongo',username="recipes",password="food",host="172.17.0.2")