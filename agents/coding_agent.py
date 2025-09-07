from models.llm import gemini_chatml
from schema.agent_state import OutputModel
from prompts.basic_prompts import coder_agent_prompt
from tools.file_handling import read_file, list_files, write_file, create_folder
from tools.system import execute_command
from inspect import signature
import json
from time import sleep

message_history = []
available_tools = {
    "execute_command": execute_command,
    "read_file": read_file,
    "list_files": list_files,
    "write_file": write_file,
    "create_folder": create_folder
}

def call_tool(func, params):
    """
    Calls `func` with only the parameters it accepts.
    Extra keys in `params` are automatically skipped.
    """
    if params is None:
        params_dict = {}
    elif hasattr(params, "dict"):
        params_dict = params.model_dump()
    else:
        params_dict = params 

    sig = signature(func)
    filtered_params = {k: v for k, v in params_dict.items() if k in sig.parameters}
    return func(**filtered_params)

def get_model_response():
    response = gemini_chatml.chat.completions.parse(
        response_format=OutputModel,
        model="gemini-2.5-flash",
        messages=message_history
    )

    res = response.choices[0].message.parsed

    message_history.append({
        "role": "assistant",
        "content": res.model_dump_json()
    })

    return res

def get_task(file):
    task_description = "Task: "

    filePath = file.filePath
    task_description = task_description + f"filePath:{filePath}"
    task_description += " Steps: "
    for step in file.steps:
        task_description += step.step_detail

    return task_description

def perform_tasks(implementation):
    for task in implementation:
        task_description = get_task(task)
        dump_user_input = json.dumps({
            "step": "START",
            "content": task_description,
            "tool_name": None,
            "tool_input": None
        })
        message_history.append({
            "role": "user",
            "content": dump_user_input
        })

        # Chain of thought
        while True:
            res = get_model_response()
            
            if res.step == "PLAN":
                print("💭",res.content)
            elif res.step == "TOOL":
                print("🛠️ ",res.tool_name,":",res.tool_input)
                tool_func = available_tools[res.tool_name]
                tool_output = call_tool(tool_func, res.tool_input)
                dump_tool_output = json.dumps({
                    "step": "OBSERVE",
                    "content": tool_output,
                    "tool_name": None,
                    "tool_input": None
                })
                message_history.append({
                    "role": "user",
                    "content": dump_tool_output
                })
                print("👀",tool_output)
            else:
                print("✅",res.content)
                break
            sleep(10)
        

def call_coding_agent(state: dict):
    plan = state["plan"]
    implementations = state["architect"].implementations
    message_history.append({"role":"system","content": coder_agent_prompt(plan)})
    print("⛓️‍💥 Performing tasks using chain of thought") 
    perform_tasks(implementations)
    print("\n🎉  Your application is ready!")
    return state