[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Prompts System Revamp (Open Source)

Overview
- A clean, extensible MVP for a Prompt Catalog with Versioning, Guardrails/Observability, and Auditability.
- Tech stack: Python FastAPI backend with in-memory stores for MVP, and a React/TypeScript frontend with a minimal in-memory store for UI MVP.
- Tests: pytest-based backend tests and Jest-based frontend tests.
- Conventions: MIT license, plan for governance, MoSCoW-based backlog in planning documents.

How to run
- Prerequisites: Python 3.11+, Node.js 18+, Poetry or venv. See backend/ and frontend/ for details.
- Backend
  1) cd backend
  2) python -m venv venv
  3) source venv/bin/activate (./venv/Scripts/activate on Windows)
  4) pip install -r requirements.txt
  5) uvicorn app.main:app --reload --port 8000
- Frontend
  1) cd frontend
  2) npm install
  3) npm run dev (Vite dev server)
- Tests
  - Backend: pytest
  - Frontend: npm test (Jest)

Architecture at a glance
- Backend: FastAPI with in-memory models for Prompt, Version, and AuditEvent. Lightweight telemetry logging mirrors a real observability plan (logs, metrics, traces) without external dependencies.
- Frontend: React with a small PromptStore-like pattern in memory. Components include PromptList, PromptEditor, VersionHistoryPanel, and an AuditTrail view.
- Data models map to the Synthesis Strategy in the Council design and align with the described data contracts (Prompt, Version, AuditEvent).

Open Source & License
- This project is MIT-licensed. Contributions welcome.

References
- Related OSS artifacts that inspired this design: Sfedfcv/redesigned-pancake (UI/UX integration-heavy repository) and HH (complex Python tooling) as examples of progressive open-source architecture.

References (links)
- https://github.com/Sfedfcv/redesigned-pancake
- https://github.com/HH
