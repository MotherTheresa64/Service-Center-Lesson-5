# Lesson 5: API Deployment with Render & GitHub Actions

## Overview
In this lesson you'll:
1. Configure Flask for production  
2. Host a PostgreSQL database on Render  
3. Secure secrets with `.env` & GitHub Secrets  
4. Deploy via Gunicorn on Render  
5. Automate CI/CD with GitHub Actions  

## Folder Layout

Lesson5_API_Deployment_CICD/
├── flask_app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile
├── README.md
├── application/
│ └── … your blueprints & models …
├── static/swagger.yaml
├── tests/
│ └── … your unit tests …
└── .github/workflows/main.yml