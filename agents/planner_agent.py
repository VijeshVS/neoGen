from schema.llm_output_schema import Plan
from models.llm import gemini_llm
from prompts.basic_prompts import planner_agent_prompt

def call_planner_agent(state: dict):
    user_prompt = state["user_prompt"]
    plan = gemini_llm.with_structured_output(Plan).invoke(planner_agent_prompt(user_prompt))
    print("🗺️  done with application planning")
    return { **state, "plan": plan }