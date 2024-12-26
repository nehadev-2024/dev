from flask import Flask, render_template,request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = '18e4bbc0c2ca027d8d4be317e7e1baa0'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'       
app.config['MYSQL_USER'] = 'root'           
app.config['MYSQL_PASSWORD'] = 'root'    
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route("/hello")
def hello():
    return "<p>Hello World!</p>"

@app.route("/users")
def get_users():
    try:
        cur = mysql.connection.cursor()
        #Query
        cur.execute("SELECT id, name, email from users")
        users = cur.fetchall()
        cur.close()
        return render_template('users.html', users=users)
    except Exception as e:
        return f"An error occured: {str(e)}"
    
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash("Name and Email are required!", "error")
        else:
            try:
                # Insert into database
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
                mysql.connection.commit()
                cur.close()
                flash("User added successfully!", "success")
                return redirect(url_for('new_user'))
            except Exception as e:
                flash(f"An error occurred: {str(e)}", "error")
    
    return render_template('new_user.html')

@app.route('/users/<int:id>')
def get_user(id):
    try:
        cur = mysql.connection.cursor()
        # Query to retrieve the user with the specific ID
        cur.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        cur.close()

        if user:
            # If user exists, render user details
            return render_template('user_detail.html', user=user)
        else:
            # If user is not found
            return f"User with ID {id} not found", 404
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)