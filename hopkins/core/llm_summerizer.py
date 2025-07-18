from openai import OpenAI
import json
from hopkins.core.llm_prompt import PROMPT, JSON_SCHEMA

def summarize_to_json(cim_text):
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI analyst for private equity. "
                    "Return valid JSON matching the schema only."
                )
            },
            {
                "role": "user",
                "content": PROMPT.format(cim_text=cim_text)
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": JSON_SCHEMA
        }
    )

    content = response.choices[0].message.content or '{}'
    return json.loads(content)
