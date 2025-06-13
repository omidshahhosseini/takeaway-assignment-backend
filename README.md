# Takeaway Backend API

A FastAPI-based backend service for the Takeaway application, providing endpoints for managing favorites and handling webhooks.

## 🚀 Features

- RESTful API endpoints for managing user favorites
- Webhook handling for real-time updates
- CORS support for cross-origin requests
- Environment-based configuration
- Health check endpoint
- Supabase integration for data persistence

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.112.1
- **Server**: Uvicorn 0.30.6
- **Database**: Supabase (for storing user favorite restaurants)
- **Environment Management**: python-dotenv
- **HTTP Client**: httpx
- **Webhook Handling**: svix
- **Data Validation**: pydantic

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)
- Supabase account and project

## 🔧 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd takeaway-assignment-backend
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory. Copy all the environment variables (with their values) from the .env.backend file that was provided to you in the email.

## 🚀 Running the Application

### Development Mode

```bash
uvicorn main:app --reload
```

### Production Mode

```bash
uvicorn main:app
```

The API will be available at `http://localhost:8000` or `http://127.0.0.1:8000`

## 📚 API Documentation

The API is deployed and available at: [https://takeaway-assignment-backend.vercel.app/docs](https://takeaway-assignment-backend.vercel.app/docs)

For local development, once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

### Main Endpoints

- `/api/v1/favorites` - Manage user favorites
- `/webhooks` - Handle incoming webhooks
- `/health` - Health check endpoint

## 🔒 CORS Configuration

The API is configured to accept requests from the following origins:

- http://localhost:3000
- http://localhost:5173
- https://takeaway-assignment-backend.vercel.app/

## 🚀 Deployment

The application is deployed on Vercel and can be accessed at [https://takeaway-assignment-backend.vercel.app](https://takeaway-assignment-backend.vercel.app). The deployment is configured using the `vercel.json` configuration file.

## 💾 Database

This project uses Supabase to store user favorite restaurants. The database stores user preferences and their favorite restaurant selections.