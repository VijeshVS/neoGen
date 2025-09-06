from models.llm import gemini_llm
from schema.llm_output_schema import ImplementationTask
from prompts.basic_prompts import architect_agent_prompt

def call_architect_agent(state: dict):
    plan = state["plan"]
    architect = gemini_llm.with_structured_output(ImplementationTask).invoke(architect_agent_prompt(plan))
    print("🏛️ done with application architect")
    return {**state, "architect": architect}