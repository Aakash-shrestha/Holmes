from google.genai.types import Content, FunctionResponse, Part

from holmes import config

import math

def to_json_safe(value):
    if isinstance(value, float):
        return value if math.isfinite(value) else None

    if value is None or isinstance(value, (str, int, bool)):
        return value

    if isinstance(value, dict):
        return {k: to_json_safe(v) for k, v in value.items()}

    if isinstance(value, (list, tuple)):
        return [to_json_safe(v) for v in value]

    if hasattr(value, "to_dict"):   # pandas Series, DataFrame
        return to_json_safe(value.to_dict())

    if hasattr(value, "tolist"):    # numpy ndarray
        return to_json_safe(value.tolist())

    if hasattr(value, "item"):      # numpy / pandas scalars
        return to_json_safe(value.item())

    return str(value)

class AgentState:
    def __init__(self):
        self.messages = []
        self.step = 0

    def add_user_message(self, text):
        self.messages.append(Content(role="user", parts=[Part(text=text)]))

    def add_model_turn(self, response):
        self.messages.append(response.candidates[0].content)
        self.step += 1

    def add_tool_result(self, name, value):
        json_safe_value = to_json_safe(value)
        self.messages.append(
            Content(
                role="user",
                parts=[
                    Part(
                        function_response=FunctionResponse(
                            name=name, response={"result": json_safe_value}
                        )
                    )
                ],
            )
        )

    def has_steps_remaining(self):
        return self.step < config.MAX_STEPS
