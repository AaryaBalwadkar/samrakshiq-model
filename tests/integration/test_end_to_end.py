import pytest
import httpx

@pytest.mark.asyncio
async def test_end_to_end():
    url = "http://localhost:8000/api/messages"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        assert response.status_code == 200
        data = response.json()
        assert "messages" in data and "metrics" in data

        redacted_text = data["messages"][0]["text"]
        assert "[REDACTED]" in redacted_text or "[PHONE_HASH]" in redacted_text