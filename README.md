# Data Quality Agent

[![CI](https://github.com/kogunlowo123/data-quality-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/data-quality-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Data quality monitoring agent that defines and enforces data quality rules, detects anomalies, measures data freshness, validates completeness and accuracy, and generates data quality scorecards.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `define_expectations` | Define data quality expectations for a dataset |
| `run_quality_checks` | Run data quality checks against a dataset |
| `detect_anomalies` | Detect anomalies in data volume, distribution, or freshness |
| `measure_freshness` | Measure data freshness and SLA compliance |
| `generate_scorecard` | Generate a data quality scorecard for stakeholders |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/quality/expectations` | Define expectations |
| `POST` | `/api/v1/quality/check` | Run quality checks |
| `POST` | `/api/v1/quality/anomalies` | Detect anomalies |
| `GET` | `/api/v1/quality/freshness` | Measure freshness |
| `POST` | `/api/v1/quality/scorecard` | Generate scorecard |

## Features

- Quality Rules
- Anomaly Detection
- Freshness Monitoring
- Completeness Checks
- Quality Scoring

## Integrations

- Great Expectations
- Soda Core
- Dbt Tests
- Monte Carlo
- Elementary

## Architecture

```
data-quality-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── data_quality_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Great Expectations + Soda + dbt Tests + Monte Carlo**

---

Built as part of the Enterprise AI Agent Platform.
