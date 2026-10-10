
from fastapi import APIRouter

router = APIRouter(prefix="/topology", tags=["Topology"])

SERVICES = [
    {
        "id": "store-web",
        "name": "Store Frontend",
        "type": "frontend",
    },
    {
        "id": "store-api",
        "name": "Store API",
        "type": "application",
    },
    {
        "id": "store-db",
        "name": "Store Database",
        "type": "database",
    },
    {
        "id": "payment-mock",
        "name": "Payment Mock",
        "type": "dependency",
    },
]

DEPENDENCIES = [
    {"source": "store-web", "target": "store-api"},
    {"source": "store-api", "target": "store-db"},
    {"source": "store-api", "target": "payment-mock"},
]


@router.get("")
def get_topology():
    return {
        "services": SERVICES,
        "dependencies": DEPENDENCIES,
    }
