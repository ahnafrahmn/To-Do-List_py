# FastAPI To-Do Backend

A production-ready REST API built with FastAPI, featuring JWT authentication, user-scoped data access, and clean layered architecture.

## Live Demo
https://to-do-fastapi-3del.onrender.com

## Features
- JWT-based authentication (register / login)
- Secure password hashing (bcrypt)
- User-scoped task CRUD (no cross-user access)
- FastAPI + SQLAlchemy ORM
- Dependency injection & service layer separation
- Deployed on Render

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite (local)
- JWT
- Poetry
- Render

## API Endpoints
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/tasks`
- `POST /api/v1/tasks`
- `PUT /api/v1/tasks/{id}`
- `DELETE /api/v1/tasks/{id}`
