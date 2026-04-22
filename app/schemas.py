FOOTBALL_TOOL_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_team_info",
            "description": "Get information about a football team including name, country, league, and stats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "team": {
                        "type": "string",
                        "description": "Team name, example: Real Madrid, Barcelona, PSG"
                    }
                },
                "required": ["team"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_live_scores",
            "description": "Get live football scores or match results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "league": {
                        "type": "string",
                        "description": "League name like Premier League, La Liga, Champions League"
                    }
                },
                "required": ["league"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_player_stats",
            "description": "Get statistics of a football player.",
            "parameters": {
                "type": "object",
                "properties": {
                    "player": {
                        "type": "string",
                        "description": "Player name, example: Messi, Ronaldo, Mbappe"
                    }
                },
                "required": ["player"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "predict_match",
            "description": "Predict the outcome of a football match based on teams and stats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "home_team": {
                        "type": "string"
                    },
                    "away_team": {
                        "type": "string"
                    }
                },
                "required": ["home_team", "away_team"]
            }
        }
    }
]