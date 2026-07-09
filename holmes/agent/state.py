from google.genai.types import Content, FunctionResponse, Part

from holmes import config


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
        self.messages.append(
            Content(
                role="user",
                parts=[
                    Part(
                        function_response=FunctionResponse(
                            name=name, response={"result": value}
                        )
                    )
                ],
            )
        )

    def has_steps_remaining(self):
        return self.step < config.MAX_STEPS
