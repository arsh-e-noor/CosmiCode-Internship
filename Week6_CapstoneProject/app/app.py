import os
import time
from datetime import datetime
from flask import Flask, render_template, request, jsonify, g, Response
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

db = SQLAlchemy()

# Prometheus metrics
TODO_CREATED = Counter('todo_created_total', 'Total TODOs created')
TODO_DELETED = Counter('todo_deleted_total', 'Total TODOs deleted')
TODO_TOGGLED = Counter('todo_toggled_total', 'Total TODOs toggled')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['method', 'endpoint'])

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done,
            'created_at': self.created_at.isoformat()
        }

def create_app(test_config=None):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    # default: sqlite for easy local dev; Docker Compose will override via DATABASE_URL env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///./dev.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    @app.before_request
    def start_timer():
        g.start_time = time.time()

    @app.after_request
    def record_latency(response):
        try:
            REQUEST_LATENCY.labels(request.method, request.path).observe(time.time() - g.start_time)
        except Exception:
            pass
        return response

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/todos', methods=['GET'])
    def list_todos():
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return jsonify([t.to_dict() for t in todos])

    @app.route('/api/todos', methods=['POST'])
    def create_todo():
        data = request.get_json() or {}
        title = data.get('title', '').strip()
        if not title:
            return jsonify({'error': 'title required'}), 400
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
        TODO_CREATED.inc()
        return jsonify(todo.to_dict()), 201

    @app.route('/api/todos/<int:todo_id>/toggle', methods=['PUT'])
    def toggle_todo(todo_id):
        todo = Todo.query.get_or_404(todo_id)
        todo.done = not todo.done
        db.session.commit()
        TODO_TOGGLED.inc()
        return jsonify(todo.to_dict())

    @app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        TODO_DELETED.inc()
        return jsonify({'result': 'deleted'})

    @app.route('/healthz')
    def healthz():
        return jsonify({'status': 'ok'})

    @app.route('/metrics')
    def metrics():
        # Serve Prometheus metrics
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    # ensure tables exist on startup (easy for dev)
    with app.app_context():
        db.create_all()

    return app
