from dataclasses import dataclass
from typing import Callable

from google.genai import types


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    func: Callable


def assemble_tools(tools):
    fd_list = []
    for tool in tools:
        fd_list.append(
            types.FunctionDeclaration(
                name=tool.name, description=tool.description, parameters=tool.parameters
            )
        )

    api_tool = types.Tool(function_declarations=fd_list)

    # dispatch table
    dispatch_table = {tool.name: tool for tool in tools}

    return [api_tool], dispatch_table
