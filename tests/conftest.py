"""Test configuration for Data Quality Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "data-quality-agent", "category": "Data Engineering"}
