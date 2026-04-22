import requests

API_URL = "https://v3.football.api-sports.io/"
API_KEY = "d5427e98f33ff48cc19aa584e1c926bb"  

HEADERS = {
    "x-apisports-key": API_KEY
}


# ⚽ 1. Get team info
def get_team_info(team: str) -> dict:
    response = requests.get(
        f"{API_URL}/teams",
        headers=HEADERS,
        params={"search": team},
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    teams = data.get("response", [])
    if not teams:
        return {"error": f"Team not found: {team}"}

    t = teams[0]["team"]
    return {
        "name": t["name"],
        "country": t["country"],
        "founded": t["founded"],
        "stadium": teams[0]["venue"]["name"]
    }


# ⚽ 2. Get live scores
def get_live_scores(league: str) -> dict:
    response = requests.get(
        f"{API_URL}/fixtures",
        headers=HEADERS,
        params={"live": "all"},
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    matches = data.get("response", [])

    results = []
    for m in matches:
        results.append({
            "home": m["teams"]["home"]["name"],
            "away": m["teams"]["away"]["name"],
            "score": f"{m['goals']['home']} - {m['goals']['away']}",
            "status": m["fixture"]["status"]["short"]
        })

    return {"matches": results}


# ⚽ 3. Player stats (basic)
def get_player_stats(player: str) -> dict:
    response = requests.get(
        f"{API_URL}/players",
        headers=HEADERS,
        params={"search": player},
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    players = data.get("response", [])
    if not players:
        return {"error": f"Player not found: {player}"}

    p = players[0]["player"]
    return {
        "name": p["name"],
        "age": p["age"],
        "nationality": p["nationality"]
    }


# ⚽ 4. Simple prediction (mock for now)
def predict_match(home_team: str, away_team: str) -> dict:
    return {
        "prediction": f"{home_team} vs {away_team} is expected to be a close match",
        "confidence": "low"
    }