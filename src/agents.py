from crewai import Agent
from tools import mcp_search


research_agent = Agent(
    role="Market Research Agent",
    goal=(
        "Find reliable market, competitor, customer, and industry evidence "
        "for a go-to-market strategy."
    ),
    backstory=(
        "You are a careful market researcher. You collect evidence from credible "
        "sources, prefer primary or top-tier sources, and always include citations."
    ),
    tools=[mcp_search],
    verbose=True,
    allow_delegation=False
)

analyst_agent = Agent(
    role="Market Analyst Agent",
    goal=(
        "Analyze research evidence and convert it into competitor tables, "
        "SWOT analysis, pricing matrix, and GTM insights."
    ),
    backstory=(
        "You are a strategic market analyst. You identify patterns, compare competitors, "
        "summarize market gaps, and create structured analysis for GTM planning."
    ),
    verbose=True,
    allow_delegation=False
)

strategy_agent = Agent(
    role="GTM Strategy Agent",
    goal=(
        "Create a practical go-to-market strategy using research evidence "
        "and market analysis."
    ),
    backstory=(
        "You are a GTM strategist. You turn market research and competitor analysis "
        "into ICPs, positioning, messaging, channels, and launch plans."
    ),
    verbose=True,
    allow_delegation=False
)

head_planner_agent = Agent(
    role="Head Planner",
    goal=(
        "Orchestrate the full market research and GTM workflow, review all outputs, "
        "and produce the final structured strategy document."
    ),
    backstory=(
        "You are the lead planner and documenter. You combine research evidence, "
        "market analysis, and GTM strategy into a polished final report with clear sections, "
        "citations, assumptions, and next steps."
    ),
    verbose=True,
    allow_delegation=False
)