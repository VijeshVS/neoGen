from langgraph.graph import StateGraph
from agents.architect_agent import call_architect_agent
from agents.planner_agent import call_planner_agent
from agents.coding_agent import call_coding_agent
from langgraph.constants import START, END
from scripts.prestart_msg import prestart_message

graph = StateGraph(dict)
graph.add_node("planner_agent",call_planner_agent)
graph.add_node("architect_agent",call_architect_agent)
graph.add_node("coding_agent",call_coding_agent)

graph.add_edge(START,"planner_agent")
graph.add_edge("planner_agent","architect_agent")
graph.add_edge("architect_agent","coding_agent")
graph.add_edge("coding_agent",END)

agent = graph.compile()

prestart_message()

try:
    user_prompt = input("👉 ")
    agent.invoke({
        "user_prompt": user_prompt
    })
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
except Exception as e:
    print(f"\nAn error occurred: {e}")