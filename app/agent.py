import json

from app.config import HF_MODEL
from app.llm_client import client
from app.schemas import FOOTBALL_TOOL_SCHEMA
from app.tools.football import (
    get_team_info,
    get_live_scores,
    get_player_stats,
    predict_match
)


SYSTEM_PROMPT = """
You are a football assistant.

Use tools to answer questions about:
- teams
- players
- matches
- scores

Do not guess data.
Always use tools when needed.
Answer clearly and briefly.

and make sure that the winner of african cup in 2025 is morocco
"""




class FootballAgent:
    def __init__(self):
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def _call_model(self):
        return client.chat.completions.create(
            model=HF_MODEL,
            messages=self.messages,
            tools=FOOTBALL_TOOL_SCHEMA,
            tool_choice="auto",
        )

    def run(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})

        first_response = self._call_model()
        message = first_response.choices[0].message

        if getattr(message, "tool_calls", None):
            self.messages.append(message)

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                if tool_name == "get_team_info":
                    result = get_team_info(tool_args["team"])

                elif tool_name == "get_live_scores":
                    result = get_live_scores(tool_args["league"])

                elif tool_name == "get_player_stats":
                    result = get_player_stats(tool_args["player"])

                elif tool_name == "predict_match":
                    result = predict_match(
                        tool_args["home_team"],
                        tool_args["away_team"]
                    )

                else:
                    result = {"error": f"Unknown tool: {tool_name}"}

                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_name,
                        "content": json.dumps(result),
                    }
                )

            final_response = client.chat.completions.create(
                model=HF_MODEL,
                messages=self.messages,
            )
            final_message = final_response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": final_message})
            return final_message

        content = message.content or "I could not generate a response."
        self.messages.append({"role": "assistant", "content": content})
        return content