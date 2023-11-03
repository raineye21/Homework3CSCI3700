# Code to update basket_a

from flask import Flask, render_template
import util


app = Flask(__name__)
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'
# route to map a URL with a Python function
# address: ip:port/127.0.0.1:5000/
@app.route("/api/update_basket_a")

def index():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # commands
    record = util.run_and_commit_sql(cursor, connection, sql_string="INSERT INTO basket_a VALUES(5, 'Cherry');")
    if record == -1:
        log = 'Error'
        print('Error')
    else:
        log = 'Success'
        print('Success')

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
    app.debug = True
    # local ip
    ip = '127.0.0.1'
    app.run(host=ip)
    
