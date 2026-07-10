from holmes.agent.state import AgentState
from holmes.llm import call_llm
from holmes.tools.base import assemble_tools
from holmes.tools.inspect import make_inspect_tool
from holmes.tools.sandbox import make_run_code_tool


def run(client, df, goal):
    tools = [make_run_code_tool(df), make_inspect_tool(df)]
    api_tools, dispatch_table = assemble_tools(tools)

    state = AgentState()
    state.add_user_message(goal)

    done = False
    final_answer = "Reached MAX_STEPS without a final answer."  # default answer for when llm does not return any thing due to max steps reached

    while not done and state.has_steps_remaining():
        response = call_llm(client, state.messages, api_tools)
        state.add_model_turn(response)

        if not response.function_calls:
            done = True
            final_answer = response.text
        else:
            for call in response.function_calls:
                assert call.name is not None
                assert call.args is not None
                tool = dispatch_table[call.name]
                result = tool.func(**call.args)
                state.add_tool_result(call.name, result)

    return final_answer
