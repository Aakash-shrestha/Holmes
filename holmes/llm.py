from google.genai import types

from holmes.config import MODEL_NAME


def call_llm(client, messages, tools) -> types.GenerateContentResponse:
    cfg = types.GenerateContentConfig(tools=tools)
    result = client.models.generate_content(
        model=MODEL_NAME, contents=messages, config=cfg
    )
    return result
