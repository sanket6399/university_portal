import pytest
from flask import Flask
import sys
import os

# Assuming the tests directory is one level below the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from app import app, courses

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Available Courses" in response.data

def test_contact_us(client):
    response = client.post('/contact', data={'name': 'John Doe', 'email': 'john@example.com', 'message': 'Hello'})
    assert response.status_code == 200
    assert b"Contact Form Submission" in response.data
    assert b"Name: John Doe" in response.data
    assert b"Email: john@example.com" in response.data
    assert b"Message: Hello" in response.data

def test_invalid_contact_us(client):
    response = client.post('/contact', data={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 400
    assert b"Invalid form data" in response.data

def test_valid_course_details(client):
    course_name = 'Computer Science'
    response = client.get(f'/course_details/{course_name}')
    assert response.status_code == 200
    assert f"{course_name} Details" in response.data.decode('utf-8')

def test_invalid_course_details(client):
    course_name = 123  # Invalid course name
    response = client.get(f'/course_details/{course_name}')
    assert response.status_code == 404

def test_valid_cost_details(client):
    course_name = 'Computer Science'
    response = client.get(f'/cost/{course_name}')
    assert response.status_code == 200
    assert b"cost" in response.data

def test_invalid_cost_details(client):
    course_name = 123  # Invalid course name
    response = client.get(f'/cost/{course_name}')
    assert response.status_code == 404

def test_nonexistent_course_details(client):
    course_name = 'Nonexistent Course'
    response = client.get(f'/course_details/{course_name}')
    assert response.status_code == 404

def test_nonexistent_cost_details(client):
    course_name = 'Nonexistent Course'
    response = client.get(f'/cost/{course_name}')
    assert response.status_code == 404
