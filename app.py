from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = {
    "Computer Science": {"cost": 5000, "duration": "4 years"},
    "Mechanical Engineering": {"cost": 4500, "duration": "4 years"},
    "Business Administration": {"cost": 4000, "duration": "3 years"},
    "Electrical Engineering": {"cost": 4800, "duration": "4 years"},
    "Psychology": {"cost": 3500, "duration": "3 years"},
    "Civil Engineering": {"cost": 4700, "duration": "4 years"},
    "Marketing": {"cost": 3800, "duration": "3 years"},
    "Physics": {"cost": 4200, "duration": "3 years"},
    "Information Technology": {"cost": 5200, "duration": "4 years"},
}

def validate_course_name(course_name):
    if not isinstance(course_name, str):
        return False
    # Add any additional checks for valid course names if needed
    return True

def validate_cost(cost):
    if not isinstance(cost, int):
        return False
    # Add any additional checks for valid cost values if needed
    return True

@app.route('/')
def index():
    # Pass the entire courses dictionary to the template
    return render_template('index.html', courses=courses)

@app.route('/contact', methods=['POST'])
def contact_us():
    data = request.form
    if 'name' not in data or 'email' not in data or 'message' not in data:
        return jsonify({"error": "Invalid form data"}), 400  # 400 Bad Request
    return render_template('contact_response.html', data=data)

@app.route('/course_details/<course_name>', methods=['GET'])
def get_course_details(course_name):
    if not validate_course_name(course_name):
        return jsonify({"error": "Invalid course name"}), 400  # 400 Bad Request

    course = courses.get(course_name)
    if course:
        return render_template('course_details.html', course_name=course_name, course=course)
    else:
        return jsonify({"error": "Course not found"}), 404

@app.route('/cost/<course_name>', methods=['GET'])
def get_cost_details(course_name):
    if not validate_course_name(course_name):
        return jsonify({"error": "Invalid course name"}), 400  # 400 Bad Request

    course = courses.get(course_name)
    if course:
        return render_template('cost_details.html', course_name=course_name, cost=course["cost"])
    else:
        return jsonify({"error": "Course not found"}), 404

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": "Internal Server Error"}), 500  # 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
