#code to show unique fruits

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
@app.route("/api/unique")

def index():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # commands
    record = util.run_and_fetch_sql(cursor, "SELECT a, fruit_a, b, fruit_b FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b WHERE a IS NULL OR b IS NULL;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        connection.commit()
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    
    return render_template('index.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
    app.debug = True
    # local ip
    ip = '127.0.0.1'
    app.run(host=ip)
