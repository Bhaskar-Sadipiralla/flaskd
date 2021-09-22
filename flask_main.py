import mysql.connector
from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='flask-mysql-db.cb3zak9nxoba.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='Awsdevops123'
app.config['MYSQL_DB']='flaskvmdb'
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template("form.html")
@app.route("/users")
def users():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * FROM users")
    if result>0:
        userDetails=cur.fetchall()
        return render_template("users.html",userDetails=userDetails)

if __name__=='__main__':
   app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
   # app.run(debug=True)
