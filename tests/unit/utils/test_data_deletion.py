import pytest
from src.utils.data_deletion import delete_data

def test_data_deletion():
    test_data = {"phone": "+919876543210", "id": "SBI-1234"}
    result = delete_data(test_data)
    assert result is None, "Deletion should return None"
    assert not test_data, "Data should be empty after deletion"