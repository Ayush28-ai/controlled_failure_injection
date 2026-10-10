
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
from fastapi.responses import Response

from backend.storage.database import init_db
from backend.api.routes import (
    health,
    topology,
    metrics,
    experiments,
    recovery,
    findings,
    planner,
)


HTTP_REQUESTS = Counter(
    "bosch_http_requests_total",
    "Total HTTP requests handled by Bosch API",
    ["method", "path", "status"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Bosch backend starting...")
    init_db()
    yield
    print("Bosch backend shutting down...")


app = FastAPI(
    title="Bosch Resilience Platform",
    description=(
        "Controlled failure testing, service monitoring, "
        "and AI-assisted resilience recommendations."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)

    if request.url.path != "/metrics":
        HTTP_REQUESTS.labels(
            request.method,
            request.url.path,
            str(response.status_code),
        ).inc()

    return response


@app.get("/", tags=["Root"])
def root():
    return {
        "name": "Bosch Resilience Platform",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/metrics", include_in_schema=False)
def prometheus_metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )


API_PREFIX = "/api/v1"

for route_module in (
    health,
    topology,
    metrics,
    experiments,
    recovery,
    findings,
    planner,
):
    app.include_router(
        route_module.router,
        prefix=API_PREFIX,
    )
