# Multi-Agent Market Research and GTM Planning

## Project Overview

This project implements a multi-agent workflow for automated market research and go-to-market planning. The system uses CrewAI and n8n to compare two different agent orchestration approaches.

The workflow includes four main agents:

1. Head Planner Agent
2. Market Research Agent
3. Market Analyst Agent
4. Strategy Agent

The final output is a structured GTM report that can be exported to Google Docs or uploaded to Google Drive.

---

## Problem Statement

Product teams often spend days manually researching markets, reviewing competitors, and drafting GTM plans. This process can be slow, inconsistent, and error-prone.

This project solves the problem by using a multi-agent system to automate:

- Market research
- Competitor analysis
- Pricing comparison
- SWOT analysis
- GTM strategy creation
- Final report generation

## MCP Server Integration

A lightweight MCP-style FastAPI server was implemented to expose research tools as reusable HTTP endpoints.

The MCP server provides:
- Web search capability
- Centralized tool access
- Reusable integration for both CrewAI and n8n workflows

CrewAI agents accessed MCP tools through Python tool wrappers, while n8n accessed the same MCP endpoints through HTTP Request nodes.

Example endpoint:

GET /search?query=AI LMS market

This architecture allowed both implementations to share the same research infrastructure.

---

## Architecture

```text
User Product Brief
      ↓
Head Planner Agent
      ↓
Market Research Agent
      ↓
Market Analyst Agent
      ↓
GTM Strategy Agent
      ↓
Documenter
      ↓
Google Docs / Google Drive Output