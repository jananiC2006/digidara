from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alumni_db"
)
cursor=db.cursor()

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('register_alumni.html')

@app.route('/register_alumni', methods=['GET', 'POST'])
def register_alumni():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        batch = request.form['batch']
        department = request.form['department']
        company = request.form['company']
        position = request.form['position']
        linkedin_url = request.form['linkedin_url']


        cursor.execute('''INSERT INTO alumni_db (name, email, batch, department, company, position, linkedin_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (name, email, batch, department, company, position, linkedin_url))
        db.commit()
        

        return redirect('/alumni')  


@app.route('/alumni')
def alumni_list():
    # db=mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="",
    #         database="alumni_db"
    #     )
    # cursor=db.cursor()
    
    cursor.execute("SELECT * FROM alumni_db WHERE status = 'Approved' ORDER BY submitted_on DESC")
    alumni = cursor.fetchall()
    
    return render_template('alumni_list.html',alumni=alumni)

@app.route('/admin', methods=['GET', 'POST'])
def admin_approval():
    if request.method =='POST':
        alumni_id = request.form['alumni_id']
        status = request.form['status']

        cursor = db.connection.cursor()
        cursor.execute("UPDATE alumni SET status = %s WHERE alumni_id = %s", (status, alumni_id))
        db.connection.commit()
        cursor=db.cursor()
        
   
    cursor.execute("SELECT * FROM alumni ORDER BY submitted_on DESC")
    alumni = cursor.fetchall()
    cursor.close()
    
    return render_template('admin_alumni.html', alumni=alumni)

if __name__ == '__main__':
    app.run(debug=True)