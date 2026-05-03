# PDF AI Agent
A project with a FastAPI backend and React frontend.

---
## 📁 Project Structure

```bash
backend/ # FastAPI app
frontend/ # React app
```

---
## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf_ai_agent.git
cd pdf_ai_agent
```

### 2. Backend (FastAPI) Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

### 4. Run server
```bash
fastapi dev app/main.py
```
Backend runs at http://127.0.0.1:8000

### 5. Frontend (React) Setup and Run
```bash
cd frontend
npm install
npm start
```

Frontend runs at http://localhost:3000

### 6. Environment Variables
Create a file:
frontend/.env

REACT_APP_BASE_API_URL=http://127.0.0.1:8000

### 7. Running Tests

Backend
```bash
cd backend
pytest
```

Frontend
```bash
cd frontend
npm test
```
