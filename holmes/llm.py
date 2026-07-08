from google.genai import types


def call_llm(client, messages, tools) -> types.GenerateContentResponse:
    cfg = types.GenerateContentConfig(tools=tools)
    result = client.models.generate_content(
        model="gemini-2.0-flash", contents=messages, config=cfg
    )
    return result
