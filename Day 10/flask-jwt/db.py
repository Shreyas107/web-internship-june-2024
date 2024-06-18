from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_DB'] = "intern"
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = "shreyas"
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PORT'] = 3306

    mysql.init_app(app)
    return mysql
