import pytest
import asyncio
from unittest.mock import patch, MagicMock
from fastapi import FastAPI, Depends
from httpx import AsyncClient, ASGITransport

# --- 1. THE APPLICATION CODE ---
app = FastAPI()


class Database:
    async def get_data(self):
        # Imagine this connects to a real DB
        return "real data"


async def get_db():
    return Database()


@app.get("/data")
async def read_data(db: Database = Depends(get_db)):
    data = await db.get_data()
    return {"data": data}


@app.get("/external")
async def external_call():
    # We will mock this function's internal logic
    return {"status": "real_external_call"}


# --- 2. THE FIXTURES (Async Testing Setup) ---
@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client():
    """Fixture to provide an AsyncClient for every test."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


# --- 3. THE TESTS ---


@pytest.mark.anyio
async def test_dependency_override(client):
    """Demonstrates overriding a FastAPI dependency."""

    # Define a mock/fake database behavior
    async def mock_get_db():
        mock = MagicMock()
        mock.get_data.return_value = "mocked data"
        return mock

    # Apply the override
    app.dependency_overrides[get_db] = mock_get_db

    response = await client.get("/data")

    assert response.status_code == 200
    assert response.json() == {"data": "mocked data"}

    # Clean up overrides after test
    app.dependency_overrides.clear()


@pytest.mark.anyio
async def test_patching_external_call(client):
    """Demonstrates standard patching of a function."""
    with patch("main.external_call") as mock_call:  # Replace 'main' with your filename
        mock_call.return_value = {"status": "mocked_call"}

        # Note: If patching a route directly, it's often better to
        # patch the logic inside the route, not the route itself.
        response = await client.get("/external")
        assert response.json()["status"] == "real_external_call"
        # ^ Patching the route function directly is tricky because
        # FastAPI has already registered the original function.
