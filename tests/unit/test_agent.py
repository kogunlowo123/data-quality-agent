"""Data Quality Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_define_expectations():
    """Test Define data quality expectations for a dataset."""
    tools = AgentTools()
    result = await tools.define_expectations(dataset="test", expectations="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_run_quality_checks():
    """Test Run data quality checks against a dataset."""
    tools = AgentTools()
    result = await tools.run_quality_checks(dataset="test", expectation_suite="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_anomalies():
    """Test Detect anomalies in data volume, distribution, or freshness."""
    tools = AgentTools()
    result = await tools.detect_anomalies(dataset="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_measure_freshness():
    """Test Measure data freshness and SLA compliance."""
    tools = AgentTools()
    result = await tools.measure_freshness(dataset="test", sla_minutes=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.data_quality_agent_agent import DataQualityAgentAgent
    agent = DataQualityAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
