from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)


# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='rootpass',
        database='todo_db'
    )
    return conn


@app.route('/')
def home():
    return "Welcome to the Dockerized Flask ToDo App!"


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        task = data.get('task')
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        return jsonify({'message': 'Task added successfully!'})

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    return jsonify([{'id': row[0], 'task': row[1]} for row in rows])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
