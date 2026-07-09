import pandas as pd

from holmes.tools.base import Tool


def make_run_code_tool(df):
    def run_code(code):
        namespace = {"df": df, "pd": pd}
        try:
            exec(code, namespace)
        except Exception as e:
            return f"{type(e).__name__}: {e}"
        if "result" not in namespace:
            return "Error: 'result' variable not defined in the code."
        return namespace["result"]

    return Tool(
        name="run_code",
        description="Run Python code with access to the provided DataFrame and pandas library. The code should define a variable named 'result' which will be returned.",
        parameters={
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to execute with given dataframe. The code should define a variable named 'result' which will be returned.",
                },
            },
            "required": ["code"],
        },
        func=run_code,
    )
