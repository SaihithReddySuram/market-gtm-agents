from crewai import Task
from agents import research_agent, analyst_agent, strategy_agent, head_planner_agent


def create_research_task(product_brief: str):
    return Task(
        description=f"""
        Research the following product/business idea:

        {product_brief}

        Collect evidence for:
        1. Target market
        2. Customer pain points
        3. Competitors
        4. Pricing examples
        5. Market trends
        6. GTM opportunities

        Use the search tool multiple times with different queries.

        Return the final answer as valid JSON with this structure:

        {{
          "product_brief": "...",
          "research_questions": [
            {{
              "question": "...",
              "answer": "...",
              "sources": [
                {{
                  "title": "...",
                  "url": "...",
                  "evidence": "..."
                }}
              ]
            }}
          ],
          "competitors": [
            {{
              "name": "...",
              "website": "...",
              "positioning": "...",
              "pricing_info": "...",
              "source_url": "..."
            }}
          ],
          "key_insights": [
            "insight 1",
            "insight 2",
            "insight 3"
          ]
        }}
        """,
        expected_output="A valid JSON market research evidence report with citations.",
        agent=research_agent,
        output_file="outputs/research_evidence.json"
    )


def create_analyst_task(product_brief: str, research_context_task):
    return Task(
        description=f"""
        Analyze the research evidence for this product:

        {product_brief}

        Use the research evidence from the previous task.

        Create a structured analysis with:

        1. Competitor Table
           - Competitor name
           - Website
           - Target customer
           - Main features
           - Pricing information
           - Strengths
           - Weaknesses
           - Source URL

        2. Pricing Matrix
           - Competitor
           - Free plan available?
           - Starting price
           - Pricing model
           - Notes

        3. SWOT Analysis
           - Strengths
           - Weaknesses
           - Opportunities
           - Threats

        4. 4P Marketing Analysis
           - Product
           - Price
           - Place
           - Promotion

        5. Key GTM Insights
           - Best target customer segment
           - Main pain points
           - Market gap
           - Differentiation opportunity
           - Risks

        Return the answer in clean markdown.
        """,
        expected_output=(
            "A markdown market analysis report with competitor table, pricing matrix, "
            "SWOT, 4P analysis, and GTM insights."
        ),
        agent=analyst_agent,
        context=[research_context_task],
        output_file="outputs/market_analysis.md"
    )

def create_strategy_task(product_brief: str, analyst_context_task):
    return Task(
        description=f"""
        Create a go-to-market strategy for this product:

        {product_brief}

        Use the market analysis from the previous task.

        Create a structured GTM plan with:

        1. Executive Summary

        2. Ideal Customer Profile
           - Primary ICP
           - Secondary ICP
           - Buyer personas
           - User personas

        3. Value Proposition
           - Main value proposition
           - Key benefits
           - Differentiation

        4. Positioning Statement

        5. Messaging Framework
           - Tagline
           - Elevator pitch
           - Pain-point messaging
           - Feature-to-benefit mapping

        6. Channel Strategy
           - Organic channels
           - Paid channels
           - Partnerships
           - Sales channels

        7. Launch Plan
           - Pre-launch
           - Launch
           - Post-launch

        8. Success Metrics
           - Awareness metrics
           - Acquisition metrics
           - Activation metrics
           - Retention metrics
           - Revenue metrics

        9. Risks and Mitigations

        Return the answer in clean markdown.
        """,
        expected_output="A complete markdown GTM strategy plan.",
        agent=strategy_agent,
        context=[analyst_context_task],
        output_file="outputs/gtm_strategy.md"
    )

def create_head_planner_task(
    product_brief: str,
    research_context_task,
    analyst_context_task,
    strategy_context_task
):
    return Task(
        description=f"""
        Create the final market research and GTM planning document for:

        {product_brief}

        Use all previous outputs:
        - Research evidence
        - Market analysis
        - GTM strategy

        Your job:
        1. Combine everything into one polished final report.
        2. Remove duplicate content.
        3. Keep the structure clear and professional.
        4. Include citations/source URLs from the research output.
        5. Highlight assumptions and risks.
        6. Add an implementation roadmap.
        7. Add a short comparison-ready summary for n8n vs CrewAI.

        Final document structure:

        # Market Research and GTM Plan

        ## 1. Executive Summary

        ## 2. Product Brief

        ## 3. Research Evidence Summary

        ## 4. Target Market

        ## 5. Customer Pain Points

        ## 6. Competitor Analysis

        ## 7. Pricing Matrix

        ## 8. SWOT Analysis

        ## 9. 4P Marketing Analysis

        ## 10. Ideal Customer Profile

        ## 11. Value Proposition

        ## 12. Positioning and Messaging

        ## 13. Channel Strategy

        ## 14. Launch Plan

        ## 15. Success Metrics

        ## 16. Risks and Mitigations

        ## 17. Implementation Roadmap

        ## 18. Source List

        ## 19. n8n vs CrewAI Comparison Notes

        Return the answer in clean markdown.
        """,
        expected_output="A polished final markdown GTM report with sources and roadmap.",
        agent=head_planner_agent,
        context=[
            research_context_task,
            analyst_context_task,
            strategy_context_task
        ],
        output_file="outputs/final_gtm_report.md"
    )