# Schedule Advisor Web App

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Technology Stack](#technology-stack)
5. [Installation and Setup](#installation-and-setup)
6. [Database Migration](#database-migration)
7. [Deployment](#deployment)
8. [Testing](#testing)
9. [Performance Tuning](#performance-tuning)
10. [Security Measures](#security-measures)
11. [Contribute and Issues](#contribute-and-issues)
12. [License](#license)

---

## Introduction

The Schedule Advisor Web App is designed to optimize and provide intelligent recommendations for academic schedules. Built on Django and backed by a PostgreSQL database, it was initially deployed on Heroku.

---

## Features

- Schedule Optimization Algorithm
- Faculty and Course Database
- User Authentication
- Mobile-Responsive Design

---

## Prerequisites

- Python 3.8+
- pip
- PostgreSQL 12+
- Virtualenv (optional)

---

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: PostgreSQL
- **Deployment**: Heroku (initially), Docker (optional)

---

## Installation and Setup

\`\`\`bash
# Clone repository
git clone https://github.com/davidxiang101/Schedule-Advisor.git
# Change directory
cd schedule-advisor
# Create a virtual environment
virtualenv venv
# Activate virtual environment
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
\`\`\`

---

## Database Migration

\`\`\`bash
# Create the database in PostgreSQL
createdb your_database_name
# Run migrations
python manage.py migrate
# Create superuser
python manage.py createsuperuser
\`\`\`

---

## Deployment

- **Heroku**: Follow Heroku's Django deployment guide.
- **AWS EC2**: Consider EC2 with an Nginx reverse proxy for scalability.
- **Docker**: Containerize the app for environment-agnostic deployments.

---

## Testing

- **Unit Tests**: \`python manage.py test\`
- **Load Testing**: Use Apache JMeter or Artillery for load testing.

---

## Performance Tuning

- Utilize Django's built-in caching mechanism.
- For larger deployments, consider load balancing.
- Leverage CDN for static assets.

---

## Security Measures

- Employ \`django-secure\` for enhanced security headers.
- SQL injection: Django ORM provides a safeguard; no extra action needed.

---

