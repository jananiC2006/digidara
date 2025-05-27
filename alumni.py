from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
alumni=Flask(__name__)
alumni.config['MYSQL_HOST']='localhost'
alumni.config['MYSQL_USER']='root'
alumni.config['MYSQL_PASSWORD']='yourpassword'
alumni.config['MYSQL_DB']='alumni_db'

mysql=MySQL(alumni)

@alumni.route('/register',method=['GET','POST'])
def register_alumni():
        if request.method=='POST':
                data=(
                  request.form['name'],
                  request.form['email'],
                  request.form['batch'],
                  request.form['department'],
                  request.form['company'],
                  request.form['position'],
                  request.form['linkedin_url']
                )
                cur=mysql.connection.cursor()
                cur.execute('''INSERT INTO alumni(name,email,batch,department,company,position,linked_url)
                            VALUES(%s,%s,%s,%s,%s,%s,%s)''',data)
                mysql.connection.commit()
                return "Thank you for registering!"
        return render_template('register_alumni.html')

@alumni.route('/alumni')
def alumni_list():
        cur=mysql.connection.cursor()
        cur.execute("SELECT*FROM alumni WHERE status='Approved'ORDER BY submitted_on DESC")
        alumni=cur.fetchall()
        return render_template('alumni-list.html',alumni=alumni)

@alumni.route('/admin',methods=['GET','POST'])
def admin_approval():
        if request.method=='POST':
                alumni_id=request.form['alumni_id']
                status=request.form['status']
                cur=mysql.connection.cursor()
                cur.execute("UPDATE alumni SET status=%s WHERE alumni_id=%s",(status,alumni_id))
                mysql.connection.commit()
        cur=mysql.connection.cursor()
        cur.execute("SELECT*FROM alumni ORDER BY submitted_on DESC")
        alumni=cur.fetchall()
        return render_template('admin_alumni.html',alumni=alumni)

