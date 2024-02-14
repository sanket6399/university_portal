# CS218 Cloud Computing Assignment - University Portal REST API

## Overview
This repository hosts the REST API for a University Portal, developed for CS218 Cloud Computing. The API, which is containerized using Docker, is deployed on an AWS EC2 instance. CircleCI is utilized for continuous integration to ensure code integrity and automated testing.

## Project Structure
- `.circleci`: Configuration for CircleCI integration.
- `static`: Static assets such as CSS, JavaScript, and images.
- `templates`: HTML templates for rendering views.
- `tests`: Test cases for the API endpoints.
- `Dockerfile`: Docker configuration for building the application container.
- `app.py`: The Flask application with RESTful API endpoints.
- `requirements.txt`: Required Python packages for the project.

## Getting Started

### Prerequisites
- Docker installed on your local machine.
- AWS account with EC2 set up.

### Installation and Local Setup
1. Clone the repository to your local machine:
2. Navigate to the project directory:
3. Build the Docker image:
4. Run the application in a Docker container:

## Deployment on AWS EC2
1. Launch an AWS EC2 instance and SSH into it.
2. Install Docker on the EC2 instance.
3. Pull the Docker image from Docker Hub or build it using the Dockerfile.
4. Run the Docker container on the EC2 instance.

## Continuous Integration with CircleCI
- Commit changes trigger automated builds and tests via CircleCI.
- The CircleCI configuration is located in `.circleci/config.yml`.

## Contributing
Please follow the steps below to contribute to this project:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
- Thanks to the CS218 course staff and students for their support and collaboration.

## Contact Information
- Your Name - sanket.kulkarni@sjsu.edu

---
