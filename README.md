# Bosch — Controlled Failure Injection & Resilience Platform

Bosch is a development platform for exercising a demo e-commerce journey, recording bounded **simulated** failure scenarios, and inspecting service topology, Prometheus metrics, and findings.

> **Safety status:** The current experiment runner is simulation-only. It records experiment metadata but does not stop containers, inject network latency, generate real traffic, or change host/production services. Recovery is therefore a no-op.

## Current stack

- Backend: Python 3.10+, FastAPI, Pydantic, SQLAlchemy
- Persistence: PostgreSQL in Docker Compose; SQLite fallback for local development
- Frontend: React, TypeScript, Vite, React Router
- Observability: Prometheus and the backend `/metrics` endpoint
- Tests: pytest

## Repository layout

The current layout is retained:

- `backend/agents/` — planning, monitoring analysis, and solution recommendations
- `backend/api/routes/` — health, topology, metrics, experiments, findings, recovery, planner
- `backend/experiments/` — scenario registry and simulation runner
- `backend/monitoring/` — Prometheus client, baseline comparison, log analysis
- `backend/orchestration/` — experiment workflow and run manager
- `backend/safety/` — guardrails, watchdog, recovery
- `backend/storage/` — SQLAlchemy models, database, repository
- `frontend/src/pages/store/` — synthetic storefront, products, cart, checkout
- `frontend/src/pages/experiments/` — scenario selection, simulation, impact, recovery
- `frontend/src/pages/observability/` — overview, services, metrics, findings, history
- `monitoring/prometheus/` — Prometheus scrape configuration
- `tests/` — backend test suite

## Run locally

### 1. Backend

From the repository root:

```bash
python -m venv .venv
# Linux/macOS/WSL
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

pip install -e ".[dev]"
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The backend uses `sqlite:///./bosch.db` when `DATABASE_URL` is not set. API docs are at `http://localhost:8000/docs`.

### 2. Frontend

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. To point to a different backend, create `frontend/.env.local`:

```dotenv
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

Vite exposes only variables prefixed with `VITE_` to browser code. Never put API keys or secrets in frontend environment variables.

### 3. Full stack with Docker Compose

Copy `.env.example` to `.env`, change the local development database password if needed, then run:

```bash
docker compose up --build
```

Services:

| Service | URL |
| --- | --- |
| Frontend | `http://localhost:5173` |
| Backend | `http://localhost:8000` |
| Swagger docs | `http://localhost:8000/docs` |
| Prometheus | `http://localhost:9090` |
| PostgreSQL | `localhost:5432` |

The Compose file passes service-to-service URLs to containers. Prometheus scrapes `api:8000`, which is the Compose service name.

## API overview

The versioned API prefix is `/api/v1`.

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Backend health response |
| `GET /topology` | Demo services and dependency edges |
| `GET /metrics` | Approved metric names |
| `GET /metrics/{metric_name}` | Execute one approved Prometheus query |
| `GET /experiments` | List saved experiment records |
| `POST /experiments` | Validate and record a simulation |
| `GET /experiments/{id}` | Read one experiment |
| `POST /planner/propose` | Suggest a scenario from a symptom |
| `GET /findings` / `POST /findings` | Read and save findings |
| `POST /recovery/{id}` | Return simulation recovery status |

The unversioned `GET /metrics` endpoint at the root of the API server is Prometheus's scrape endpoint and is intentionally separate from `/api/v1/metrics`.

## Run tests

From the repository root:

```bash
pytest
```

Optional lint:

```bash
ruff check backend tests
```

## Current limitations and next steps

- The experiment runner is a simulation; no real fault injection is implemented.
- Service health currently reflects the backend health endpoint and configured topology, not active probes of every dependency.
- Prometheus queries may return no series until the relevant metrics are scraped. Missing data should be treated as unavailable, not zero.
- Findings are persisted records; they are not automatically generated from every experiment yet.
- The planner currently uses deterministic rules; it is not yet calling an LLM.
- The storefront uses synthetic products and browser-local cart state. Checkout does not create an order or process a payment.
- For shared/team environments, replace development secrets, restrict exposed ports, add migrations, and add authentication before deployment.

## Development safety

Use only systems you own or have explicit authorization to test. Keep the current simulation mode as the default. Any future real fault-injection adapter should be isolated behind explicit allowlists, duration limits, an environment-level kill switch, audit logs, and verified cleanup.
