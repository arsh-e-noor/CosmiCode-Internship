import pytest
from app.app import create_app, db

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_loads(client):
    """Test if home page loads successfully."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_crud_flow(client):
    """Test full CRUD flow: create, list, toggle, delete."""
    
    # Create
    rv = client.post('/api/todos', json={'title': 'Buy milk'})
    assert rv.status_code == 201
    todo = rv.get_json()
    assert todo['title'] == 'Buy milk'
    assert todo['done'] is False

    # List
    rv = client.get('/api/todos')
    assert rv.status_code == 200
    todos = rv.get_json()
    assert len(todos) == 1
    todo_id = todos[0]['id']

    # Toggle
    rv = client.put(f'/api/todos/{todo_id}/toggle')
    assert rv.status_code == 200
    assert rv.get_json()['done'] is True

    # Delete
    rv = client.delete(f'/api/todos/{todo_id}')
    assert rv.status_code == 200
    rv = client.get('/api/todos')
    assert rv.get_json() == []
