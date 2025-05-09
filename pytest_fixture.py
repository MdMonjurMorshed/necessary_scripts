# pytest fixture is used where we need a dependency to run a test
import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_sample(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
