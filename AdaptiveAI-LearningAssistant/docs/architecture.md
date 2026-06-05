# Architecture

The Adaptive AI Learning Assistant is structured as a local full-stack prototype.

- **Backend**: FastAPI serving endpoints for login, topic selection, question generation, answer evaluation, and analytics.
- **AI modules**: Python modules that integrate with Ollama for NLP generation and fallback logic.
- **Frontend**: React + Vite + Tailwind CSS rendering login, dashboard, topic selection, question screens, result screens, and analytics.
- **Storage**: JSON files for topic hierarchies, learning objectives, dependency maps, difficulty frameworks, and student profiles.

The system uses hierarchical questioning levels and confidence-aware adaptive rules to personalize the learning flow.
