from crewai import Crew, Process
from tasks import (
    create_research_task,
    create_analyst_task,
    create_strategy_task,
    create_head_planner_task
)
from google_docs_writer import create_google_doc_from_markdown


def run_full_gtm_workflow():
    product_brief = """
    Create a market research and GTM plan for an AI-powered LMS SaaS
    for small and mid-sized schools.
    """

    research_task = create_research_task(product_brief)
    analyst_task = create_analyst_task(product_brief, research_task)
    strategy_task = create_strategy_task(product_brief, analyst_task)

    head_planner_task = create_head_planner_task(
        product_brief=product_brief,
        research_context_task=research_task,
        analyst_context_task=analyst_task,
        strategy_context_task=strategy_task
    )

    crew = Crew(
        agents=[
            research_task.agent,
            analyst_task.agent,
            strategy_task.agent,
            head_planner_task.agent
        ],
        tasks=[
            research_task,
            analyst_task,
            strategy_task,
            head_planner_task
        ],
        process=Process.sequential,
        verbose=True
    )


    crew.kickoff()
    print("Final report saved at outputs/final_gtm_report.md")




if __name__ == "__main__":
    run_full_gtm_workflow()