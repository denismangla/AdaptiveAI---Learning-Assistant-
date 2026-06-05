# Adaptive AI Learning Assistant for Programming Education

This project implements an academic prototype that combines a Python backend with a React + Tailwind frontend to deliver adaptive, confidence-aware programming practice.

## Structure
- `backend/` - FastAPI backend, AI modules, data storage in JSON files.
- `frontend/` - React + Vite application with Tailwind CSS.
- `docs/` - Architecture, scope, report points, and completion documentation.
- `tests/` - Pytest modules for adaptive engine, question generation, analytics, and AI fallback validation.

## Run Instructions
1. Start Ollama locally with `gemma3:1b-it-qat`.
2. Install backend dependencies:
   - `cd backend`
   - `python -m pip install -r requirements.txt`
3. Start the backend:
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
4. Install frontend dependencies:
   - `cd ../frontend`
   - `npm install`
   - `npm run dev`
5. Access the app at `http://localhost:5173`.

## Notes
- The backend stores student profiles and metadata in JSON under `backend/data/`.
- Ollama integration is handled by `backend/app/modules/ollama_client.py`.
- The project runs entirely locally and requires no paid external services.
